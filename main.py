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
            print_cool = "☆*:.｡.o(≧▽≦)o.｡.:*☆ test mode"
            for _ in range(len(print_cool)):
                sys.stdout.write("\r{0}".format(" "*_ + print_cool[_]))
                sys.stdout.flush()
                sleep(0.125)
                if _ == len(print_cool) - 1:
                    ### only works in Unix...
                    sys.stdout.write("\033[2K\033[1G")
                    sys.stdout.write("\r{0}\n".format("☆*:.｡.o(≧▽≦)o.｡.:*☆"))
            print(">>>", end='')
            text = input()

            ### test chats are not recorded in the database for sample learning. . .
            app.test_chat(text)

        else:
            raise Exception("Please check your arguments")
    ### Unacceptable system arguments at run time
    else:
        raise Exception("Please check your arguments")