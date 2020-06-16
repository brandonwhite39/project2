import os

from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels = []
messages = {}

@app.route("/")
def index():
    return render_template("index.html")

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
    
    room=data["channelss"]
    join_room(data["channelss"])
    selection = data["selection"]#message
    name = data["name"]#user name who wrote message
    h = data["h"]#hour of message
    m = data["m"]#minute of message
    s = data["s"]#second of message
    fullmsg = "%s (%s:%s:%s): %s" % (name, h, m, s, selection)
    #append to messages["channel"], pass into emit
    channel = data["channelss"]
    print(len(messages[channel]))
    if(len(messages[channel]) == 100):#if 100 messages already
        messages[channel].pop(0)
        messages[channel].append(fullmsg)
        emit("submit message", {"messages": selection, "name": name,
                                "fullmsg":fullmsg, "h":h,
                                "m":m, "s":s}, broadcast=True, room=room)
    else:
        messages[channel].append(fullmsg)
        emit("submit message", {"messages": selection, "name": name,
                                "fullmsg":fullmsg, "h":h,
                                "m":m, "s":s}, broadcast=True, room=room)

@socketio.on("join room")
def join(data):
    text = data["mess"]
    room = data["channelss"]
    print("can u see me")
    emit("new message", {"text": text}, broadcast=True)
