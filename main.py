from flask import Flask, render_template, request
import pickle
import numpy as np

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
    if request.method == "POST":
        data = request.get_json()
        print(data.size)
    return "placeholder"

if __name__ == "__main__":
    load_model()
    app.run(debug=True)