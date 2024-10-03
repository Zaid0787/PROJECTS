import os
import pyttsx3
from pyttsx3.six import text_type

if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1 Created by Zaid")
    while True:
        x = input("Enter what you want me to speak: ")
        if x== "q":
            y = ("bye bye friends")
            no = pyttsx3.init()
            no.say(y)
            no.runAndWait()
            break
        Word = pyttsx3.init()
        Word.say(x)
        Word.runAndWait()