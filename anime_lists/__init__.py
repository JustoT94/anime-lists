from flask import Flask
from extensions import db, migrate
from .main import main_bp
from config import config_map, DevelopmentConfig

def create_app(config_name="development"):
    app = Flask(__name__)
    config_class = config_map.get(config_name, DevelopmentConfig)
    app.config.from_object(config_class)    
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main_bp)    
    return app

