
from helper import get_response 

from flask import Flask, render_template, request

from flask_cors import CORS

app = Flask(__name__,template_folder='template')
CORS(app)

@app.route("/")
def home():
    return render_template("chatbot.html")

@app.route("/get")
def chatbot_response():
    userText = request.args.get('message')
    user = 1
    response = str(get_response(userText,user))
    return (response)


if __name__ == "__main__":
    app.run(host='localhost',debug=True)
