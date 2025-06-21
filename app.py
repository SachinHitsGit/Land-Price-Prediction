import flask
import pandas as pd
import joblib

app = flask.Flask(__name__)

try:
    model = joblib.load('land_price_model.pkl')
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

def predict_land_price(area_sqft, road_width_ft, distance_to_landmark_km, location):
    try:
        area_sqft = float(area_sqft)
        road_width_ft = float(road_width_ft)
        distance_to_landmark_km = float(distance_to_landmark_km)
        
        if location not in ['Downtown', 'Suburb', 'Urban', 'Rural']:
            raise ValueError("Location must be one of: Downtown, Suburb, Urban, Rural")

        if not (100 <= area_sqft <= 50000):  
            raise ValueError("Area must be between 100 and 50,000 sq ft")
        if not (5 <= road_width_ft <= 100):  
            raise ValueError("Road Width must be between 5 and 100 ft")
        if not (0.1 <= distance_to_landmark_km <= 50):  
            raise ValueError("Distance to Landmark must be between 0.1 and 50 km")
            
    except ValueError as e:
        return None, str(e)
    
    if model is None:
        return None, "Model not loaded. Please check if 'land_price_model.pkl' exists."
    
    try:
        input_data = pd.DataFrame({
            'Area_SqFt': [area_sqft],
            'Road_Width_Ft': [road_width_ft],
            'Distance_to_Landmark_Km': [distance_to_landmark_km],
            'Location': [location]
        })
        
        input_encoded = pd.get_dummies(input_data, columns=['Location'], prefix='Location')
        
        for col in ['Location_Downtown', 'Location_Rural', 'Location_Suburb', 'Location_Urban']:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        
        input_features = input_encoded[['Area_SqFt', 'Road_Width_Ft', 'Distance_to_Landmark_Km', 
                                       'Location_Downtown', 'Location_Rural', 'Location_Suburb', 'Location_Urban']]
        
        prediction = model.predict(input_features)[0]
        return round(prediction, 2), None
        
    except Exception as e:
        return None, f"Prediction error: {str(e)}"

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        area = flask.request.form.get('area', '').strip()
        road_width = flask.request.form.get('road_width', '').strip()
        distance = flask.request.form.get('distance', '').strip()
        location = flask.request.form.get('location', '').strip()
        
        if not all([area, road_width, distance, location]):
            return flask.render_template('index.html', error="Please fill in all fields")
        
        prediction, error = predict_land_price(area, road_width, distance, location)
        

        if error:
            return flask.render_template('index.html', error=error)
        

        total_value = prediction * float(area)
        
        return flask.render_template('index.html', 
                                   prediction=prediction, 
                                   total_value=total_value,
                                   area=area)
    
    except Exception as e:
        return flask.render_template('index.html', error=f"An unexpected error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)