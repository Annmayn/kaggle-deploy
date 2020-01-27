import joblib
from models.base import Model
from sklearn.linear_model import SGDClassifier, stochastic_gradient
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import json


class NlpGettingStarted(Model):
    model_name = "nlp-getting-started.pkl"
    vectorizer_name = "nlp-getting-started-vectorizer.pkl"
    required = ['text']

    @classmethod
    def validate_body(cls):
        # validate body
        pass

    @classmethod
    def make_prediction(cls, body):
        text = body['text']
        print('->', text)
        model = joblib.load(cls.base_location + cls.model_name)
        vectorizer = joblib.load(cls.base_location + cls.vectorizer_name)
        text_transformed = vectorizer.transform(text)
        y_pred = model.predict(text_transformed)
        print('->', y_pred)
        return y_pred.tolist()
