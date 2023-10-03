
## Esta clase sirve para guardar el historial de mensajes de cada usuario
class SessionHistoryUser:
    def __init__(self, user_name = "dummy", user_age = 0, user_type_learning = 0):
        self.user : str = user_name
        self.user_type_learning : int = user_age
        self.age : int = user_type_learning
        self.messages : list = []

    def getMessages(self):
        return self.messages
    
    def addMessage(self, message):
        try:
            self.messages.append(message)
            return True
        except:
            print("Error adding message")
            return False
        
    def resetMessages(self, user_name = "dummy", user_age = 0, user_type_learning = 0):
        self.user = user_name
        self.user_type_learning = user_age
        self.age = user_type_learning
        self.messages = []

""" def create_uuid_from_username(s: str):
    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return uuid.UUID(m.hexdigest()) """