from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")  # Automatically looks in the 'templates/' folder

@app.route("/predict", methods=["POST"])
def predict():
    values = [float(x) for x in request.form.values()]
    features = np.array(values).reshape(1, -1)
    prediction = model.predict(features)[0]
    result = "Diabetic" if prediction == 1 else "Not Diabetic"
    return f"<h1>Prediction Result: {result}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
