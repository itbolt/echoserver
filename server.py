import os
from flask import Flask, request, jsonify, render_template
import openai
app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    message = request.form.get('message')
    return message + " " + message

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    
    # Call the OpenAI API to get a response
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can choose a different engine if needed
        prompt=user_message,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None
    )
    
    # Extract the response text from the API response
    chat_response = response['choices'][0]['text'].strip()
    
    return chat_response

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)