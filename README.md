# Diabetes-prediction-using-Machine-learning-
No worries! Here's a plain text version of the README you can easily copy and paste:

---

# 🩺 Diabetes Prediction Using Machine Learning

This is a web application that predicts whether a person is likely to have diabetes based on several medical parameters. The machine learning model is trained on the Pima Indians Diabetes Dataset.

🚀 **Live Demo**: [https://diabetes-prediction-l69e.onrender.com/](https://diabetes-prediction-l69e.onrender.com/)

---

## 💡 Features

- Predicts diabetes based on user input  
- Built using Python, Flask, and scikit-learn  
- Web UI created using HTML/CSS (Jinja templates)  
- Trained model served using `model.pkl`  
- Hosted live on [Render](https://render.com/)

---

## 📊 Input Parameters

The following health parameters are required:

- Number of Pregnancies  
- Glucose Level  
- Blood Pressure  
- Skin Thickness  
- Insulin Level  
- Body Mass Index (BMI)  
- Diabetes Pedigree Function (DPF)  
- Age  

---

## 🛠️ Tech Stack

- Python 🐍  
- Flask 🌐  
- scikit-learn 📚  
- HTML/CSS 🧑‍🎨  
- Render 🌩️ (Deployment)

---

## 📁 Project Structure

```
.
├── app.py               # Flask application script
├── model.pkl            # Trained machine learning model
├── requirements.txt     # Python dependencies
├── Procfile             # For Render deployment
├── templates/
│   └── index.html       # Web interface
└── README.md            # This file
```

---

## 🔧 Setup Instructions (Local)

1. **Clone the repository**  
   ```
   git clone https://github.com/speranzadeejoe/Diabetes-prediction-using-Machine-learning-.git
   cd Diabetes-prediction-using-Machine-learning-
   ```

2. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

3. **Run the app**  
   ```
   python app.py
   ```

4. Visit `http://127.0.0.1:5000/` in your browser.

---

## 📈 Model Training

This app uses a random forest classifier trained on the Pima Indians Diabetes Dataset, which contains real medical diagnostic measurements for females aged 21 and older.

---

## 🙌 Acknowledgements

- Dataset: [UCI Machine Learning Repository (via Kaggle)](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)  
- Inspired by real-world medical diagnostic prediction challenges.

---

## 📬 Contact

Made with ❤️ by [@speranzadeejoe](https://github.com/speranzadeejoe)

If you found this project helpful, feel free to ⭐ star the repo!

---
