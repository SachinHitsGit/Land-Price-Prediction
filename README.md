## Land Price Prediction

This is a Flask web application that predicts land prices per square foot using a pre-trained linear regression model
Users can input land features to get a price prediction
The app also displays model evaluation metrics and residual plots

---

Features

- Predict land price per square foot based on the following inputs
- Area in square feet
- Road width in feet
- Distance to the nearest landmark in kilometers
- Location as one of the following Downtown Suburb Urban Rural

Model performance metrics include R squared Mean Squared Error Root Mean Squared Error and Mean Absolute Error
Residuals are visualized using a scatter plot and a histogram

---

## Model

- The model used is a Linear Regression model saved as land\_price\_model.pkl
- The target variable is Price\_per\_SqFt\_USD
- The input features are
- Area\_SqFt ranging from 2000 to 15000
- Road\_Width\_Ft ranging from 10 to 50
- Distance\_to\_Landmark\_Km ranging from 0.5 to 15
- Location encoded as Downtown Suburb Urban or Rural using one hot encoding

---

## Evaluation on Test Data

- R squared is 0.8354
- Mean Squared Error is 620.33
- Root Mean Squared Error is 24.91
- Mean Absolute Error is 19.07

---

## Example Input

- Area 5000
- Road Width 30
- Distance to Landmark 2.5
- Location Downtown
- Predicted price is approximately 230 dollars per square foot

---

## How to Run

- Clone the repository using git clone [https://github.com/SachinHitsGit/Land-Price-Prediction.git](https://github.com/SachinHitsGit/Land-Price-Prediction.git)
- Navigate into the project folder
- Install the required dependencies using pip install -r requirements.txt
- Run the application using python app.py
- Open your web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000) for prediction
- Visit [http://127.0.0.1:5000/evaluate](http://127.0.0.1:5000/evaluate) to view model evaluation metrics and residual plots

---

## Notes

- The .gitignore file excludes the virtual environment model files and static plot files
- This model was trained on specific data and may need retraining for use with real world data

---

## Future Improvements

- Use real world datasets for training
- Add interactive and dynamic plots
- Deploy the application to a production environment

---

## Author

### Sachin
- GitHub profile [https://github.com/SachinHitsGit](https://github.com/SachinHitsGit)
- Project repository [https://github.com/SachinHitsGit/Land-Price-Prediction](https://github.com/SachinHitsGit/Land-Price-Prediction)
