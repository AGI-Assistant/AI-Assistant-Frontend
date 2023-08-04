import streamlit as st
from streamlit_chat import message


def send_message():
    message_prompt = st.session_state.message_prompt
    st.session_state.past.append(message_prompt)
    st.session_state.generated.append("This works!")


# if __name__ == "__main__":

st.title("Chat App")

# Initialize variables
message_container = st.empty()

# Display chat history
with message_container.container():
    for i in range(len(st.session_state['messages'])):
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
        message(st.session_state['messages'][i]['data'], key=f"{i}")

with st.container():
    st.text_input("User Input:", on_change=send_message, key="message_prompt")
