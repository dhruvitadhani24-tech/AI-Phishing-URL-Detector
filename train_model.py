import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

def extract_features(url):
    features = []
    features.append(len(url))                     
    features.append(url.count('@'))               
    features.append(url.count('-'))               
    features.append(url.count('.'))               
    features.append(1 if 'http://' in url else 0) 
    return features

data = {
    'url': [
        'https://www.google.com', 
        'http://secure-login-update.xyz', 
        'https://www.github.com', 
        'http://192.168.5.5/admin-login-bank',
        'https://www.amazon.in'
    ],
    'label': [0, 1, 0, 1, 0] 
}
df = pd.DataFrame(data)

print("Extracting features and training model...")

X = df['url'].apply(lambda x: pd.Series(extract_features(x)))
y = df['label']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

with open('phishing_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("✅ Model Trained and Saved Successfully as 'phishing_model.pkl'!")