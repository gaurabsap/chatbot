
import openai
import time
import sys
import pyttsx3
import threading

def speak(text):
    eng = pyttsx3.init()
    voice = eng.getProperty('voices') 
    eng.setProperty('voice', voice[1].id)
    eng.say(text) 
    eng.runAndWait() 



def type_slowly(char, delay):
    for chars in char:
        sys.stdout.write(chars)
        sys.stdout.flush()
        time.sleep(float(delay))

def type_and_speak(msg):
    t1 = threading.Thread(target=type_slowly, args=(msg, 0.05))
    t2 = threading.Thread(target=speak, args=(msg,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

openai.api_key = "API_KEY"

while True:
    try:
        ask = input("\nAsk : ")
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt=ask,
          temperature=0.5,
          max_tokens=60,
          top_p=1.0,
          frequency_penalty=0.5,
          presence_penalty=0.0,
        )
        msg = response.choices[0].text
        type_and_speak(msg)
    except:
        print("Something unexpected happened!! try again")
