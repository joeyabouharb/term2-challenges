from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    """
    home page
    """
    return 'Hello, World!'


import didyoueat.routes.lunches
import didyoueat.routes.person


if __name__ == "__main__":
    app.run()

