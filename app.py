import sqlite3

###from lib.###

### Chatbot Definition
class Chatbot:
    def __init__(self):
        self.db = sqlite3.connect("data/chatlog.db")
        self.cursor = None

    def __enter__(self):
        self.cursor = self.db.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        pass

    def start_chat(self):
        pass
    
    def terminate(self, exit_code):
        print("Thanks for using the app :D")
        return