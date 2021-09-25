import os
from flask import Flask, send_from_directory
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
# from flask_praetorian import Praetorian
from flask_migrate import Migrate



app = Flask(__name__, static_folder="../frontend", template_folder="../frontend")
app.config.from_object(Config)



db = SQLAlchemy(app)
jwt = JWTManager(app)
from .Models import User
# guard = Praetorian(app, User)

def create_app():
    migrate = Migrate(app, db)
    CORS(app)
    
    # from .frontend import react_app
    from .frontend import landing_page_app, admin_react_app, client_react_app
    landing_page_app()
    admin_react_app()
    client_react_app()
    
    from .routes.Authentication import auth
    from .routes.Client import client

    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(client, url_prefix="/client")
    

    return app

