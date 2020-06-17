from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer 
import re

app = Flask(__name__)

model = None

def load_model():
    global model

    with open('nb_trained_model.pickle', 'rb') as f:
        model = pickle.load(f)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict", methods=["POST"])
def predict():
    cv = pickle.load(open("vectorizer.pickle", 'rb'))
    if request.method == "POST":
        text = request.form.get('article')
        text = re.sub(r"\r\n", "", text)
        # print(text)
        # clean_text = text.strip() 
        data = [text]
        # data = {"story": [text]}
        # response = jsonify(data)
        vect = cv.transform(data)
        prediction = model.predict(vect)
        return "Fake News Story" if prediction[0] else "Real News Story"
        # return str(prediction[0])

if __name__ == "__main__":
    load_model()
    app.run(debug=True, host="0.0.0.0", port="80")