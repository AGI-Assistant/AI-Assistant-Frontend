"""
This module holds all post requests.
"""
import requests as rq
import streamlit as st


# Send message
def send_message(contents: str) -> rq.models.Response:
    """
    This function sends a message to the API.

    Args:
        contents (str): The content of the message.

    Returns:
        requests.models.Response: A request object, containing the response.
    """
    return rq.post(
        url=st.session_state['api_url'] + '/user/send',
        data=contents,
        headers={'conversationId': st.session_state['api_conversation_id'],
                 'apiKey': st.session_state['api_key']})
