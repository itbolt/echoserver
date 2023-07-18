import os
from flask import Flask, request, jsonify, render_template
import openai

#print(models.data[0].id)

# create a chat completion
#chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

# print the chat completion
#print(chat_completion.choices[0].message.content)

openai.api_key = os.environ.get("OPENAI_KEY")

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/echo', methods=['POST'])
def echo():
    message = request.form.get('message')
    return message + " " + message


@app.route('/chat', methods=['POST'])
def chat_with_openai():
    data = request.get_json()
    user_input = data.get('text', '')
    
    # Call the OpenAI API to get the chat response
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        max_tokens=100,
    )
    
    chat_response = response.choices[0].text.strip()
    return jsonify({'response': chat_response})



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)