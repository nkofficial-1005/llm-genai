import os

from flask import Flask, request

import google.auth
import vertexai
from vertexai.generative_models import GenerativeModel

_, project = google.auth.default()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        animal = request.form['animal']
        vertexai.init(project=project, location="us-central1")
        model = GenerativeModel("gemini-1.5-flash")
        prompt = f"Give me 10 fun facts about {animal}. Return this as html without backticks."
        response = model.generate_content(prompt)
        return response.text
    else:
        return '''
            <form method="POST">
                <label for="animal">Enter an animal:</label>
                <input type="text" id="animal" name="animal">
                <input type="submit" value="Submit">
            </form>
        '''

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))