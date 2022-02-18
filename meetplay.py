#!/usr/bin/env python3

import speech_recognition as sr
from playsound import playsound
from pynput.keyboard import Key, Controller
import subprocess

r = sr.Recognizer()
m = sr.Microphone()

print("\n\n\nsr init done")

keyboard = Controller()
audioFile = 'audio.wav'

# word list to listen for
wordList = ["example", "test", "words"]

# set the audio device monitor and mic here, which can be found by running
# pacmd list-sources | grep -e 'index:' -e device.string -e 'name:'
# for example: alsa_output.device.monitor
audioDevice = "YOUR AUDIO OUTPUT MONITOR HERE"
microphoneDevice = "YOUR MICROPHONE INPUT HERE"

print("Changing default source...")
subprocess.run(["pactl", "set-default-source", audioDevice])

# listening to the actual microphone - optionally, these lines can be uncommented
# print("Restoring microphone...")
# subprocess.run(["pactl", "set-default-source", microphoneDevice])


# google meet unmute and mute - optionally, this can be uncommented in the loop
def mute():
    keyboard.press(Key.ctrl_l)
    keyboard.press('d')
    keyboard.release(Key.ctrl_l)
    keyboard.release('d')

def mute_and_play():
    mute()
    playsound(audioFile)
    mute()

# comment out if not using google cloud speech API
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""YOUR JSON FILE CONTENTS HERE"""

# you can change recognize_google_cloud to the engine of your choice, for alternatives look here: https://github.com/Uberi/speech_recognition
# language can be changed as well: https://cloud.google.com/speech-to-text/docs/languages
def recognize():
    with m as source:
            print("Listening now.")
            audio = r.listen(source)
    text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, language='en-GB')
    print(text)
    for word in wordList:
        if word in text:
            return 1


while True:
    try:
        if recognize() == 1:
            # mute_and_play()
            playsound(audioFile)
            break
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))
        break

print("Restoring microphone...")
subprocess.run(["pactl", "set-default-source", microphoneDevice])
