"""
handles server/ web functionality for
torrent client.
"""


from flask import Flask, Response
import time
import getpass

app = Flask(__name__)

@app.route('/hello')
def greet():
    def data_generator():
        text = f"Hello, from {getpass.getuser()}"
        for letter in text:
            time.sleep(0.5)
            yield letter
    return Response(data_generator(), mimetype="text/plain")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)