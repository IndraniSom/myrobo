import pyttsx3
text_speech=pyttsx3.init()
greet="Hello user welcome to the robo speaker made by Indrani Som"
text_speech.say(greet)
text_speech.runAndWait()

while True:
    answer = input("enter what you want me to say ")
    if answer=="stop":
        break
    else:
        text_speech.say(answer)
        text_speech.runAndWait()



    
