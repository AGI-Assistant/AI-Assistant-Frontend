"""
Main file for running the chat app.
https://github.com/Knaeckebrothero/AGI-Assistant-Frontend
"""
import os
import streamlit as st
from dotenv import load_dotenv
import interface as msgr
from interface import init

# The main function for running the app.
if __name__ == "__main__":
    # Load environment variables and save them in the session state.
    load_dotenv()
    st.session_state.api_url = os.getenv("API_URL")
    st.session_state.api_key = os.getenv("API_KEY")
    st.session_state.api_conversation_id = os.getenv("TEST_CONVERSATION_ID")

    # Initialize the app and device it into two containers.
    init.layout()
    init.conversation()
    message_container = st.container()
    input_container = st.container()

    # Text field for the user to input his messages.
    temp_message = input_container.text_input("Type your message here...")

    # Button for sending the message
    if input_container.button("Send"):
        with st.spinner(text='Sending message...'):
            msgr.send_and_process(temp_message)

    # Displays the messages after running the program (if they exist ofc.).
    if "history" in st.session_state:
        with message_container.container():
            msgr.render(st.session_state['history'])
