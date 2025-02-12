import streamlit as st
import pandas as pd
import requests
import lightgbm as lgb
import pickle
import os

# header = st.container()
# raw_url = "https://github.com/AJFarthing/field-scout/raw/main/lgb_model.pkl"
# model_path = "lgb_model.pkl"

# # Check if the model file exists locally
# if not os.path.exists(model_path):
#     # Fetch the model from GitHub if it doesn't exist locally
#     response = requests.get(raw_url, stream=True)
#     if response.status_code == 200:
#         with open(model_path, "wb") as f:
#             f.write(response.content)
#     else:
#         st.error("Failed to fetch the pickle file from GitHub.")
# else:
#     st.text("Model file already exists locally.")

# # Load the model
# try:
#     with open(model_path, "rb") as f:
#         load_clf = pickle.load(f)
# except Exception as e:
#     st.error(f"Error loading model: {e}")

# header = st.container()

# with header:
#     st.title('CropSense: A Smart Crop Advisor')
#     st.text('This app was created to work as a gardening assistant.')
#     st.text('With the crop recommendation system, all the guess work is taken out of gardening.')
#     st.text('Simply enter readings from your own garden into the User Input Sidebar')
#     st.text('and we will suggest the crop best suited to these conditions')

# st.sidebar.header('User Input Sidebar')

# # Function to collect user inputs
# def user_input_features():
#     Nitrogen = st.sidebar.number_input('Input your Nitrogen reading here (0-150)', value=0, min_value=0, max_value=150, step=1, format='%d')
#     Phosphorus = st.sidebar.number_input('Input your Phosphorus reading here (0-150)', value=0, min_value=0, max_value=150, step=1, format='%d')
#     Potassium = st.sidebar.number_input('Input your Potassium reading here (0-210)', value=0, min_value=0, max_value=210, step=1, format='%d')
#     Temperature = st.sidebar.number_input('Input your Temperature reading here (0-50)', value=0.0, min_value=0.0, max_value=50.0, step=0.1, format="%.1f")
#     Humidity = st.sidebar.number_input('Input your Humidity reading here (0-100)', value=0, min_value=0, max_value=100, step=1, format='%d')
#     PH = st.sidebar.number_input('Input your PH reading here (0-14)', value=0.0, min_value=0.0, max_value=14.0, step=0.1, format="%.1f")
#     Rainfall = st.sidebar.number_input('Input your Rainfall reading here (0-400)', value=0, min_value=0, max_value=400, step=1, format='%d')

#     data = {'Nitrogen': Nitrogen,
#             'Phosphorus': Phosphorus,
#             'Potassium': Potassium,
#             'Temperature': Temperature,
#             'Humidity': Humidity,
#             'PH': PH,
#             'Rainfall': Rainfall
#             }
#     features = pd.DataFrame(data, index=[0])
#     return features

# # Collecting input data from the user
# input_df = user_input_features()
# st.write(input_df)

# # Predict using the loaded model
# try:
#     prediction = load_clf.predict(input_df)[0]

#     st.subheader('Prediction')
#     st.write(f"Based on the inputs provided, the best crop for your parameters would be: <br><b style='font-size: 50px'>{prediction}</b>", unsafe_allow_html=True)

# except Exception as e:
#     st.error(f"Prediction failed: {e}")
