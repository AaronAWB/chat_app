from flask import Flask, request
from src import create_app

app = create_app()

messages = [
    {
        "id": 1,
        "user": "AaronAWB",
        "message": "This is a test message."
    },
    {
        "id": 2,
        "user": "SecondUser",
        "message": "This is a message in response to the test message"
    }
]

users = [
    {
        "id": 1,
        "user": "AaronAWB"
    },
    {
        "id": 2,
        "user": "SecondUser"
    }
]

@app.route('/api/messages', methods = ['GET'])
def return_current_messages():
    return messages, 200

@app.route('/api/messages', methods = ['POST'])
def create_message():
    request_data = request.json
    messages.append(request_data)
    return 'Message added.', 200

@app.route('/api/users', methods = ['GET'])
def get_users():
    return users, 200

@app.route('/api/users/<id>', methods = ['GET'])
def get_user(users, id):
    for user in users:
        if user["id"] == id:
            return user
    return "No user with that ID found.", 404

@app.route('/api/users', methods = ['POST'])
def create_user():
    request_data = request.json
    users.append(request_data)
    return 'User added.', 201

if __name__ == '__main__':
    app.run(debug=True)