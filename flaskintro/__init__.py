from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from .config import DevelopmentConfig, TestingConfig, ProductionConfig
from .models import db
from .routes import main as main_blueprint
from flasgger import Swagger
import os
from dotenv import load_dotenv

load_dotenv()

CONFIG_MAP = {
    "DevelopmentConfig": DevelopmentConfig,
    "TestingConfig": TestingConfig,
    "ProductionConfig": ProductionConfig,
}

def create_app(config_override=None):
    app = Flask(__name__)

    config_name = os.getenv("FLASK_CONFIG", "DevelopmentConfig")
    app.config.from_object(CONFIG_MAP[config_name])
    # ✅ Override to SQLite only if explicitly asked (for CI or local fast tests)
    if app.config.get("TESTING") and os.getenv("USE_SQLITE_FOR_TESTS") == "1":
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    if config_override:
        app.config.update(config_override)

    db.init_app(app)
    app.register_blueprint(main_blueprint)

    Swagger(app)

    with app.app_context():
        db.create_all()

    # ✅ Add custom error handlers here
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500

    return app
