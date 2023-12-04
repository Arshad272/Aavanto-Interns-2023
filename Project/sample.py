import pyttsx3
import speech_recognition as sr
import webbrowser 
import os 

def convert_speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something:")
        # Adjust for ambient noise and listen to the audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Use Google Web Speech API to recognize the audio
            text = recognizer.recognize_google(audio)
            print(f"You said - {text}")
            return text 
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error with the request to Google Web Speech API; {e}")


def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()


while True:
    text = "I am listening"
    text_to_speech(text)
    command = convert_speech_to_text()
    command = command.lower()
    if 'open instagram' in command:
        webbrowser.open("www.instagram.com") 

    if 'control panel' in command:
        os.system("control panel")

    elif 'exit' in command:
        text_to_speech("Good bye, see you again")
        break

    else:
        text_to_speech("I don't know")

    