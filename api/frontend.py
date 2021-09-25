from api import app
from flask import render_template, send_from_directory
import os

def react_app():
    @app.route("/Admin", defaults={'path': ''})
    @app.route('/<path:path>')
    def admin_app(path):
        print("the requested path:", path)
        print(app.static_folder + '/build/' + path)
        if path != "" and os.path.exists(app.static_folder + '/build/' + path):
            print("returning : ",path)
            return send_from_directory(app.static_folder,'build/' + path)
        return send_from_directory(app.static_folder, "build/index.html")

def landing_page_app():
    @app.route("/")
    def landing_page():
        return render_template("LandingPage/index.html")

def client_react_app():
    @app.route("/Certificate")
    def client_app():
        return "this is client app"