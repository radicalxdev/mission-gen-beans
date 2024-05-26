import streamlit as st
from genai.core import chat

st.title("Gen AI test")

prompt = "Explain gravity"

responses = chat.send_message(prompt, stream=True)
for chunk in responses:
    text = chunk.text
    st.write(text)
