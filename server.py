import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    text = data['text']
    response = f"{text} {text}"
    return response

@app.route('/', methods=['GET'])
def home():
    return "hello! This is home page"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)