import requests
from flask import Flask, request
from .routes import api

def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)

    @app.after_request
    def send_to_webhook(response):
        if response.status_code == 200 and request.endpoint == 'api.movie_info':
            try:
                webhook_url = "https://eo9m0nh4z7lacho.m.pipedream.net"
                data = response.get_json()
                if data:
                    wh_res = requests.post(webhook_url, json=data, timeout=5000)
                    print(wh_res.text)
            except Exception as e:
                app.logger.error(f"Error sending to webhook: {e}")
        return response

    return app
