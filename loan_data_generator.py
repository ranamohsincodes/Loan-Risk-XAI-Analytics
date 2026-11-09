import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

print("⏳ Ingesting simulated Loan Risk Records matching paper parameters...")
np.random.seed(42)
records = 1500

cities = ['Karachi', 'Lahore', 'Islamabad', 'Rawalpindi', 'Faisalabad', 'Multan']
employment_types = ['Salaried Individual', 'Self-Employed Professional', 'Business Owner', 'Unemployed/Freelance']
loan_purposes = ['Debt Consolidation', 'Home Renovation', 'Small Business Expansion', 'Educational Loan']
model_prediction_status = ['Low Risk', 'Medium Risk', 'High Risk']

data = []
for i in range(records):
    city = random.choice(cities)
    emp = random.choice(employment_types)
    purpose = random.choice(loan_purposes)
    
    monthly_income = random.randint(45000, 350000)
    loan_amount = random.randint(100000, 2500000)
    dti_ratio = round((random.randint(15000, 120000) / monthly_income) * 100, 2)
    pred_risk = np.random.choice(model_prediction_status, p=[0.6, 0.25, 0.15])
    
    if pred_risk == 'High Risk' or dti_ratio > 50:
        actual_default = np.random.choice(['Defaulted', 'Performing'], p=[0.7, 0.3])
    else:
        actual_default = np.random.choice(['Defaulted', 'Performing'], p=[0.1, 0.9])
        
    top_feature_impact = random.choice(['Debt-to-Income Ratio', 'Income Variance', 'Employment Duration', 'Prior Credit History'])

    data.append({
        'Application_ID': f'APP-{800000 + i}',
        'City': city,
        'Employment_Type': emp,
        'Loan_Purpose': purpose,
        'Monthly_Income_PKR': monthly_income,
        'Requested_Amount_PKR': loan_amount,
        'Debt_to_Income_Percent': dti_ratio,
        'Model_Risk_Tier': pred_risk,
        'Final_Loan_Status': actual_default,
        'Top_SHAP_Feature_Driver': top_feature_impact
    })

df = pd.DataFrame(data)
df.to_csv('loan_risk_telemetry.csv', index=False)
print("✅ Dataset generated successfully: 'loan_risk_telemetry.csv' with risk attributions.")
