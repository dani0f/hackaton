from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
import random

load_dotenv() 

llm = ChatOpenAI(temperature=0)


def identificador(input_user):
    messages = [
        SystemMessage(content="Your job is to only return 1 if the input is a question and 0 if it is not a question. You must ignore questions like 'What is your name?' or 'How are you?'"),
        ]
    messages.append(
        HumanMessage(content=input_user)
    )

    res = llm(messages)
    try:
        flag = int(res.content[0])
    except:
        flag = 0
    print(flag)
    return flag

def clasificador(input_user):
    messages = [
        SystemMessage(content="You are ExpertGPT Model that can answer questions about the world or any topic in particular in a friendly and pedagogical way. "+
                      "You are in charge of talking to a user between the ages of 10 and 15 who is learning about any topic related to school and general knowledge. "+
                      "You can answer questions about the world or any topic in particular in a friendly and pedagogical way. "+"You need to try to convince the user to ask you a question. Always talk in spanish.")
        ]
    
    question = identificador(input_user)
    if question:
        res = teacher(input_user, "Alfonso", 12, "Lógico")
        return res
    else:
        messages.append(
            HumanMessage(content=input_user)
        )
        res = llm(messages)
        return res.content

def teacher(input_user, user_name, user_age, user_type_learning):
    messages = [
        SystemMessage(content=f"You are a teacher of a 12 year child with name ${user_name}, ${user_age} years old, you have to respond with a ${user_type_learning} way of teaching. Afterwards, you have to ask the user a question about the topic that can be answered through multiple choice with only 3 options with numbers 1,2 and 3. Always talk in spanish."),
    ]
    messages.append(
        HumanMessage(content=input_user)
    )

    res = llm(messages)
    ola = analyzer(res.content, "1")
    print(ola)
    return res.content
    
def analyzer(input_ai, choice_user):
    messages = [
        SystemMessage(content="Read the question and return the number of the correct answer as the first character of the response."),
    ]
    messages.append(
        HumanMessage(content=input_ai)
    )

    res = llm(messages)
    return learning(res.content[0], choice_user)

def learning(correct_option, choice_user):
    if correct_option == choice_user:
        return 1
    else:
        return 0

def ajuste_temp(temperatura):
    temperature=max(0.1,temperatura*random.uniform(0.85,1))
    return temperature