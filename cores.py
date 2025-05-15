from wikipidia import wiki, wiki_def
from dict import fake_NLP
from weather import weather
import valuegenerator


def core(*n):
    if not n:
        return "No input provided."

    tokens = n[0].strip().lower().split()
    command = tokens[0]
    args = tokens[1:]

    if command == "/explain":
        return wiki(*args)

    elif command == "/define":
        if args:
            return wiki_def(*args)
        else:
            return "Sorry,'/define' is used with input"
    elif command == "/fetch":
        if len(args) == 1:
            word = ""
            for item in args:
                word += item
            return weather.get_temp(word.strip())
        else:
            return "Invalid Input for /fetch. Use: /fetch [city]"

    else:
        user_input = ""
        for items in tokens:  # if not a command, treat as input
            user_input += items + " "
        for phrase, response in fake_NLP.items():
            if phrase in user_input:
                return response
        return valuegenerator.genvalue(user_input)
