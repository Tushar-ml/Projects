import pyttsx3
from googletrans import Translator
import speech_recognition as sr 
from face_recognition_system import Face_Recognition 
import time
from selenium import webdriver
import pyautogui
import os
import cv2
from playsound import playsound
import datetime
import wikipedia
import webbrowser
import keyboard
#enter the name of u
# sb microphone that you found 
#using lsusb 
#the following name is only used as an example 
mic_name = 'Microsoft Sound Mapper - Input'
#Sample rate is how often values are recorded 
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data) 
#here.  
#it is advisable to use powers of 2 such as 1024 or 2048 
chunk_size = 2048
#Initialize the recognizer 
r = sr.Recognizer() 

#generate a list of all audio cards/microphones 
mic_list = sr.Microphone.list_microphone_names() 
  
#the following loop aims to set the device ID of the mic that 
#we specifically want to use to avoid ambiguity. 
for i, microphone_name in enumerate(mic_list): 
    if microphone_name == mic_name: 
        device_id = i 
  
#use the microphone as source for input. Here, we also specify  
#which device ID to specifically look for incase the microphone  
#is not working, an error will pop up saying "device_id undefined" 
def jarvis():
    with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                        chunk_size = chunk_size) as source: 
    #wait for a second to let the recognizer adjust the  
    #energy threshold based on the surrounding noise level 
        # print("Speak to Search")
        r.energy_threshold = 300
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source) 
        
        #listens for the user's input 
        audio = r.listen(source) 
              
        try: 
            text = r.recognize_google(audio)
            print('You said : {}'.format(text))
            text = text.lower()
            return text
        except sr.UnknownValueError: 
                
                print('Speak again')
                jarvis()
        except sr.RequestError as e: 
                print('Speak Again')
                jarvis()
                
    

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate',150)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe(author):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning {} Sir'.format(author))
    elif hour>=12 and hour<16:
        speak('Good Afternoon {} Sir'.format(author))
    else:
        speak('Good Evening {} Sir'.format(author))
            

def Open_Camera():
    cap = cv2.VideoCapture(0)
    while True:
        _,frame = cap.read()
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    
          
print('Say Something')
if __name__=='__main__':
                        #
                        # wishMe('Tushar')
                        speak('Welcome')
                        speak('Wait for a Moment , Identifying you , will not take a minute ')
                            
                        name = Face_Recognition()
                        if name=='Tushar':
                              wishMe(name)
                              speak('What can i do for you Sir')
                              while True:
                                
                                text = jarvis()
                                
                               
                                
                                try:
                                    if 'entertain' or 'bored' or 'tired' in text:
                                        speak("what would you like to have Sir: Listening Music or Watching Videos")
                                        entertain_text = jarvis()
                                        if 'video' or 'videos' or 'watching videos' in entertain_text:
                                            speak('Opening Youtube')
                                            webbrowser.open('www.youtube.com')
                                            speak('Waiting for the youtube to load')
                                            time.sleep(15)
                                            speak('What you would you like to Tushar Sir')
                                            search_text = jarvis()
                                            if search_text:
                                                pyautogui.press('tab')
                                                keyboard.write(str(search_text))
                                    
                                    if 'open' and 'camera' in text:
                                        print('Opening the Web Camera')
                                        speak('Opening the Camera')
                                        Open_Camera()
                                      
                                    if 'stop' in text:
                                        print('Stopping Procedure')
                                        speak('Successfully Stopped. Have a Good day Sir')
                                        break
                                    if 'translate' in text:
                                        speak('What to Translate Sir')
                                        translated_speech = jarvis()
                                        translator = Translator()
                                    
                                        translated = translator.translate(translated_speech,src='hi',dest='en')
                                        trans = str(translated.text)
                                        speak(trans)
                                  
                                except:
                                    speak('Having Some Problem')
                                    speak('Sorry for the Inconvienence')
                        else:
                            speak('Access Denied')
                            
                          
                 
