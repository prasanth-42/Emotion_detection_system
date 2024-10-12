import requests
def emotion_predictor(text_to_analyze):
    url = "https://an-watson-emotion.laba.akills.network/vi/watson.runtime.nin.vi/HinService/EmotionPredics"
    headers = {
        "grpo-metadata-mm-model-id": "emotion aggregated-workflow_lang_en_stock"
    }
    if not text_to_analyze or text_to_analyze.strip() == "":
        raise ValueError("Input text is blank. Please provide valid text for analysis.")
    data = {
        "document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 400:
        return None, None 
    response.raise_for_status()
    formatted_response = response.json()
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    dominant_score = emotions[dominant_emotion]
    return dominant_emotion, dominant_score
try:
    print(emotion_predictor("I love new technology."))  # Normal case
    print(emotion_predictor(""))  # This should raise an error due to blank input
except ValueError as e:
    print("Error:", e)
