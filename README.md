# Project 2

Harvard CS50W: Web Programming with Python and JavaScript

Hello! Welcome to my online messaging service Flack!

Username is stored in local memory so it is only needed to be entered once
after entering, you are able to create and view list of channels

After choosing a channel, your choice is stored in local memory and the webpage will
return to the previously entered chatroom if the window is closed or refreshed.

Chatrooms store 100 most recent messages, any messages sent while in the room have a bullet point beside them
Each chat includes the hour and time the message has been sent to the channel
Chatroom messages show up without the need to refresh with use of SocketIO

After pressing back in channel the local memory is freed and does not make you return to previously entered channel,
I hope you enjoy!

File contents:
application.py - flask application, contains routing of various webpages
requirements.txt - contains all the packages needed to be installed to run code (none added)
templates folder - contains all html + javascript code
templates/index - html + javascript for home page registration of use
templates/createchannel - html + javascript for creating and viewing channels
templates/chatroom - html + javascript for entering chatroom

Personalized touch:
Username and channel is broadcasted to everyone in all channels when a user joins a channel