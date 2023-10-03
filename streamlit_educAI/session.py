
## Esta clase sirve para guardar el historial de mensajes de cada usuario
class SessionHistoryUser:
    def __init__(self, user_name = "Dummy", user_age = 7, user_type_learning = 0):
        self.user : str = user_name
        self.user_type_learning : int = user_type_learning
        self.age : int = user_age
        self.label : str = ""
        self.messages : list = []
        self.selection_option : int = 0

    def getMessages(self):
        return self.messages
    
    def addMessage(self, message):
        try:
            self.messages.append(message)
            return True
        except:
            print("Error adding message")
            return False
        
    def resetMessages(self):
        self.messages = []
    
    def returnContext(self):
        assert len(self.messages) > 0
        return self.messages[0]

""" def create_uuid_from_username(s: str):
    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return uuid.UUID(m.hexdigest()) """