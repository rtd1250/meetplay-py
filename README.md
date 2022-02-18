# meetplay-py

## Info
A simple python3 program that listens to the computer (or microphone) audio, and plays a sound file if it finds a specific word. Originally written for unmuting on Google Meet, playing a sound, then muting the microphone back again, but it can be used for any other purpose.

Works only on Linux.

Used libraries:
- [**speech_recognition**](https://pypi.org/project/SpeechRecognition/)
- [playsound](https://pypi.org/project/playsound/)
- [pynput](https://pypi.org/project/pynput/)
- [pyaudio](https://pypi.org/project/PyAudio/)

## Installation
Debian/Ubuntu requires these packages in addition to pip modules:
```
sudo apt install portaudio19-dev python3-gst-1.0
```

Use pip to get the modules:
```
pip3 install speechrecognition
pip3 install playsound
pip3 install pynput
pip3 install pyaudio
```

If using Google Cloud Speech API:
```
pip3 install google-cloud-speech
pip3 install oauth2client
pip3 install google-api-python-client
```

If using CMU Sphinx:
```
pip3 install pocketsphinx
```

For other engines, you are on your own.

## Usage:
First of all, check your pulseaudio device names - microphone and output monitor:
```
pacmd list-sources | grep -e 'index:' -e device.string -e 'name:'
```

Then, copy the names over to strings audioDevice and microphoneDevice in meetplay.py.
For example:
```python
audioDevice = "alsa_output.device.monitor"
microphoneDevice = "alsa_input.device"
```

\
If using Google Cloud Speech API, create a project in Google Cloud Console, enable the Cloud Speech-To-Text API, then create a service account and create a key. Download the JSON file and copy its contents to GOOGLE_CLOUD_SPEECH_CREDENTIALS:
```python
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""YOUR JSON FILE CONTENTS HERE"""
```

Be aware that with the Google API only 60 minutes of listening are free of charge.

\
To use CMU Sphinx instead of Google's API, replace
```python
text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, language='en-GB')
```
with
```python
text = r.recognize_sphinx(audio)
```

\
To set the words the program will listen for, edit the word list in meetplay.py:
```python
# word list to listen for
wordList = ["example", "test", "words"]
```

\
For further information, read the comments in meetplay.py.
