from fastai import *
from fastai.vision import *
from fastbook import load_learner

def predict(image):
    model = load_learner('Model.pkl')
    prediction = model.predict(image)
    return prediction[0]
