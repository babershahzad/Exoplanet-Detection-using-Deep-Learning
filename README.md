# 🔭 Exoplanet Detection using Deep Learning (NASA Kepler Light Curves)

[![Streamlit App](https://img.shields.io/badge/🔭_Live_App-Streamlit-green?style=for-the-badge)](https://exoplanet-detection-using-deep-learning-hedt5bhak5gus223xxrcat.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/📂_Source_Code-GitHub-blue?style=for-the-badge)](https://github.com/ayushmandas29/Exoplanet-Detection-using-Deep-Learning)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Streamlit](https://img.shields.io/badge/Web_App-Streamlit-red)
![NASA](https://img.shields.io/badge/Data-NASA_Kepler-black)
![Deep Learning](https://img.shields.io/badge/Model-1D_CNN-green)

---

## 🌌 Background — What is an Exoplanet?
An **exoplanet** is a planet located **outside our solar system**.  
We cannot directly photograph most of them — they are too far and too dim compared to their host stars.

Astronomers use the **Transit Method**:
> When a planet passes in front of its star, the star’s brightness dips slightly.  
> This repeating dip pattern (light curve) indicates the presence of an exoplanet.

This project automates the detection of these light-curve patterns using **Deep Learning**.

---

## 🚀 Project Overview
This system analyzes **NASA Kepler light-curve time-series data** and predicts whether a star has an orbiting exoplanet.

| Output | Meaning |
|--------|---------|
| 🌍 **1** | Exoplanet candidate detected |
| ✖️ **0** | No exoplanet detected |

A **1D Convolutional Neural Network (CNN)** is trained and deployed as an interactive **Streamlit web application**.

🔗 **Live Demo:**  
https://exoplanet-detection-using-deep-learning-hedt5bhak5gus223xxrcat.streamlit.app/

---

## 📂 Dataset
NASA Kepler dataset: **Exoplanet Hunting in Deep Space**  
Contains:
- Confirmed or likely exoplanet transit samples
- Non-transit light curves
- ~3198 flux values per sample

Kaggle Source:  
https://www.kaggle.com/datasets/keplersmachines/exoplanet-hunting-in-deep-space

---

## 🧠 Model Architecture
Input (3198 flux values)
→ Conv1D → MaxPool
→ Conv1D → MaxPool
→ Conv1D → MaxPool
→ Flatten
→ Dense(128) + Dropout(0.5)
→ Dense(1, Activation = Sigmoid)


### 🏆 Performance
| Metric | Score |
|--------|-------|
| Training Accuracy | ~99.6% |
| Validation Accuracy | ~99.5% |

---

## 🛠 Tech Stack
| Component | Technology |
|----------|-------------|
| Language | Python |
| Deep Learning | TensorFlow / Keras |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib |
| Deployment | Streamlit Cloud |

---

## 📁 Repository Structure
📦 Exoplanet-Detection-using-Deep-Learning
┣ 📄 Exoplanet_Detection_using_Deep_Learning.ipynb (model training)
┣ 📄 best_model.keras (trained model)
┣ 📄 exoplanet_app.py (Streamlit app)
┣ 📄 sample_lightcurve.csv (example input)
┣ 📄 requirements.txt (dependencies)
┗ 📄 README.md


---

## ▶️ Run Locally (Optional)
```bash
git clone https://github.com/ayushmandas29/Exoplanet-Detection-using-Deep-Learning.git
cd Exoplanet-Detection-using-Deep-Learning
pip install -r requirements.txt
streamlit run exoplanet_app.py

📥 Input Format for Prediction
To use the web app:
1. Upload a .csv file containing one row only
2. All values should be numeric flux values
3. No header and no label column

Example:
0.021, 0.018, 0.012, -0.005, -0.053, -0.049, ...

🔧 Future Enhancements:
. Explainability via Grad-CAM on 1D signals
. Support batch upload for multiple stars
. Regression model for transit depth and duration estimation
. FastAPI endpoint for production API inference
. Deploy to mobile edge devices using TFLite

👤 Author
Ayushman Das
AI & Machine Learning Enthusiast — Space Science & Research Lover 🚀
📧 Email: ayushmandas736@gmail.com
🔗 GitHub: https://github.com/ayushmandas29

⭐ If this project helped you or inspired you, please consider giving the repository a star — your support motivates further improvements!
