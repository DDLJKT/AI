import pyttsx3
engine=pyttsx3.init()
text=input("Enter something: ")
engine.say(text)
engine.runAndWait()
