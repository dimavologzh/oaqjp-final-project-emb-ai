import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the emotion scores from the response
    if response.status_code == 200:
        anger_score = float(formatted_response['emotionPredictions'][0]['emotion']['anger'])
        disgust_score = float(formatted_response['emotionPredictions'][0]['emotion']['disgust'])
        fear_score = float(formatted_response['emotionPredictions'][0]['emotion']['fear'])
        joy_score = float(formatted_response['emotionPredictions'][0]['emotion']['joy'])
        sadness_score = float(formatted_response['emotionPredictions'][0]['emotion']['sadness'])

        scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
        }

        dominant_emotion = max(scores, key=scores.get)
        output = scores.copy()
        output ['dominant_emotion'] = dominant_emotion

    # If the response status code is 400 or 500, set label and score to None
    elif response.status_code == 400 or response.status_code == 500:
        anger_score = disgust_score = fear_score = joy_score = sadness_score = dominant_emotion = None
        output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
        }
    
     # Returning a dictionary containing sentiment analysis results
    return output

