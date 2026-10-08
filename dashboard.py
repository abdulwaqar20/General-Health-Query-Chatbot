import streamlit as st

from health_chatbot import HealthChatbot


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="General Health Chatbot",
    page_icon="🩺",
    layout="centered"
)


# --------------------------------------------------
# Page Header
# --------------------------------------------------

st.title("🩺 General Health Chatbot")

st.markdown(
    """
    Ask general health-related questions and receive
    educational information powered by **LLaMA 3.1**.
    """
)


# --------------------------------------------------
# Medical Disclaimer
# --------------------------------------------------

st.warning(
    """
    **Medical Disclaimer**

    This chatbot provides general health information only.
    It does not diagnose medical conditions, prescribe medication,
    or replace professional medical advice.

    If you are experiencing a medical emergency, contact
    your local emergency services or seek immediate medical care.
    """
)


# --------------------------------------------------
# Initialize Chatbot
# --------------------------------------------------

if "chatbot" not in st.session_state:
    st.session_state.chatbot = HealthChatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("About")

    st.write(
        """
        This project is a general health information chatbot
        built using:

        - Python
        - Groq API
        - LLaMA 3.1
        - Streamlit
        - Prompt Engineering
        """
    )

    st.divider()

    if st.button("🗑️ Clear Conversation", use_container_width=True):

        st.session_state.chatbot.clear_history()
        st.session_state.messages = []

        st.rerun()


# --------------------------------------------------
# Display Previous Messages
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# --------------------------------------------------
# Chat Input
# --------------------------------------------------

user_input = st.chat_input(
    "Ask a general health question..."
)


# --------------------------------------------------
# Process User Message
# --------------------------------------------------

if user_input:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = st.session_state.chatbot.chat(
                user_input
            )

        st.markdown(response)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })