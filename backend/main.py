from flask import Flask
from user_api import app as user_app
from pet_api import app as pet_app

app = Flask(__name__)

# Register all blueprints
app.register_blueprint(user_app)
app.register_blueprint(pet_app)

if __name__ == '__main__':
    app.run(debug=True)
