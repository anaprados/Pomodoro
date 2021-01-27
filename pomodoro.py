import config
import getopt
import sys

from slack import WebClient
from slack.errors import SlackApiError

from helper import get_help_page


def get_args(argv):
    """
    Get the status option and time from the arguments. The options can be:
        - Clear status
        - Working remotely
    :param argv:
    :return: clear, remote, time
    """
    clear = remote = False
    time = 0
    try:
        opts, args = getopt.getopt(argv, 'crt:', ['clear', 'remote', 'time='])
        for opt, arg in opts:
            if opt in ('-c', '--clear'):
                clear = True
            elif opt in ('-r', '--remote'):
                remote = True
            elif opt in ('-t', '--time'):
                # Convert to seconds
                time = int(arg) * 60
        return clear, remote, time
    except getopt.GetoptError:
        get_help_page()


def get_status_info(argv):
    """
    Get the status emoji, text and time based on the arguments
    :param argv:
    :return: emoji, text, time
    """
    # Default status: pomodoro
    emoji = ':tomato:'
    text = ''

    clear, remote, time = get_args(argv)
    if clear:
        # Remove status
        emoji = ''
        time = 0
    elif remote:
        # Status: working remotely
        emoji = ':house_with_garden:'
        text = 'Working remotely'
    return emoji, text, time


def set_slack_profile(slack_token, emoji, text, time):
    """
    Call Slack to change status
    :param slack_token:
    :param emoji:
    :param text:
    :param time:
    """
    client = WebClient(token=slack_token)
    client.api_call(
        api_method='users.profile.set',
        json={'profile': {
            'status_emoji': emoji,
            'status_text': text,
            'status_expiration': time}}
    )


def main(argv):
    emoji, text, time = get_status_info(argv)

    for slack_name, slack_token in config.slack_workspaces.items():
        try:
            set_slack_profile(slack_token, emoji, text, time)
        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            print(f'Error in {slack_name}: {e.response["error"]}')
            return
        print(f'Status updated in {slack_name}!')


if __name__ == "__main__":
    main(sys.argv[1:])
