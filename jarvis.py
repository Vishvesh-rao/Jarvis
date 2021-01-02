
############-MODULES-##############

import speech_recognition as sr
import pyautogui as pygui
from datetime import *
import subprocess as s
import urllib.request
from gtts import gTTS 
import pyttsx3
import time
import os 
from Crypto.Util.number import getPrime

##################################


############-SET GLOBAL VARIABLES-##########adity

date = datetime.now()
r = sr.Recognizer()
r.energy_threshold = 400
engine = pyttsx3.init()
repeat = 0

#-------------------------------------------------------------------------------------------------------
#-DEFINING FUNCTIONS

def check_connectivity():
    try:
        wp = urllib.request.urlopen("http://google.com")
        return True
    except Exception as e:
        return False

def tts_voice1(mesg):
    language = 'en'
    myobj = gTTS(text=mesg, lang=language, slow=False) 
      
    myobj.save("speech.mp3") 
    os.system("mpg321 speech.mp3") 
    os.system('rm speech.mp3')

def tts_voice2(mesg):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[17].id)  # changes the voice
    engine.say(mesg)
    engine.runAndWait()

def notify(title,content):
    s.call(['notify-send',title,content])

#-------------------------------------------------------------------------------------------------------
######-START SPEECH RECOGNITION

while 1:
    with sr.Microphone() as source:

        if(not check_connectivity() and repeat == 0):
            
            tts_voice2("Sir I am offline")
            tts_voice2("Please check network connectivity")
            
            if repeat and repeat < 3:
                notify('Jarvis','Trying to re-establish connection')
            else:    
                notify('Jarvis','Net connectivity lost')
            
            repeat += 1
            
        else:
            if repeat>0:
                notify("Jarvis",'Connection Re-established!!')
            repeat = 0
        
        
        error = 0
        os.system("( speaker-test -t sine -f 10 )& pid=$! ; sleep 0.1s ; kill -9 $pid")
        os.system("clear")
        print("Talk...")
        
        try:
            audio_text = r.listen(source,timeout=3, phrase_time_limit=6)
            print("Time over, thanks")
        except:
            print("listening timed out while waiting for phrase to start")
            os.system("( speaker-test -t sine -f 100 )& pid=$! ; sleep 0.1s ; kill -9 $pid")
            
        os.system('clear')
        
        try:
            print("converting to text......")
            text = r.recognize_google(audio_text) 
            text = text.lower()
            print("Text: "+text)
            
            if text.startswith("go"):
                text = text[3:]
                print("go found")
                print(text)
                tts_voice1(text)
        
        except:
            print("Sorry, I did not get that")
            # tts_voice1("Sorry, I did not get that")
            error = 1
        
        if error:
            continue

        if 'hai' in text or 'hi' in text:
            tts_voice1("hello")

        if "open" in text:
            print("opening "+str(text.split("open")[1][1:]))
        

	    ## opens gmail account on telling username assuming all the accounts passwords are stored on your browser
            if 'gmail' in text:

                tts_voice1("Which account")
                acoount_name = r.listen(source,timeout=3, phrase_time_limit=5)
                
                try:
                    print("converting to text......")
                    text = r.recognize_google(acoount_name) 
                    text = text.lower()
                except:
                    print("Sorry, I did not get that")

                if "v" in text:
                    print("""ACCOUNT NAME: "ENTER ACCOUNT 1 USERNAME" """)
                    os.system("chrome https://mail.google.com/mail/u/2/#inbox")
            
                elif "d" in text:
                    print("""ACCOUNT NAME: "ENTER ACCOUNT 2 USERNAME" """)
                    os.system("chrome https://mail.google.com/mail/u/1/#inbox")

                else:
                    os.system("chrome https://mail.google.com/mail/u/0/#inbox")
            
            if 'gh' in text or 'github' in text:
                tts_voice1("opening github")
                print("opening github")
                os.system("chrome https://github.com/Vishvesh-rao")

#---------------------------------------------------------------------------
    
        if "start" in text:
            print("starting "+str(text.split("start")[1][1:]))

            if str(text.split("start")[1][1:2]) == 's' or str(text.split("start")[1][1:2]) == 'c':
                tts_voice1("opening CTF time")
                print("opening CTF time")
                os.system("chrome ctftime.org")

            if str(text.split("start")[1][1:2]) == 'd' or str(text.split("start")[1][1:]) == 'discord':
                # tts_voice1("opening Discord")
                print("starting Discord")
                os.system("discord")

            if str(text.split("start")[1][1:2]) == 't' or str(text.split("start")[1][1:]) == 'teams':
                # tts_voice1("starting Microsoft Teams")
                print("starting Microsoft teams")
                os.system("teams")

#---------------------------------------------------------------------------

        if "dark mode" in text.lower() or "dark" in text.lower():  ## Need Dark reader extension for this functionality
            tts_voice1("toggling dark mode")
            pygui.press("alt"+"shift"+'d')
        if "close" in text.lower():                                ## Closes currently open tab on a browser
            tts_voice1("closing "+str(text.split("close")[1][1:]))
            pygui.hotkey('ctrl','w')
        if "lock" in text.lower():
            os.system("i3lock-fancy")
            tts_voice1("System unlocked")
        if "shutdown" in text:
            tts_voice1("Warning Shutting Down System")
            os.system("shutdown 0")
        
            
