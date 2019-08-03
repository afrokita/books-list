import sys

sys.path.append('../display')
import colors as dclr

def greet(color):
    dclr.foreground_paint(color, "Greetings!\n")

def get_action():
    valid = {"read": "r", "r": "r",
            "write": "w", "w": "w"}
    question = "Would you to like to read or write contents? [r/w]"

    while True:
        dclr.foreground_paint('Yellow', question)
        choice = input().lower()

        if choice in valid:
            return valid[choice]
        else:
            dclr.foreground_paint('Red', "Select read/write")

def query_yes_no(question):
    valid = {"yes": "y", "y": "y",
             "no": "n", "n": "n"}

    while True:
        dclr.foreground_paint('Yellow', question)
        choice = input().lower()

        if choice in valid:
            return valid[choice]
        else:
            dclr.foreground_paint('Red', "Select yes/no")
