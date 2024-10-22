# Install the required packages
# Run the following command to install Flask and google-generativeai
# pip install Flask google-generativeai

from flask import Flask, request, render_template
import google.generativeai as genai
import os
import markdown

# Configure the API key (you need to set up your API_KEY in the environment variables)
genai.configure(api_key=os.environ.get("API_KEY"))

# Initialize the Flask app
app = Flask(__name__)

# Route to handle the form submission
@app.route('/', methods=['GET', 'POST'])
def chat():
    response = None
    if request.method == 'POST':
        query = request.form['query']
        try:
            # Use the generative model to get a response
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(query)
            response = markdown.markdown(response.text)
        except Exception as e:
            response = markdown.markdown(f"Error: {str(e)}")

    return render_template('app.html', response=response)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
