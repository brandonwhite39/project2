import os

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/channel")
def channel():
    return render_template("channel.html")


@app.route("/createchannel")
def createchannel():
    return render_template("createchannel.html", channels=channels)

@app.route("/chatroom/<channel>")
def chatroom(channel):
    return render_template("chatroom.html", channel=channel)

@socketio.on("add channel")
def newChannel(channel):
    channels.append(channel)
    data = {"channels": channels}
    emit("all channels", data, broadcast=True)

