import random
from dict import fallback_responses


def genvalue(user_input):
    for word in user_input.lower().split():
        if word in fallback_responses:
            return random.choice(fallback_responses[word]["responses"])
    return f"I'm still learning how to respond to that. Can you rephrase it"




