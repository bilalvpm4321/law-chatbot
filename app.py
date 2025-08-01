import streamlit as st
from utils import qa_pipeline

# Initialize the QA pipeline once globally
qa = qa_pipeline()

# Provide static context or load from a file/db
CONTEXT = """
Indian law is derived from a mix of common law, statutory law, constitutional provisions, and customary principles.
It covers various domains like criminal law, civil law, constitutional law, family law, and more.
For example, Article 21 of the Indian Constitution guarantees the right to life and personal liberty.
"""

def initialize_session():
    if 'chat_log' not in st.session_state:
        st.session_state.chat_log = []

def process_user_input(user_input):
    # Run QA pipeline with question and context
    result = qa({
        "question": user_input,
        "context": CONTEXT
    })
    return result['answer']

def display_chat_log():
    for exchange in st.session_state.chat_log:
        st.markdown(f'**You:** {exchange["User"]}')
        st.markdown(f'**Bot:** {exchange["Bot"]}')

def main():
    st.title('Indian Law Q&A Bot')
    initialize_session()

    user_input = st.text_input("You:")

    if user_input:
        bot_output = process_user_input(user_input)
        st.session_state.chat_log.append({"User": user_input, "Bot": bot_output})
        st.text_input("You:", value="", key="new_input_box")  # Reset input box

    display_chat_log()

if __name__ == "__main__":
    main()
