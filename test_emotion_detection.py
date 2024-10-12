import unittest
from EmotionDetection import emotion_predictor

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        dominant_emotion, _ = emotion_predictor("I am glad this happened")
        self.assertEqual(dominant_emotion, 'joy', "Expected 'joy' but got something else!")

    def test_anger(self):
        dominant_emotion, _ = emotion_predictor("I am really mad about this")
        self.assertEqual(dominant_emotion, 'anger', "Expected 'anger' but got something else!")

    def test_disgust(self):
        dominant_emotion, _ = emotion_predictor("I feel disgusted just hearing about this")
        self.assertEqual(dominant_emotion, 'disgust', "Expected 'disgust' but got something else!")

    def test_sadness(self):
        dominant_emotion, _ = emotion_predictor("I am so sad about this")
        self.assertEqual(dominant_emotion, 'sadness', "Expected 'sadness' but got something else!")

    def test_fear(self):
        dominant_emotion, _ = emotion_predictor("I am really afraid that this will happen")
        self.assertEqual(dominant_emotion, 'fear', "Expected 'fear' but got something else!")

if __name__ == '__main__':
    unittest.main()
