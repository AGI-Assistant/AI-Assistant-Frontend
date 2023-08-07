"""
Main file for running the chat app
Run with streamlit run src\main.py

https://pypi.org/project/streamlit-chat/
"""
import streamlit as st
import interface as msgr
from interface import init
import requests
import json

if __name__ == "__main__":
    session = requests.Session()
    # Initialize layout and containers
    init.layout()
    message_container = st.container()
    input_container = st.container()

    # Handle user input
    temp_message = input_container.text_input("Type your message here...")

    if input_container.button("Send"):
        promptObject = {
            "username": "John",
            "prompt": temp_message
        }
        prompt = json.dumps(promptObject)
        data = requests.post("http://localhost:8081/ai", prompt)

        id = data.text
        id = id.replace('"', '')

        r = requests.get(f"http://localhost:8081/ai/{id}")

        response_json = r.json()  # Parse the JSON response

        message = response_json['prompt']

        if data:
            msgr.add(message, True)

        else:
            st.error("Error")

    # Display messages if they exist
    if "history" in st.session_state:
        with message_container.container():
            msgr.render(st.session_state['history'])
