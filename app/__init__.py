from flask import Flask
from flask_mysqldb import MySQL
from config import Config
# from .gemini_service import GeminiService


mysql = MySQL()

def create_app():
    app = Flask(__name__)
    # app.config.from_object(Config)

    # mysql.init_app(app)

    # from .routes import bp as main_bp
    # app.register_blueprint(main_bp)

    return app