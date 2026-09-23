import streamlit as st
import requests

st.set_page_config(page_title="Model Inference Dashboard", layout="centered")

st.title("🤖 ML Model Serving Dashboard")
st.write("Interface for interacting with the FastAPI Model Endpoint.")

API_URL = "http://127.0.0.1:8000/predict"

input_str = st.text_input("Enter comma-separated features (e.g., 1.0, 2.5, 3.8):", "1.0, 2.0, 3.0")

if st.button("Run Inference"):
    try:
        features = [float(x.strip()) for x in input_str.split(",") if x.strip()]
        
        response = requests.post(API_URL, json={"features": features})
        
        if response.status_code == 200:
            result = response.json()
            st.success("Inference Successful!")
            st.json(result)
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
    except ValueError:
        st.error("Please enter valid numerical values.")
    except Exception as e:
        st.error(f"Could not connect to API: {e}")