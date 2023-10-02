import streamlit as st
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

st.set_page_config(
    page_title="educAI",
    page_icon="📚"
)

chat_history = st.empty()  # Define chat_history as a global variable

radioMessage = st.empty()

def init():
    load_dotenv()
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("Openai key is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

def init_message():
    st.session_state.messages = [
        SystemMessage(content="You are a teacher of 12 year old childs"),
    ]

def showAllMessages(messages):
    chat_history_content = ""
    for msg in messages:
        if isinstance(msg, HumanMessage):
            chat_history_content += f"😎 You: {msg.content}\n\n"
        elif isinstance(msg, AIMessage):
            chat_history_content += f"👨‍🏫 Bot: {msg.content}\n\n"
    chat_history.text(chat_history_content)

def bot_message(response):
    content = f"{response.content}\n\nResponde el siguiente quiz:\n\n"

    # Use Markdown to display the question
    content += "¿Cómo se forman las nubes?\n\n"

    # Use radio buttons to provide options
    options = ["uno", "dos", "tres"]
    correct = "uno"
    return { 'options' : options , 'correct_answer' : correct}
    # if radioMessage:
    #     # Include the selected option in the content
    #     option_selected = f"Respuesta seleccionada: {radioMessage}"
    #     st.session_state.messages.append(AIMessage(content=content, type="ai"))
    #     st.session_state.messages.append(HumanMessage(content=option_selected, type="none"))

def main():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if openai_api_key is None or openai_api_key == "":
        st.warning("OpenAI API key is not set. Please set the API key.")
        return


    chat = ChatOpenAI(temperature=0)

    if "messages" not in st.session_state:
        init_message()



    user_input = st.text_input("Your message:", key="user_input")

    if user_input:
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("Thinking..."):
            response = chat(st.session_state.messages)
        #First bot response
        radio_config = bot_message(response)
        
        with st.radio(label = "hola", options = radio_config["options"]):
            st.text("response")


    # Display all chat messages
    #showAllMessages(st.session_state.get("messages", []))


    

if __name__ == '__main__':
    main()
