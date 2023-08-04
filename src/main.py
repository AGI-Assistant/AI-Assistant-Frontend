"""
Main file for running the chat app
Run with streamlit run src\main.py

https://pypi.org/project/streamlit-chat/
"""
import time
import datetime
import streamlit as st
from streamlit_chat import message


# Add a message to the chat history
def add_message(string_value: str,
                true_if_user: bool = True,
                time_stamp: datetime.datetime = datetime.datetime.now()):
    # Add message dict to session state
    st.session_state.history.append({'true_if_user': true_if_user,
                                     'message': string_value,
                                     'sent': time_stamp})


def send_message():
    # Add user message to chat history and rerun
    add_message(st.session_state.message, true_if_user=True)

    # Show a spinner during the api call
    with st.spinner(text='Sending message...'):
        # Add API call here!
        time.sleep(1)
        add_message("This works!", False)


if __name__ == "__main__":

    # Set page title and containers
    st.title("Simple Chat App")
    message_container = st.empty()
    input_container = st.empty()

    # Initialize session state and display messages if they exist
    if "history" not in st.session_state:
        st.session_state.history = []
    else:
        with message_container.container():
            for i in range(len(st.session_state['history'])):
                message(message=st.session_state['history'][i]['message'],
                        is_user=st.session_state['history'][i]['true_if_user'],
                        key=str(i))

    # Handle user input
    with input_container.container():
        st.session_state.message = st.text_input("Type your message here...",
                                                 on_change=send_message,
                                                 key="message_input")
        st.button("Send", on_click=send_message)
