from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer 
import re

app = Flask(__name__)

model = None
cv = None

def load_model():
    # load in our model and article vectorizer from pickle files
    global model
    global cv

    model = pickle.load(open('nb_trained_model.pickle', 'rb'))
    cv = pickle.load(open("vectorizer.pickle", 'rb'))

@app.route("/")
def home():
    return render_template("home.html") # render_template is used to load html files

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict", methods=["POST"]) # we need the post method because we call the model to make a prediction
def predict():
    if request.method == "POST":
        text = request.form.get('article') # retrieves the text inside the form with name "article"
        text = re.sub(r"\r\n", "", text) # clean up newline & return char.
        data = [text] # we need to enclose it in a vector for the model
        vect = cv.transform(data) # vectorize the article
        prediction = model.predict(vect) # predict!
        return render_template("predict.html", fake = prediction[0]) # 1: fake; 0: real
       #  return "Fake News Story" if prediction[0] else "Real News Story" # 1: fake; 0: real

if __name__ == "__main__":
    load_model() # load in the model when app runs
    app.run(debug=True, host="0.0.0.0", port="80") # run on port 80 because of AWS/HTTP