import streamlit as st
from gpt4all import GPT4All

# Update with your downloaded model's filename
model_path = r"C:\Users\Thomas\mistral-7b-instruct-v0.1.Q4_K_M.gguf"

gpt = GPT4All(model_path, allow_download=False)

st.title("💬 AI Chatbot!")
st.write("This chatbot is COMPLETELY home made!")
st.write("Credit goes to MistralAi, ChatGPT, and Thomas Fairfield")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Use st.chat_input() instead of st.text_input()
user_input = st.chat_input("Type your message here...")

# Process input only after user submits a message
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Show "Thinking..." message
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("🤖 *Thinking...*")

    # Generate AI response
    with gpt.chat_session():
        ai_reply = gpt.generate(user_input)

    # Replace "Thinking..." with actual response
    message_placeholder.markdown(ai_reply)

    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

    # Force rerun to update UI
    st.rerun()
