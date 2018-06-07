# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import Config
from .base_model import BaseModel

db = SQLAlchemy(model_class=BaseModel)
api = Api()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    Config.init_app(app)
    db.init_app(app)

    from .auth import api_auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app