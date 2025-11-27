# 🪐 Exoplanet Detection using Deep Learning (NASA Kepler Light Curves)

### 🔭 Real-time AI system to detect exoplanets from telescope data using a 1D-CNN model and Streamlit web app

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![NASA](https://img.shields.io/badge/NASA-Kepler%20Data-black)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-CNN-green)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Project Overview

This project uses **NASA Kepler space telescope light-curve data** to detect whether a star contains an **exoplanet** (a planet outside our solar system).  
A **1D Convolutional Neural Network (1D-CNN)** is trained on time-series flux data and deployed as an interactive **Streamlit web app**.

📌 Upload a 1-row `.csv` file containing star brightness values →  
📌 The app plots the curve and predicts **Exoplanet / No Exoplanet** along with a **probability score**.

---

## 🌌 Why this project is unique

| Feature | Advantage |
|--------|----------|
| Uses real NASA Kepler dataset | Scientifically relevant ML problem |
| 1D-CNN for time-series signals | High accuracy on transit detection |
| Clean Streamlit deployment | Ready for demos / interviews |
| Reproducible code | Entire workflow open-sourced |

---


## 🧠 Model Architecture (1D-CNN)

Input → Conv1D → MaxPool →
Conv1D → MaxPool →
Conv1D → MaxPool →
Flatten →
Dense(128) + Dropout →
Dense(1, activation = sigmoid)


- Loss: `Binary Crossentropy`  
- Optimizer: `Adam`  
- Output: {0 → No Exoplanet, 1 → Exoplanet Candidate}

---

## 📁 Repository Structure
📦 Exoplanet-Detection-using-Deep-Learning
├── exoplanet_app.py ← Streamlit Web App
├── best_model.keras ← Trained 1D-CNN model
├── Exoplanet_Detection_using_Deep_Learning.ipynb ← Training notebook
├── sample_lightcurve.csv ← Example input
├── requirements.txt ← Dependencies
└── README.md


---

## ▶️ Run the Web App Locally

```bash
pip install -r requirements.txt
streamlit run exoplanet_app.py

Then open the generated link:

http://localhost:8501

📥 Input Format (for predictions)

The app expects a .csv file:

Single row

Only numeric flux values

No header

Example:

0.032, 0.031, 0.028, 0.021, 0.019, -0.002, -0.054, -0.049, ...


⚠️ Don't upload the full Kepler dataset — the app only accepts one light curve per file.

🛰 Dataset Information

Dataset: Exoplanet Hunting in Deep Space

Source: NASA Kepler Space Telescope

Format: Time-series flux with ground-truth orbit labels

Dataset Link: https://www.kaggle.com/datasets/keplersmachines/exoplanet-hunting-in-deep-space

💡 Future Improvements

Add Transformers / LSTM for sequence modeling

Support multi-planet systems

Add attention visualization over transit region

Deploy model on mobile using TensorFlow Lite

API endpoint for astronomical observatory pipelines

👤 Author

Ayushman Das
AI & Machine Learning Enthusiast | Space Tech Curious 🚀

📌 If you like this repository, please ⭐ star the project — it helps a lot!


---

## 🔼 STOP COPYING HERE

---

### 📌 Next Step — Update README
1. Open your GitHub repo
2. Click `README.md`
3. Click ✏️ **Edit**
4. Delete everything that is currently inside
5. Paste the **full README above**
6. Click **Commit changes**

Your repository will now look **professional and industry-ready**.

---

## 🔥 Final phase (next)
Once the README is updated, we will:

### 🌍 Deploy your app publicly on Streamlit Cloud
→ So GitHub shows a **Live Demo** button  
→ And you get a public link like:



https://exoplanet-detector.streamlit.app


That link will be **amazing for LinkedIn, resume & portfolio**.

---

### When README is updated, reply:
👉 **README updated — continue deployment**

Then I will guide you to deploy the app step-by-step (2 minutes only). 🚀
