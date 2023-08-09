"""
This module contains all functions necessary for working with messages.
"""
import datetime
import logging
import streamlit as st
from streamlit_chat import message
from api import post


# Add message
def _add(string_value: str, true_if_user: bool,
         time_stamp: datetime.datetime = datetime.datetime.now()):
    """
    This Private function adds a message to the conversation history,
    saved in the session state.

    Args:
        string_value (str): The content of the message.
        true_if_user (bool): Value indicating if the message was sent by the user or the AI.
    """
    # Add message dict to session state
    st.session_state.history.append({'true_if_user': true_if_user,
                                     'message': string_value,
                                     'sent': time_stamp})


# Render conversation
def render(conversation: list[dict]):
    """
    This function takes a list of message dictionary's
    and displays messages for every one of them.

    Args:
        conversation (list[dict]): A list of message dictionary's (like from _add() function).
    """
    for i in range(len(conversation)):
        message(message=conversation[i]['message'],
                is_user=conversation[i]['true_if_user'],
                key=str(i))


# Send message
def send_and_process(contents: str):
    """
    This function handles the interaction with the server.
    It takes a message, sends it to the server and processes the response,
    by saving both the message and answer form the AI to the conversation history.

    Args:
        contents (str): A string with the message to send.
    """
    logging.info(f"Attempting to send message")
    # Send the message
    response = post.send_message(contents)

    # Check the response
    if response.status_code == 201:
        # Add the messages to the conversation
        _add(contents, True)
        _add(response.json()['answer'], False)
        logging.info(f"Message sent processed successfully")
    else:
        # Print error
        logging.error(f"Error sending message: {response.status_code}")
        st.error("Something went wrong...")
