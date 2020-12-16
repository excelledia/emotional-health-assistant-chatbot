
from helper import get_response 

from flask import Flask, render_template, request,json, jsonify

from flask_cors import CORS

app = Flask(__name__,template_folder='template')
CORS(app)

@app.route('/api/v1.0/response', methods=['POST'])
def chatbot_response_json():
    print(request)
    if not request.json or not 'query' in request.json:
        abort(400)
    user = 1
    response = str(get_response(request.json['query'],user))
    print(response)
    return jsonify({'message': response})

@app.route('/api/v1.0/test', methods=['GET'])
def chatbot_test():
    # if not request.json or not 'query' in request.json:
    #     abort(400)
    # user = 1
    # response = str(get_response(request.json['query'],user))
    # print(response)
    # return jsonify({'message': response})
    return ('jjjj')

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