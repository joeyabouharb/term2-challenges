from flask import Flask
from didyoueat.routes.lunches import lunch_routes
from didyoueat.routes.person import person_routes
app = Flask(__name__)


@app.route('/')
def home():
    """
    home page
    """
    return 'Hello, World!'

app.register_blueprint(lunch_routes)
app.register_blueprint(person_routes)


if __name__ == "__main__":
    app.run()

