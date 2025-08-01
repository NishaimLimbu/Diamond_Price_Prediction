import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("Diamond_price_prediction.pkl")

# Mappings for categorical variables
cut_mapping = {"Fair": 0, "Good": 1, "Very Good": 2, "Premium": 3, "Ideal": 4}
color_mapping = {'J': 0, 'I': 1, 'H': 2, 'G': 3, 'F': 4, 'E': 5, 'D': 6}
clarity_mapping = {'I1': 0, 'SI2': 1, 'SI1': 2, 'VS2': 3, 'VS1': 4, 'VVS2': 5, 'VVS1': 6, 'IF': 7}

# UI
st.title("Diamond Price Prediction 💎")

Carat = st.number_input("How much **carat** Diamond💎 do you want?", min_value=0.15, max_value=6.0, step=0.01)

Cut = st.selectbox("Select the **cut** quality of the diamond.", list(cut_mapping.keys()))
st.write(f"Your Choice: **{Cut}**")

Color = st.selectbox("Select the **color** of the diamond.", list(color_mapping.keys()))
st.write(f"Your Choice: **{Color}**")

Clarity = st.selectbox("Select the **clarity** of the diamond.", list(clarity_mapping.keys()))
st.write(f"Your Choice: **{Clarity}**")

Depth = st.number_input("Enter the **Depth** of the diamond (in %).", min_value=40.0, max_value=100.0, step=0.01)
Table = st.number_input("Enter the **Table** of the diamond (in %).", min_value=40.0, max_value=100.0, step=0.01)
X = st.number_input("Enter the **X** of the diamond (in mm).", min_value=0.0, max_value=12.0, step=0.01)
Y = st.number_input("Enter the **Y** of the diamond (in mm).", min_value=0.0, max_value=60.0, step=0.01)
Z = st.number_input("Enter the **Z** of the diamond (in mm).", min_value=0.0, max_value=35.0, step=0.01)

# Encode categorical values
cut_encoded = cut_mapping[Cut]
color_encoded = color_mapping[Color]
clarity_encoded = clarity_mapping[Clarity]

# Prepare input
input_data = np.array([[Carat, cut_encoded, color_encoded, clarity_encoded, Depth, Table, X, Y, Z]])

# Prediction
if st.button("Predict the Price of Diamond"):
    prediction = model.predict(input_data)
    st.success(f"💰 Predicted Diamond Price: ${round(prediction[0], 2)}")
else:
    st.info("🔍 Click the button to predict after filling the inputs.")
