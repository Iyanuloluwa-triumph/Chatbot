import sys
from cores import core


def main():
    name = input("Name to begin with chatbot: ")
    print(f"Hi {name}, welcome to this simple chatbot\n Type 'help' for help")
    chat()


def chat():
    while True:
        help1 = "*Chatbot can make conversation\n"\
                '1."/exit" to exit\n' \
                '2. "/explain" to explain term\n3. /define" to define term\n' \
                '4. "/fetch" to fetch weather data from specified location'
        userinput = input("> ")
        if userinput.lower() == "help":
            print(help1)
        elif userinput.lower() == "/exit":
            sys.exit("Goodbye!")
        else:
            print(core(userinput))


if __name__ == "__main__":
    main()


