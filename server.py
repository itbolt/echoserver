from flask import Flask, request

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    text = data['text']
    response = f"{text} {text}"
    return response


@app.route('/')
def index():
    return "hello world"

if __name__ == '__main__':
    app.run()