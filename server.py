from flask import Flask, request, abort
import datetime
import time

x = datetime.datetime.now()

print(x.strftime("%c"))

app = Flask(__name__)

messages = [
    {'username': 'Admin', 'text': 'Lorem Ipsum', 'time': 0.0}
]

users = {
    'Admin': '12345'
}

@app.route("/")
def hello():
    return "Welcome to A-Chat"

@app.route("/status")
def status():
    t = datetime.datetime.now()
    TU = len(users)
    TM = len(messages)
    return {
        "Status": True, "Messanger Title": "A-chat", 'Server Time': (t.strftime("%x %X")),
        'Total users': TU, 'Total messages': TM
    }

   

@app.route("/send", methods=['POST'])
def send():
    RJ = request.json
    username = RJ['username']
    password = RJ['password']
    if username in users:
        if password != users[username]:
            return abort(401)
    else:
        users[username] = password

    text = RJ['text']
    current_time = time.time()
    message = {'username': username, 'text': text, 'time': current_time}
    messages.append(message)
    print(messages)
    return {"ok": True}

@app.route("/msgs")
def msgs():
    after = float(request.args.get('after'))
    FM = []
    for message in messages:
        if message['time'] > after:
            FM.append(message) 

    return {
        'messages': FM
    }

app.run()