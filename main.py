from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer 

app = Flask(__name__)

model = None
cv = CountVectorizer()

def load_model():
    global model

    with open('nb_trained_model.pkl', 'rb') as f:
        model = pickle.load(f)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        data = request.get_json()
        data = np.reshape(data, (-1, 1))
        data = cv.transform(data)
        prediction = model.predict([data])
        # message = request.form['article']
        # data = [message]
        # vect = cv.transform(data).toarray()
        # my_prediction = clf.predict(vect)
        return str(prediction[0])

if __name__ == "__main__":
    load_model()
    app.run(debug=True)