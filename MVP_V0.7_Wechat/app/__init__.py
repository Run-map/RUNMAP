from flask import Flask
from config import Config
import logging
from .logger import handler
from .main import main as main_blueprint

logger = logging.getLogger(__file__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)

    app.register_blueprint(main_blueprint)

    return app
