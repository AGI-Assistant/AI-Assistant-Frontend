"""
This module contains functions for initialization of various different components.
"""

import logging
import streamlit as st
from api import get


# Initialize page
def layout():
    """
    This function initializes the layout and page config of the interface.
    """
    # Set page config
    st.set_page_config(page_title="Your AI Assistant",
                       page_icon="🤖",
                       layout="wide")

    # Set page title
    st.title("Your AI Assistant")


# Initialize chat history
def conversation():
    """
    This function initializes the chat history.
    It does so by requesting the chat history from the server
    and storing it in the session state.
    """
    # Initialize chat history
    if "history" not in st.session_state:
        logging.info("Initializing chat history")
        history_request = get.get_history()

        # Check if request was successful
        if history_request.status_code == 200:
            logging.info("Successfully requested chat history")
            st.session_state.history = history_request.json()
        else:
            logging.warning(
                f"Failed requesting chat history, status:{history_request.status_code}")
            st.session_state.history = []
