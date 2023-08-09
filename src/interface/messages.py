import datetime
import streamlit as st
from streamlit_chat import message
from api import post


def add(string_value: str,
        true_if_user: bool = True,
        time_stamp: datetime.datetime = datetime.datetime.now()):
    # Add message dict to session state
    st.session_state.history.append({'true_if_user': true_if_user,
                                     'message': string_value,
                                     'sent': time_stamp})


def render(conversation: list[dict]):
    for i in range(len(conversation)):
        message(message=conversation[i]['message'],
                is_user=conversation[i]['true_if_user'],
                key=str(i))


def send(contents: str):
    # Show a spinner during the api call
    with st.spinner(text='Sending message...'):
        response = post.send_message(contents, st.session_state.conversation_id)
        if response.status_code == 201:
            st.success("Message sent!")
            # response.json()['message_id']
        else:
            st.error("Something went wrong...")
