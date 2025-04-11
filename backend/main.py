from flask import Flask
from user_api import user_api
from pet_api import pet_api
from extra_api import extra_api   # <-- ADD THIS

app = Flask(__name__)

app.register_blueprint(user_api)
app.register_blueprint(pet_api)
app.register_blueprint(extra_api)  # <-- AND THIS

@app.route('/')
def home():
    return 'API is running! Try /api/pets or /api/profile'

if __name__ == '__main__':
    app.run(debug=True)

