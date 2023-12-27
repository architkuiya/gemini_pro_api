from dotenv import load_dotenv
load_dotenv() # take environment variables from .env.

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
## function to load gemini pro model and get responses

def get_response(question):
    # load model
    model = genai.GenerativeModel("gemini-pro")
    # get responses
    response = model.generate_content(question)

    return response.text

## input and submit

st.set_page_config(page_title="Gemini Pro demo", page_icon=":gem:", layout="wide")
st.header("Gemini Pro demo")
input = st.text_input("Input:", key = 'input')
submit = st.button("Submit", key = 'submit')

if submit:
    response = get_response(input)
    st.subheader("Response:")
    st.write(response)
