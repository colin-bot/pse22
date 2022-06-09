#!/usr/bin/env python
# encoding: utf-8
import json
import datetime as dt
from flask import Flask, Request, request, abort
from chat import Chat
app = Flask(__name__)

chats = {'0': Chat(0)}


@app.route('/')
def index():
    return 'Welcome on home'


@app.route('/get_chat/<meeting_id>', methods=['GET'])
def get_chat(meeting_id):
    if meeting_id not in chats:
        print(f'Tried to access {meeting_id}')
        return abort(404)

    # formaat voor json (datetime, message_id, user_id, message)
    return json.dumps(chats[meeting_id].get_dictionary())


@app.route('/send_message', methods=['PUT'])
def add_message_to_chat():
    data = json.loads(request.get_json())

    chat_id = str(data['chat_id'])
    user_id = data['user_id']
    message = data['message']
    time = str(dt.datetime.strptime(data['time'], '%d/%m/%Y %H:%M:%S'))

    if message == '/clear':
        chats[chat_id].message_list = []
        return ''

    chats[chat_id].create_message(user_id, time, message)

    print(chats[chat_id].message_list)

    return ''


# app.run(ssl_context='adhoc')
