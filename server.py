"""
server.py

A Flask application for analyzing the emotions expressed in user-provided text 
using the Watson NLP service. It provides an endpoint to receive text and 
returns the dominant emotion with a corresponding score.
"""

from flask import Flask, request, render_template  # Removed jsonify as it's not used
from EmotionDetection.emotion_detector import emotion_predictor

app = Flask(__name__)

def emotion_response_formatting(label, score):
    """Format the emotion response."""
    split_label = label.split('_')
    if len(split_label) > 1:
        return f"The given text has been identified as '{split_label[1]}' with a score of {score}."
    return f"The given text has been identified as '{label}' with a score of {score}."


@app.route("/emotionDetector", methods=['GET', 'POST'])
def sentiment_analyzer():
    """Analyze the sentiment of the given text."""
    if request.method == 'GET':
        text_to_analyze = request.args.get('textToAnalyze')
    elif request.method == 'POST':
        text_to_analyze = request.form.get('textToAnalyze')  # If sent as form data
    else:
        return "Unsupported method", 405

    # Call the emotion predictor function
    response = emotion_predictor(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again!", 400

    label, score = response
    return emotion_response_formatting(label, score)


@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='localhost', port=5000)
