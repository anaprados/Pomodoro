# Pomodoro 🍅
pomodoro.py es un pequeño script que nos facilita los cambios de estado de Slack cuando queremos avisar a los demás que estamos trabajando, basándonos, cómo no, en la [técnica Pomodoro](https://es.wikipedia.org/wiki/Técnica_Pomodoro).

## Comenzando 🚀
Antes de poder poner en funcionamiento este script, necesitamos tener un token de Slack por cada workspace que queramos manejar. Para esto, debemos crear una app (o usar alguna que haya creada en el workspace). Los pasos de cómo hacerlo se pueden seguir [aquí](https://metadrop.net/articulos/desarrollar-aplicacion-pomodoro-slack-php).

Lo importante es que la app tenga permisos para modificar el estado del usuario, por lo que debemos de asegurarnos que en la pestaña **Features/OAuth & Permissions**, el apartado **User Token Scopes** contenga el permiso **[users.profile:write](https://api.slack.com/scopes/users.profile:write)**.

Una vez instalada la aplicación, generamos un **OAuth Access Token** para poder configurar el script.

## Pre-requisitos 📋
Para ejecutar el script se requiere instalar el paquete **slackclient**. Si quieres usar un entorno virtual y no sabes cómo, sigue los pasos [aquí](https://docs.python.org/3/tutorial/venv.html).

El proyecto contiene un archivo **requirements.py** para facilitar la instalación:
```
pip install -r requirements.txt
```

## Configuración 🔧
Necesitamos que el script sepa en qué workspaces debe cambiar el estado, para ello debemos crear un archivo **config.py** en la misma raiz del proyecto con la siguiente estructura:

```
slack_workspaces = {
    'nombre_workspace_1': 'xoxp-XXXX-XXXX-XXXX-XXXX',
    'nombre_workspace_2': 'xoxp-XXXX-XXXX-XXXX-XXXX',
}
```

## Cómo funciona 📖
El script tiene tres funciones:
* Cambiar el estado a 🍅 cuando quieras avisar de que estás ocupado:
```
python pomodoro.py
```

* Borrar el estado cuando quieras avisar de que ya no estás ocupado:
```
python pomodoro.py --clear
```

* Debido al auge del teletrabajo, puedes cambiar tu estado a 🏡 cuando no estés ocupado y trabajando desde casa:
```
python pomodoro.py --remote
```

Además, puedes configurar el tiempo que quieres que dure el cambio de estado (esto no aplica a opción de borrarlo). Una vez ha pasado el tiempo configurado, el estado se borrará:
```
python pomodoro.py --time TIEMPO_EN_MINUTOS
```

## Recursos 🛠️

Para crear este proyecto se han usado los siguientes recursos:

* [Cómo desarrollar una aplicación de Pomodoro para Slack en PHP](https://metadrop.net/articulos/desarrollar-aplicacion-pomodoro-slack-php)
* [Basic usage of slackclient](https://slack.dev/python-slackclient/basic_usage.html)
* [Una plantilla para hacer un buen README.md](https://gist.github.com/Villanuevand/6386899f70346d4580c723232524d35a)

---
⌨️ con ❤️
