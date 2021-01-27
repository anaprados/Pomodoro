import argparse
import sys


def get_help_page():
    parser = argparse.ArgumentParser(
        description='''Change the slack status.''')
    parser.add_argument('-c', '--clear', action='store_true', help="Clear status")
    parser.add_argument('-r', '--remote', action='store_true', help="Set working remotely status")
    parser.add_argument('-t', '--time', type=int,
                        help="Set a time in the future when the status will clear (in minutes)")
    parser.parse_args()
    sys.exit()
