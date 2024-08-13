from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_comment = request.args.get('comment', '')
    return f'<html><body><h1>User comment: {user_comment}</h1></body></html>'

if __name__ == '__main__':
    app.run(port=8080)