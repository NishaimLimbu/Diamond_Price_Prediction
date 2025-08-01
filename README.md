# 💎 Diamond Price Prediction Project

This project predicts the price of diamonds based on their characteristics using machine learning. It consists of two main components:

- 📘 `Diamond_Price_Prediction.ipynb` – Jupyter Notebook for data preprocessing, training, evaluation, and visualization.
- 🚀 `Diamond_price_prediction.py` – Streamlit app to run the trained model in an interactive web interface.

---

## 📁 Project Structure
Diamond_Price_Prediction/
├── Diamond_price_prediction.py # Streamlit app for predicting diamond prices
├── Diamond_Price_Prediction.ipynb # Jupyter Notebook for data cleaning, training, and evaluation
├── diamonds.csv # Dataset used for training
└── README.md # Project documentation

## 📊 Project Workflow

### 🔬 Jupyter Notebook (`Diamond_Price_Prediction.ipynb`)
- Load and explore the dataset (`diamonds.csv`)
- Data cleaning and preprocessing (encoding, scaling, etc.)
- Visualizations using **Seaborn** and **Matplotlib**
- Train/test split
- Train the model using **RandomForestRegressor**
- Evaluate model performance using:
  - R² Score
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
- Save the trained model using `joblib`

### 🌐 Streamlit App (`Diamond_price_prediction.py`)
- Load the trained model
- Provide a user interface to:
  - Input diamond features (carat, cut, color, clarity, dimensions, etc.)
  - Predict the diamond's price
- Built with **Streamlit** for live web-based prediction

---

## 🧰 Installation & Setup

### 📦 Install Required Packages

Use the following command to install all necessary packages:
**pip install scikit-learn joblib numpy pandas matplotlib seaborn streamlit**

**🚀 Run the Streamlit App**
streamlit run Diamond_price_prediction.py

# 🧠 Technologies Used
1.Python 3
2.Scikit-learn
3.Joblib
4.Pandas
5.NumPy
6.Matplotlib
7.Seaborn
8.Streamlit
9.Jupyter Notebook

# 📈 Sample Dataset
The project uses the diamonds.csv dataset, which includes features like:
1.Carat
2.Cut
3.Color
4.Clarity
5.Depth
6.Table
7.Dimensions (X, Y, Z)
8.Price

#📜 License
This project is licensed under the MIT License.
Built for educational and demonstration purposes.
