from flask import Flask


app = Flask(__name__)

@app.route('/')
class HomeController():
    def get_index():
        return 'hello'