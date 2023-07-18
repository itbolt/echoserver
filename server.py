import os
from flask import Flask, request, jsonify, render_template
import openai

#print(models.data[0].id)

# create a chat completion
#chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

# print the chat completion
#print(chat_completion.choices[0].message.content)

#openai.api_key = os.environ.get("OPENAI_KEY")

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_KEY")

# list models
models = openai.Model.list()

print(models.data[0].id)

# create a chat completion
completion = openai.Completion.create(model="text-davinci-003", prompt="Hello world")
print(completion.choices[0].text)




@app.route('/')
def home():
    return render_template('index.html')



@app.route('/echo', methods=['POST'])
def echo():
    message = request.form.get('message')
    return message + " " + message


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