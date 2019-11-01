####################
import sys
from wAIfu.app import Chatbot
####################

app = Chatbot()


if __name__ == "__main__":
    ### Runs the app in its pre-trained state
    if len(sys.argv) == 1:
        with app as wAIfu:
            ### open interactive w/e
            
            ### begin chat! have fun talking to her~~~ ###
            wAIfu.start_chat()
            ##############################################
    elif len(sys.argv) == 2:
        if sys.argv[1] == "--train":
            pass
        elif sys.argv[1] == "--test":
            pass
        else:
            raise Exception("Please check your arguments")
    ### Unacceptable system arguments at run time
    else:
        raise Exception("Please check your arguments")