import streamlit as st
import google.generativeai as genai
# Initialize Google Cloud Language client
# Function to generate a complaint letter using Google Generative AI
genai.configure(api_key="YOUR_API_KEY")
def generate_complaint_letter(details):
    prompt = f"Write a formal police complaint letter based on the following details:\n{details}"
    
    # Assuming Google Generative AI client has a similar interface
    
     
   
    model = genai.GenerativeModel("AIzaSyDNcp_JDchji_PfU6mKwjCz2SxGBj0a4Ow")
    generated_text = model.generate_content(prompt)

    # Here, you'd use the appropriate API call for text generation.
    # The line below is a placeholder for the actual generative AI function.
   # Modify as per actual API response structure
    
    return generated_text

# Streamlit UI
st.title("AI Police Complaint Letter Generator (Google Generative AI)")

st.subheader("Enter the details of your complaint:")
details = st.text_area("Describe the incident here (include what happened, when, where, and who was involved):")

if st.button("Generate Complaint Letter"):
    if details:
        with st.spinner('Generating your complaint letter...'):
          letter = generate_complaint_letter(details)
          st.subheader("Generated Complaint Letter:")
          st.text_area("Complaint Letter", value=letter, height=300)
    else:
        st.warning("Please enter the details of your complaint.")
