from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import logging

app = Flask(__name__, template_folder="templates", static_folder="static", 
           static_url_path="/static/")
#socketio = SocketIO(app, logger=True, engineio_logger=True)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('client_message')
def receive_message (client_msg):
    emit('server_message', client_msg, broadcast=True)

if __name__ == "__main__":
    #app.run(debug=True)

    # Without log_output flask logs doesnt show on stdout
    socketio.run(app, log_output=True)
    