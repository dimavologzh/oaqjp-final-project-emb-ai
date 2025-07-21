from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    
    # Extract all items except the last one
    items = list(response.items())
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

    # Return a formatted string with the sentiment label and score
    return output


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

