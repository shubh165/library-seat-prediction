# library-seat-prediction
# 📚 Library Seat Availability Prediction  
### Machine Learning Project | Streamlit Web App | Aug–Nov 2025 Dataset (College - NIT Kurukshetra)

👉 **Live App:** https://library-seat-prediction.streamlit.app/  
👉 **Dataset:** Aug 15 – Nov 10 (Hourly data – Weather, Gender Count, Exam Days)

---

## 📌 Project Overview
This project predicts **seat availability in a NIT Kurukshetra college library** based on:

- Day of the week  
- Hour of the day  
- Weather conditions  
- Exam day or not  
- Boys count  
- Girls count  

The model helps students know the **best time to visit the library** and plan study hours effectively.

A **Random Forest Regression model** was trained on a realistic dataset covering **4 months (Aug–Nov)** with **hourly data**.

---

## 🎯 Objective  
To build a machine-learning model and a Streamlit-based web application that predicts:

- **Available seats**  
- **Occupied seats**  
- **Daily seat availability trend graph**

---

## 🧠 Machine Learning Workflow

### **1️⃣ Data Preparation (EDA & Cleaning)**  
- Converted date to datetime  
- Encoded weather using Label Encoding  
- Created useful features  
  - Day of week  
  - Hour  
  - Exam day flag  
- Verified missing values (none found)  
- Split dataset for training/testing

### **2️⃣ Modeling**  
Three models were tested:

| Model | MAE ↓ | RMSE ↓ | R² ↑ |
|-------|--------|---------|--------|
| Linear Regression | 34.33 | 42.84 | 0.13 |
| Decision Tree | 14.19 | 19.31 | 0.82 |
| **Random Forest** (Best) | **13.72** | **18.29** | **0.84** |

👉 **Random Forest** performed the best and was chosen for final deployment.

### **3️⃣ Deployment**  
The model was deployed using:

- 🐍 Python 3.11  
- 🌐 Streamlit Cloud  
- 📦 joblib for model saving  
- GitHub for hosting source code

---

## 🚀 Features of the Live App

### ✔ Predict seat availability  
Based on:
- Day  
- Hour  
- Weather  
- Exam day  

### ✔ Shows both:  
- **Available Seats**  
- **Occupied Seats**  

### ✔ Trend Graph (24-hour prediction)  
Beautiful Altair graph showing:
- Hour-wise available seats  
- Hour-wise occupied seats  

### ✔ Clean and modern UI  
Built using Streamlit with a well-designed interface.

---

## 📂 Project Structure
library-seat-prediction/
- │
- ├── APP.py                     # Streamlit web application
- ├── EDA.ipynb                  # Data exploration & preprocessing notebook
- ├── library_dataset.csv        # Final dataset used for model training
- ├── seat_availability_model.pkl # Trained Random Forest model
- ├── requirements.txt           # Python dependencies
- └── README.md                  # Project documentation



---

## ⚙️ Installation (Local Setup)

### 1. Clone the repository:
```bash
git clone https://github.com/shubh165/library-seat-prediction.git
cd library-seat-prediction
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the app:
```bash
streamlit run APP.py
```

