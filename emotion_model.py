from transformers import pipeline

emotion_classifier = pipeline("text-classification", 
                              model="j-hartmann/emotion-english-distilroberta-base",
                              return_all_scores=False)

def get_emotion(text):
    result = emotion_classifier(text)
    return result[0]['label'].lower()
