import streamlit as st
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

from session import SessionHistoryUser

st.set_page_config(
    page_title="educAI",
    page_icon="📚"
)
st.title("educAI")

chat_history = st.empty()  # Define chat_history as a global variable
st.session = SessionHistoryUser()

def init_message(user_name, user_age, user_type_learning):
    st.session_state.messages = [
        SystemMessage(content=f"You are a teacher of a 12 year child with name ${user_name}, ${user_age} years old, you have to respond with a ${user_type_learning}"),
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
    st.radio("responde", options=["1","2","3"])


def main():        

    load_dotenv() 
    
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key is None or openai_api_key == "":
        st.warning("OpenAI API key is not set. Please set the API key.")
        
    chat = ChatOpenAI(temperature=0)

    local_session = st.session

    if "user" not in st.session_state:
        local_session.resetMessages()
    
    with st.sidebar:
        st.title("User info")
        user_name = st.text_input("Name", value=local_session.user)
        user_age = st.number_input("Age", value=local_session.age)
        st.title("Customize learning")
        user_type_learning= st.selectbox(
        'Who would you like to be your teacher',
        ('Cuentos', 'Logico', 'Rimas'), index=local_session.user_type_learning)
           
    if "messages" not in st.session_state:
        init_message(user_name, user_age, user_type_learning)

    st.text(user_name + str(user_age) + user_type_learning)
    input_user = st.chat_input("write your question")
    if input_user:
        st.session_state.messages.append(HumanMessage(content=input_user))
        with st.spinner("Thinking..."):
            response = chat(st.session_state.messages)  
            st.session_state.messages.append(AIMessage(content=response.content))     
    showAllMessages(st.session_state.get("messages", []))



if __name__ == "__main__":
    main()




    # user_input = st.text_input("Your message:", key="user_input")

    # if user_input:
    #     st.session_state.messages.append(HumanMessage(content=user_input))
    #     with st.spinner("Thinking..."):
    #         response = chat(st.session_state.messages)
    #     #First bot response
    #     radio_config = bot_message(response)
        
    #     with st.radio(label = "hola", options = radio_config["options"]):
    #         st.text("response")


    # Display all chat messages
    #showAllMessages(st.session_state.get("messages", []))

# def bot_message(response):
#     content = f"{response.content}\n\nResponde el siguiente quiz:\n\n"

#     # Use Markdown to display the question
#     content += "¿Cómo se forman las nubes?\n\n"

#     # Use radio buttons to provide options
#     options = ["uno", "dos", "tres"]
#     correct = "uno"
#     return { 'options' : options , 'correct_answer' : correct}
    # if radioMessage:
    #     # Include the selected option in the content
    #     option_selected = f"Respuesta seleccionada: {radioMessage}"
    #     st.session_state.messages.append(AIMessage(content=content, type="ai"))
    #     st.session_state.messages.append(HumanMessage(content=option_selected, type="none"))