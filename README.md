Land Price Prediction
A Flask web application to predict land prices per square foot using a pre-trained linear regression model. The app allows users to input land features and view predictions, along with model evaluation metrics and residual visualizations.
Features

Prediction: Enter Area_SqFt, Road_Width_Ft, Distance_to_Landmark_Km, and Location (Downtown, Suburb, Urban, Rural) to predict Price_per_SqFt_USD.
Evaluation: Displays R-squared (0.8354), MSE (620.3293), RMSE (24.9064), MAE (19.0681), and residual plots (scatter, histogram).
Model: Linear regression, saved as land_price_model.pkl.

Project Structure
Land-Price-Prediction/
├── app.py                    # Flask app for prediction and evaluation
├── evaluate_land_price_model.py  # Script for model evaluation
├── templates/
│   ├── index.html            # Form for predictions
│   └── evaluate.html         # Model metrics and residual plots
├── land_price_model.pkl      # Pre-trained model
├── requirements.txt          # Dependencies
├── static/                   # Residual plot images
└── README.md

Setup

Clone the Repository:
git clone https://github.com/SachinHitsGit/Land-Price-Prediction.git
cd Land-Price-Prediction


Create Virtual Environment:
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows


Install Dependencies:
pip install -r requirements.txt


Run the App:
python app.py


Access at http://127.0.0.1:5000 for predictions.
Visit http://127.0.0.1:5000/evaluate for model evaluation.



Usage

Prediction:
Enter land details in the form (e.g., Area=5000, Road Width=30, Distance=2.5, Location=Downtown).
View predicted Price_per_SqFt_USD (e.g., ~$230).


Evaluation:
Check metrics and residual plots to assess model performance.
Metrics: R²=0.8354, MSE=620.3293, RMSE=24.9064, MAE=19.0681.



Dependencies

Python 3.8+
Flask, pandas, numpy, scikit-learn, joblib, seaborn, matplotlib (see requirements.txt)

Model Details

Features: Area_SqFt, Road_Width_Ft, Distance_to_Landmark_Km, Location (one-hot encoded).
Target: Price_per_SqFt_USD.
Performance: Strong fit (R²=0.8354), with average errors ~19–25 USD.

Notes

.gitignore: Excludes .venv/, *.pkl, static/.
Limitations: Model trained on specific data; real-world data may require retraining.
Future Work: Add interactive plots, support real datasets, deploy with Gunicorn.

Author

Sachin (SachinHitsGit)

