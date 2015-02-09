__author__ = 'Charlie'

import random

INSULTS = [
    "You are funny lookin!",
    "I don't know what your problem is, but I'll bet it's hard to pronounce.",
    "How about never? Is never good for you?",
    "I see you've set aside this special time to humiliate yourself in public.",
    "I'll try being nicer if you'll try being smarter.",
    "It sounds like English, but I can't understand a word you're saying.",
    "I will always cherish the initial misconceptions I had about you.",
    "The fact that no one understands you doesn't mean you're an artist.",
    "Whatever kind of look you were going for, you missed."
    ]

def get_insult():
    """returns a random insult"""
    return random.choice(INSULTS)
