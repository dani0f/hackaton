# --- Imports ---
import streamlit as st
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

from session import SessionHistoryUser
from learning_types import get_type_learning

from agente import clasificador

import os

# --- Streamlit ---
st.set_page_config(
    page_title="educAI",
    page_icon="📚"
)
st.title("educAI")

# --- Load environment variables ---
load_dotenv() 

# --- Global Variables
st.session = SessionHistoryUser()
chat_history = st.empty()  # Este es para llenar el text-area

# --- Métodos ---
def init_message(user_name, user_age, user_type_learning):
    st.session.messages = [
        SystemMessage(content=f"You are a teacher of a {user_age} year child with name {user_name}, you have to respond with a {get_type_learning(user_type_learning)}"),
    ]

def showAllMessages(messages):
    chat_history_content = ""
    for msg in messages:
        if isinstance(msg, HumanMessage):
            chat_history_content += f"😎 You: {msg.content}\n\n"
        elif isinstance(msg, AIMessage):
            chat_history_content += f"👨‍🏫 Bot: {msg.content}\n\n"
    chat_history.text_area("History",chat_history_content, height=400)
    st.balloons()
    #st.radio("responde", options=["1","2","3"])

def get_user_info(sidebar, local_session):
    user_name = sidebar.text_input("Name", value=local_session.user, on_change=local_session.resetMessages())
    user_age = sidebar.number_input("Age", value=local_session.age,  on_change=local_session.resetMessages())
    user_type_learning= sidebar.selectbox(
    '¿Quién te gustaría que fuese tu profesor?',
    ('Cuentos', 'Logico', 'Rimas'), index=local_session.user_type_learning, on_change=local_session.resetMessages())
    return user_name, user_age, user_type_learning


# --- Main ---

def main():       
    local_session = st.session

    with st.sidebar:
        user_name, user_age, user_type_learning = get_user_info(st.sidebar, local_session)

    if  len(local_session.messages) == 0:
        init_message(user_name, user_age, user_type_learning)

    st.text(user_name + str(user_age) + user_type_learning)
    input_user = st.chat_input("write your question")
    if input_user:
        local_session.messages.append(HumanMessage(content=input_user))
        with st.spinner("Thinking..."):
            response = clasificador(input_user)
            local_session.messages.append(AIMessage(content=response))     
    showAllMessages(local_session.getMessages())

if __name__ == "__main__":
    main()