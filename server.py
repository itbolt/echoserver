import os
from flask import Flask, request, jsonify, render_template
import openai
import pymongo

mongo_client = pymongo.MongoClient('mongodb+srv://mnguyen:Ntmntm1019@cluster0.ybulhme.mongodb.net/')
db = mongo_client['NuocDB']
collection = db['ResponseLog']

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
    user_message = request.form.get('message')
    
    # Call the OpenAI API to get a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_message,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None
    )
    
    # Extract the response text from the API response
    chat_response = response['choices'][0]['text'].strip()
    
    return chat_response


@app.route('/reaction', methods=['POST'])
def reaction():
    data = request.get_json()
    question = data.get('question')
    response = data.get('response')
    reaction = data.get('reaction')
    
    # Store the user's reaction in the MongoDB collection
    document = {
        'question': question,
        'response': response,
        'reaction': reaction
    }
    collection.insert_one(document)
    
    return jsonify(success=True)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)