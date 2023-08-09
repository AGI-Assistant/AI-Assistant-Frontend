"""
This module holds the initialization functions for the interface.
"""

import logging
import streamlit as st
from api import get


# Initialize layout and cfg
def layout():
    # Set page config
    st.set_page_config(page_title="Your AI Assistant",
                       page_icon="🤖",
                       layout="wide")

    # Set page title
    st.title("Your AI Assistant")


# Initialize and load chat history
def conversation():
    # Initialize chat history
    if "history" not in st.session_state:
        logging.info("Initializing chat history")
        history_request = get.get_history()

        if history_request.status_code == 200:
            logging.info("Successfully requested chat history")
            st.session_state.history = history_request.json()
        else:
            logging.warning(
                f"Failed requesting chat history, status:{history_request.status_code}")
            st.session_state.history = []
