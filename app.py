import streamlit as st
from pathlib import Path
import hashlib
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv() 

from PIL import Image


from api_key import api_key

genai.configure(api_key=api_key)

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

system_instruction = """
As a highly skilled food scientist with specializing in image analysis, you are tasked with examining the processed food item and beverage ingredient images which contain the ingredient list and may also include nutritional information and any health claim about the product, understand the ingredients and analyze them. Your expertise is crucial in identifying any harmful ingredient is present in the product as well as in identifying its effects on human body based on the proposition.

Your Responsibilities include:

1. Detailed Analysis: Thoroughly analyze the image, focusing on identifying any harmful findings.
2. Findings Report: Document all observed harmful ingredients and its effect on the body. Clearly articulate these findings in a structured form.
3. Recommendations: Based on your analysis, suggest alternative for the ingredient.

"""
def get_gemini_response(image):
  model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)
  if input!="":
       response = model.generate_content([image])
  else:
       response = model.generate_content(image)
  return response.text

#page configuration
st.set_page_config(page_title="Ingredient Decoder")

#page title
st.title("Ingredient Decoder")
st.subheader("Decode the ingredients before use")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

st.button("Analyze")

if st.button:
    
    response=get_gemini_response(image)
    st.subheader("The Response is")
    st.write(response)





 