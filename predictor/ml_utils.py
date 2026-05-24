import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(BASE_DIR, 'xgboost_model.joblib'))
scaler = joblib.load(os.path.join(BASE_DIR, 'scaler.joblib'))

def predict_score(gpa, attendance, study_hours, assignments_done, previous_prep):
    input_data = pd.DataFrame([{
        'GPA_previous': float(gpa),
        'attendance': int(attendance),
        'study_hours': float(study_hours),
        'assignments_done': int(assignments_done),
        'previous_prep': int(previous_prep)
    }])
    
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    
    # Простой сдвиг вниз (подбираем, чтобы средний стал ~3.6)
    calibrated = prediction - 0.5
    
    calibrated = max(2.0, min(5.0, calibrated))
    return round(calibrated, 2)