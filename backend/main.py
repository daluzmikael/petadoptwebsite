from flask import Flask
from flasgger import Swagger
from user_api import user_api
from pet_api import pet_api
from extra_api import extra_api
from flask_cors import CORS


app = Flask(__name__)
swagger = Swagger(app)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

app.register_blueprint(user_api)
app.register_blueprint(pet_api)
app.register_blueprint(extra_api)

@app.route('/')
def home():
    """Api home"""
    return 'API is running'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
