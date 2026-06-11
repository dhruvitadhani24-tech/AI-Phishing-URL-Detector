import streamlit as st
import pickle

try:
    with open('phishing_model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Error: Model file not found. Please run 'train_model.py' first.")
    st.stop()

def extract_features(url):
    return [
        len(url), 
        url.count('@'), 
        url.count('-'), 
        url.count('.'), 
        1 if 'http://' in url else 0
    ]

st.set_page_config(page_title="Phishing URL Detector", page_icon="🛡️")

st.title("🛡️ AI-Powered Phishing URL Detector")
st.markdown("**Created for 5th Sem Cybersecurity Internship Project**")
st.write("નીચે કોઈ પણ લિંક (URL) નાખો અને ચેક કરો કે તે સુરક્ષિત છે કે હેકર્સની ફિશિંગ લિંક છે.")

url_input = st.text_input("Enter the URL here (e.g., http://example.com):")

if st.button("🔍 Check Security"):
    if url_input:
        features = extract_features(url_input)
        prediction = model.predict([features])[0]
        
        st.markdown("---")
        if prediction == 1:
            st.error("🚨 **WARNING:** This looks like a Phishing or Malicious URL! Do not click or share your details.")
        else:
            st.success("✅ **SAFE:** This URL appears to be legitimate and safe.")
    else:
        st.warning("Please enter a URL to check.")