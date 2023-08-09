"""
This module holds all get requests.
"""

import requests as rq
import streamlit as st


# Request conversation history
def get_history() -> rq.models.Response:
    """
    This function fetches the conversation history from the API.

    Returns:
        requests.models.Response: A request object, containing the response.
    """
    return rq.get(
        url=st.session_state['api_url'] + '/conversation/history',
        headers={'conversationId': st.session_state['api_conversation_id'],
                 'apiKey': st.session_state['api_key']})
