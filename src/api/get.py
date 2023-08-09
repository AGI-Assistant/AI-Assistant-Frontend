"""
This package holds all APIs needed to run the frontend chat interface.
"""

import requests as rq
import streamlit as st


# Request the conversation history from the server.
def get_history() -> rq.models.Response:
    return rq.get(
        url=st.session_state['api_url'] + '/conversation/history',
        headers={'conversationId': st.session_state['api_conversation_id'],
                 'apiKey': st.session_state['api_key']})
