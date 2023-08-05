import streamlit as st


def layout():
    # Set page config
    st.set_page_config(page_title="Your AI Assistant",
                       page_icon="🤖",
                       layout="wide")

    # Set page title
    st.title("Your AI Assistant")

    # Initialize chat history
    if "history" not in st.session_state:
        st.session_state.history = []