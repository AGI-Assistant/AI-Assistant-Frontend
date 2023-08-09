"""
This is the main function for running the chat interface.
It has to be executed with streamlit run main.py to start the application.

https://github.com/Knaeckebrothero/AGI-Assistant-Frontend
"""
import os
import streamlit as st
from dotenv import load_dotenv
import interface as msgr
from interface import init

# Main function
if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    st.session_state.api_url = os.getenv("API_URL")
    st.session_state.api_key = os.getenv("API_KEY")
    st.session_state.api_conversation_id = os.getenv("TEST_CONVERSATION_ID")

    # Initialize the app
    init.layout()
    init.conversation()
    message_container = st.container()
    input_container = st.container()

    # Handle the user input
    temp_message = input_container.text_input("Type your message here...")

    if input_container.button("Send"):
        msgr.add(temp_message, True)

    # Display messages if they exist
    if "history" in st.session_state:
        with message_container.container():
            msgr.render(st.session_state['history'])
