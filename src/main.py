"""
Main file for running the chat app
Run with streamlit run src\main.py

https://pypi.org/project/streamlit-chat/
"""
import streamlit as st
import interface as msgr
from interface import init

if __name__ == "__main__":
    # Initialize layout and containers
    init.layout()
    message_container = st.container()
    input_container = st.container()

    # Handle user input
    temp_message = input_container.text_input("Type your message here...")

    if input_container.button("Send"):
        msgr.add(temp_message, True)

    # Display messages if they exist
    if "history" in st.session_state:
        with message_container.container():
            msgr.render(st.session_state['history'])
