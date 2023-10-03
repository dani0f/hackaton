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
import streamlit as st
import random

from dotenv import load_dotenv
load_dotenv()

llm=AzureChatOpenAI(
    deployment_name="educai_chat35", #educai_chat35_16k
    model_name="gpt-35-turbo", #gpt-35-turbo-16k
    temperature=0.5,
)

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
    print("Identify")
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
        SystemMessage(content=f"You are a teacher of a 12 year child with name ${user_name}, ${user_age} years old, you have to respond with a ${user_type_learning} way of teaching. Afterwards, you have to ask the user a question about the topic that can be answered through multiple choice. Always talk in spanish."),
    ]
    messages.append(
        HumanMessage(content=input_user)
    )

    res = llm(messages)
    return res.content

def analyzer(input_ai, choice_user):
    messages = [
        SystemMessage(content=f"Your job is to analyze this AI response with a multiple choice question at the end. You must figure out which choice is the correct one and compare it to the number the user chose, which is {choice_user}. If the answer is right only return the number 1, else return 0."),
    ]
    messages.append(
        HumanMessage(choice_user),
        AIMessage(content=input_ai)
    )

    res = llm(messages)
    try:
        flag = int(res.content[0])
    except:
        flag = 0
    print("Analyze")
    print(flag)
    return flag

def ajuste():   
    temperature=max(0.1,temperature*random.uniform(0.85,1))
    return temperature
    