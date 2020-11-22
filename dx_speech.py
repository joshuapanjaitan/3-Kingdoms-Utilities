import speech_recognition as sr
import time
t = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
     'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'free': 3, 'tree': 3, '1': 1, '2': 2, '5': 5, '6': 6, '7': 7, '8': 8,
     '9': 9, 'time': 10, 'full': 4, 'pool': 4, 'sweet': 3, 'for': 4, 'to': 2, 'AIDS': 8, 'a': 8, '10': 10}
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Speak anything: ')
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        if len(text) == 1:
            print(text)
        else:
            print(t[text])
    except:
        print('Sorry could not recogonize your voice')
        print(t[text])
