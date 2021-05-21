from flask import Flask
from ml.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    from ml.models.routes import models

    app.register_blueprint(models)

    return app