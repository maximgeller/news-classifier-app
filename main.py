from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer 

app = Flask(__name__)

model = None

def load_model():
    global model

    with open('nb_trained_model.pkl', 'rb') as f:
        model = pickle.load(f)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
   #  cv = CountVectorizer()
    if request.method == "POST":
        text = request.form['article']
        data = {"story": [text]}
        response = jsonify(data)
        # vect = cv.transform(data)
        # prediction = model.predict(vect)
        return response

if __name__ == "__main__":
    load_model()
    app.run(debug=True)