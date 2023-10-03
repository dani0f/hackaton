from session import SessionHistoryUser
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
)
from dotenv import load_dotenv

class Agents:
    def __init__(self, session_history: SessionHistoryUser):
        load_dotenv()
        self.llm = AzureChatOpenAI(
                deployment_name="educai_chat35",
                model_name="gpt-35-turbo",
                temperature=0.5,)
        
        self.session_history = session_history
        
    def chain(self, input_user):
        print(f"Input user: {input_user} \n Nombre: {self.session_history.user} \n Age {self.session_history.age}" )
        return self.clasificador(input_user)
        
    def clasificador(self, input_user):
        messages = [
            SystemMessage(content="You are ExpertGPT Model that can answer questions about the world or any topic in particular in a friendly and pedagogical way. "+
                        "You are in charge of talking to a user between the ages of 10 and 15 who is learning about any topic related to school and general knowledge. "+
                        "You can answer questions about the world or any topic in particular in a friendly and pedagogical way. "+"You need to try to convince the user to ask you a question. Always talk in spanish.")
            ]
        
        question = self.identifier(input_user)
        if question:
            res = self.teacher(input_user)
            return res
        else:
            messages.append(
                HumanMessage(content=input_user)
            )
            res = self.llm(messages)
            return res.content
        
    def identifier(self, input_user: str):

        messages = [
            SystemMessage(content="Your job is to only return 1 if the input is a question and 0 if it is not a question. You must ignore questions like 'What is your name?' or 'How are you?'"),
        ]

        messages.append(
            HumanMessage(content=input_user)
        )

        res = self.llm(messages)

        try:
            flag = int(res.content[0])
        except:
            flag = 0
        print(flag)
        return flag


    def teacher(self, input_user):
        messages = [
            SystemMessage(content=f"You are a teacher for a child with name {self.session_history.user}, {self.session_history.age} years old, you have to respond with a {self.session_history.user_type_learning} way of teaching. Afterwards, you have to ask the user a question about the topic that can be answered through multiple choice with only 3 options with numbers 1, 2 and 3. Always talk in spanish."),
        ]
        messages.append(
            HumanMessage(content=input_user)
        )

        res = self.llm(messages)
        return res.content
            
