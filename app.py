import sqlite3
from wAIfu.lib.network import Seq2Seq, AdaBoost

###from lib.###

### Chatbot Definition
class Chatbot:
    def __init__(self):
        ### wAIfu Intelligence ###
        self.waifu = Seq2Seq()
        ##########################
        self.db = sqlite3.connect("data/chatlog.db")
        self.cursor = None
        self.status = 0
    
    def __call__(self):
        pass

    def __enter__(self):
        self.cursor = self.db.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        pass

    def start_chat(self):
        while not self.status:
            pass
    
    def test_chat(self, text):
        return
    
    def terminate(self, exit_code):
        print("Thanks for using the app :D")
        return