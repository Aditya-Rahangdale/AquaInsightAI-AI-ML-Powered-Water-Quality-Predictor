# AquaInsightAI-AI-ML-Powered-Water-Quality-Predictor
AquaInsightAI is an AI-powered web app that predicts water quality by analyzing key parameters, providing fast, accurate assessments to ensure safe drinking water using a machine learning model.

#**Technical Details**
Front-End: HTML, CSS, JavaScript
Back-End: Flask framework
ML Model: RandomForestClassifier
Model Training: Python, scikit-learn
Data Input: pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, turbidity
Prediction Process: Input data converted to NumPy array and passed to the model
Result Handling: Redirects to specific pages based on prediction (0 or 1)
Deployment: Local servers or cloud platforms

**Demo Video**
https://github.com/Aditya-Rahangdale/AquaInsightAI-AI-ML-Powered-Water-Quality-Predictor/assets/112549645/0980f8cf-757f-4f35-abeb-3c8ce6f12497

**userInterface**
![Screenshot (306)](https://github.com/Aditya-Rahangdale/AquaInsightAI-AI-ML-Powered-Water-Quality-Predictor/assets/112549645/ba146124-542e-4e3d-9c61-24a6f8cae8f6)

**output Potable water **
![Screenshot (304)](https://github.com/Aditya-Rahangdale/AquaInsightAI-AI-ML-Powered-Water-Quality-Predictor/assets/112549645/6d953792-c400-4296-9a77-eea2a5e4f453)

**output Not Potable Water**
![Screenshot (305)](https://github.com/Aditya-Rahangdale/AquaInsightAI-AI-ML-Powered-Water-Quality-Predictor/assets/112549645/23884aaa-a6f9-4453-b174-beb0af718557)


AquaInsightAI/
├── app/
│   ├── app.py
│   
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── images/
│   │       └── background.jpg
│   ├── templates/
│   │   ├── index.html
│   │   ├── page0.html
│   │   └── page1.html
├── model/
│   ├── model.pkl
├── scripts/
│   ├── train_model.py
├── .gitignore
├── requirements.txt
└── run.py
