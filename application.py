import os

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels = []
messages = {}

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
    return render_template("chatroom.html", channel=channel, messages=messages)

@socketio.on("add channel")
def newChannel(channel):
    channels.append(channel)
    data = {"channels": channels}
    
    messages[channel] = []
    print(channels)
    print(messages)
    emit("all channels", data, broadcast=True)

@socketio.on("submit message")
def message(data):
    selection = data["selection"]
    #append to messages["channel"], pass into emit
    channel = data["channelss"]
    messages[channel].append(selection)
    emit("submit message", {"messages": messages[channel]}, broadcast=True)


