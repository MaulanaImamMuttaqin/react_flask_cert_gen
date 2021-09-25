from api import app
from flask import render_template, send_from_directory
import os

def admin_react_app():
    @app.route("/Admin", defaults={'path': ''})
    @app.route('/<path:path>')
    def admin_app(path):
        print(path)
        if path != "" and os.path.exists(app.static_folder + '/admin/' + path):
            return send_from_directory(app.static_folder,'admin/' + path)
        return send_from_directory(app.static_folder, "admin/index.html")


def landing_page_app():
    @app.route("/")
    def landing_page():
        return render_template("LandingPage/index.html")


def client_react_app():
    @app.route("/certificate", defaults={'path': ''})
    @app.route("/<path:path>")
    def client_app(path):
        print("client app", path)
        if path != "" and os.path.exists(app.static_folder + '/client/' + path):
            return send_from_directory(app.static_folder,'client/' + path)
        return send_from_directory(app.static_folder, "client/index.html")