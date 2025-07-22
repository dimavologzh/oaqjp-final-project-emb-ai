""" This project uses the Emotion Predict function of the IBM Watson NLP Library
    for a text emotion detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """ Function to detect emotions """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    items = list(response.items())

    # Check if the first value is None, indicating an error or invalid input
    if items[-1][1] is None:
        output = "Invalid text! Please try again!"
    else:
        # Extract all items except the last one
        emotion_items = items[:-1]  # all except 'dominant_emotion'
        dominant = items[-1][1]     # value of 'dominant_emotion'

        # Build the sentence
        output = "For the given statement, the system response is "

        # Add all emotion pairs with correct punctuation
        for i, (emotion, score) in enumerate(emotion_items):
            if i == len(emotion_items) - 1:
                output += f"and '{emotion}': {score}. "
            else:
                output += f"'{emotion}': {score}, "

        # Add the dominant emotion part
        output += f"The dominant emotion is {dominant}."

        # Return a formatted string with the emotions labels and scores

    return output

@app.route("/")
def render_index_page():
    """ Function to render the Web App main page """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
