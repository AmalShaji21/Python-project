import pyttsx3

if __name__ == "__main__":
    print("Welcome to our robo speakerpro v1.2, Created by Amal")
    engine = pyttsx3.init(driverName='sapi5')  # Specify the TTS engine (sapi5 for Windows)
    while True:
        x = input("Enter the word that you want to speak (enter 'q' to quit): ")
        if x.lower() == "q":
            message = ("You have quit the robo speaker pro, closing the program")
            print(message)
            engine.say(message)
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()




