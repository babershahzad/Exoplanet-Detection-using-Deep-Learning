import numpy as np
import pandas as pd
import streamlit as st
from tensorflow.keras.models import load_model

MODEL_PATH = "best_model.keras"

@st.cache_resource
def load_exoplanet_model():
    return load_model(MODEL_PATH)

def preprocess_lightcurve(arr: np.ndarray) -> np.ndarray:
    # normalize: (x - mean) / std
    mean = arr.mean()
    std = arr.std() + 1e-6
    arr = (arr - mean) / std
    return arr.reshape(1, -1, 1)   # (1, timesteps, 1)

st.title("🔭 Exoplanet Detector – NASA Kepler Light Curves")
st.write("Upload a CSV file containing **one row** of flux values (no label).")

uploaded = st.file_uploader("Upload light-curve CSV", type=["csv"])

if uploaded is not None:
    df = pd.read_csv(uploaded, header=None)
    lc = df.values.flatten().astype("float32")

    st.subheader("Light Curve")
    st.line_chart(lc)

    x = preprocess_lightcurve(lc)
    model = load_exoplanet_model()

    prob = float(model.predict(x)[0][0])
    pred = "🟢 Exoplanet Candidate" if prob > 0.5 else "🔴 No Exoplanet"

    st.subheader("Result")
    st.write(f"**Prediction:** {pred}")
    st.write(f"**Probability score:** `{prob:.4f}`")
