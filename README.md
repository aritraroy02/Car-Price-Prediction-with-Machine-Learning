
# 🚗 Car Price Prediction with Machine Learning

This project predicts the selling price of used cars based on features like present price, mileage, fuel type, transmission, and more using machine learning models.

## 📂 Project Structure

```
car-price-prediction/
│
├── data/
│   └── car data.csv
│
├── notebooks/
│   └── Car_Price_Prediction.ipynb
│
├── app/
│   └── model.pkl  # Trained ML model
│
├── README.md
└── requirements.txt
```

## 🛠 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Random Forest Regressor
- Jupyter Notebook
- Joblib

## 📊 Features Used
- Present Price
- Driven Kms
- Owner
- Fuel Type
- Transmission
- Selling Type
- Car Age (Derived from Year)

## ✅ Steps Performed
1. Data Cleaning and Preprocessing
2. Feature Engineering
3. Encoding Categorical Features
4. Training a Random Forest Regressor
5. Evaluating the model using R² Score and RMSE
6. Saving the model with `joblib`

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/aritraroy02/car-price-prediction-with-machine-learning.git
   cd car-price-prediction-with-machine-learning
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the notebook:
   ```bash
   jupyter notebook notebooks/Car_Price_Prediction.ipynb
   ```

## 📌 Future Enhancements
- Add a web interface using Streamlit
- Hyperparameter tuning with GridSearchCV
- Deploy the model online

## 🙌 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
