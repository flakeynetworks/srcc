from flask import Flask

from backend.src.api.api_manager import APIManager
from backend.src.endpoints import device_endpoint, zones_endpoint

api_manager = APIManager()

flask_app = Flask(__name__, static_folder="frontend/static/", template_folder="frontend/templates/")
flask_app.register_blueprint(device_endpoint.construct_blueprint(api_manager), url_prefix="/device")
flask_app.register_blueprint(zones_endpoint.construct_blueprint(api_manager), url_prefix="/zones")


@flask_app.route('/')
def hello_world():
    return flask_app.send_static_file('index.html')


@flask_app.route('/images/<path:path>')
def send_images(path):
    return flask_app.send_static_file('images/' + path)


@flask_app.route('/css/<path:path>')
def send_css(path):
    return flask_app.send_static_file('css/' + path)

if __name__ == '__main__':
    flask_app.run()
