import os

from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

from extra_api import extra_api
from init_db import init_db
from pet_api import pet_api
from questionnaire_api import questionnaire_api
from user_api import user_api


def create_app(test_config=None):
    app = Flask(__name__)
    if test_config:
        app.config.update(test_config)

    init_db()
    Swagger(app)

    allowed_origins = os.environ.get(
        "PET_ADOPTION_ALLOWED_ORIGINS",
        "http://localhost:3000,http://127.0.0.1:3000",
    ).split(",")
    CORS(app, resources={r"/api/*": {"origins": allowed_origins}})

    app.register_blueprint(user_api, url_prefix="/api")
    app.register_blueprint(pet_api, url_prefix="/api")
    app.register_blueprint(extra_api, url_prefix="/api")
    app.register_blueprint(questionnaire_api, url_prefix="/api")

    @app.route("/")
    def home():
        return "API is running"

    return app


app = create_app()


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=5000, debug=debug)
