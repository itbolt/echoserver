from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    text = data['text']
    response = text + " " + text
    return response


@app.route('/')
def index():
  return '', 200

if __name__ == '__main__':
    app.run()