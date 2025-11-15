import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load saved model
model = joblib.load("seat_availability_model.pkl")

# Title
st.title("📚 Library Seat Availability Predictor")
st.write("Predict number of seats available in the library at any hour.")

# -----------------------------
# USER INPUTS
# -----------------------------
day = st.selectbox(
    "Select Day of Week:",
    (0, 1, 2, 3, 4, 5, 6),
    format_func=lambda x: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][x]
)

weather = st.selectbox("Weather:", ["cloudy", "rainy", "sunny"])
weather_mapping = {"cloudy": 0, "rainy": 1, "sunny": 2}
weather_encoded = weather_mapping[weather]

exam_day = st.selectbox("Is it an Exam Day?", ["No", "Yes"])
exam_encoded = 1 if exam_day == "Yes" else 0

hour = st.slider("Select Hour (0–23):", 0, 23)

# -----------------------------
# PREDICT BUTTON
# -----------------------------

if st.button("Predict"):
    # ----- Single Hour Prediction -----
    inputs = np.array([[day, hour, exam_encoded, weather_encoded]])

    pred = model.predict(inputs)[0]
    predicted_seats = int(round(pred))
    predicted_seats = max(0, min(250, predicted_seats))
    occupied = 250 - predicted_seats

    # Show results
    st.subheader("📊 Prediction Results")
    st.write(f"**Available Seats:** {predicted_seats}")
    st.write(f"**Occupied Seats:** {occupied}")

    # -----------------------------
    # FULL DAY PREDICTION (24 hours)
    # -----------------------------
    hours = list(range(24))
    predictions = []

    for h in hours:
        inp = np.array([[day, h, exam_encoded, weather_encoded]])
        p = model.predict(inp)[0]
        p = int(round(max(0, min(250, p))))
        predictions.append(p)

    # Build DataFrame for graph
    df = pd.DataFrame({
        "Hour": hours,
        "Available Seats": predictions,
        "Occupied Seats": [250 - x for x in predictions]
    })

    st.subheader("📅 Daily Seat Availability Trend")
    st.line_chart(df.set_index("Hour"))
