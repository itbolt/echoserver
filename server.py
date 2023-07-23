import os
from flask import Flask, request, jsonify, render_template
import openai
import pymongo

mongodb_url = os.environ.get("MONGODB_URL")

try:
    # Connect to the MongoDB server
    client = MongoClient(mongodb_url)
    db = client["NuocDB"]  # Replace "mydatabase" with your database name
    collection = db["ResponseLog"]  # Replace "mycollection" with your collection name

    print("Connected to MongoDB successfully!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

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
    response1 = request.form.get('message')
    return response1 + " " + response1


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
    
    return render_template('index.html', response=chat_response)



@app.route('/feedback', methods=['POST'])
def feedback():
    reaction = request.json.get('reaction')

    # Store the reaction in the MongoDB collection
    feedback_data = {
        'reaction': reaction
    }
    collection.insert_one(feedback_data)

    print("Data received:", feedback_data)  # Add this line to print the data

    # Return a response to the client (optional)
    return jsonify({'message': 'Feedback received'})





if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)