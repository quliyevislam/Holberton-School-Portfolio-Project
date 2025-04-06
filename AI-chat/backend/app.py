from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
import os

app = Flask(__name__)
CORS(app)

client = genai.Client(api_key=os.getenv('GOOGLE_GEMINI_API_KEY'))
ai_response_directives = 'Respond in a maximum of 8 sentences.'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    response = client.models.generate_content(model='gemini-2.0-flash', contents=data.get('message')) 
    return jsonify(response.text)

if __name__ == "__main__":
    app.run(debug=True)