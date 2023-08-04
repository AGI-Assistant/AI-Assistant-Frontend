# Description: Main file for running the chat app
# Run with: streamlit run src\main.py

import time
import streamlit as st
from streamlit_chat import message


if __name__ == "__main__":

    # Set page title
    st.title("Simple Chat App")

    # Initialize chat history if it doesn't exist and display it if it does
    if "messages" not in st.session_state:
        st.session_state.messages = []
    else:
        for i in range(len(st.session_state['messages'])):
            message(st.session_state['messages'][i]['content'],
                    is_user=st.session_state['messages'][i]['role'] == 'user',
                    key=f"{i}_user")

    # Handle user input
    if prompt := st.text_input("Type your message here..."):

        # Send user message to API
        message_id = 201

        # Handle API response
        if message_id == 201:
            with st.spinner(text='Generating response...'):
                # Get API response using message ID
                answer_content = "Great this works!"
                time.sleep(2)

            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

            # Add API response to chat history
            st.session_state.messages.append(
                {"role": "assistant", "content": answer_content})
        else:
            st.error("Something went wrong...")
