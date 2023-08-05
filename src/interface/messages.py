import datetime
import streamlit as st
from streamlit_chat import message


def add_message(string_value: str,
                true_if_user: bool = True,
                time_stamp: datetime.datetime = datetime.datetime.now()):
    # Add message dict to session state
    st.session_state.history.append({'true_if_user': true_if_user,
                                     'message': string_value,
                                     'sent': time_stamp})


def render_messages(conversation: list[dict]):
    for i in range(len(conversation)):
        message(message=conversation[i]['message'],
                is_user=conversation[i]['true_if_user'],
                key=str(i))
