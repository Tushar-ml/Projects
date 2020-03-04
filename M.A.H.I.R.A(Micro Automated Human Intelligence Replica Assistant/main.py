from gtts import gTTS
from googletrans import Translator
import speech_recognition as sr 
from face_recognition_system import Face_Recognition 
import time
from selenium import webdriver
import pyautogui
import os
import cv2
from playsound import playsound

#enter the name of usb microphone that you found 
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
        r.adjust_for_ambient_noise(source) 
        
        #listens for the user's input 
        audio = r.listen(source) 
              
        try: 
            text = r.recognize_google(audio) 
        except sr.UnknownValueError: 
                text = 'Not recognized'
                          
        except sr.RequestError as e: 
                print('Speak Again')
                jarvis()
    return text
def Open_Camera():
      name = Face_Recognition()
      if name=='Tushar':
          print('Welcome {}'.format(name))
          
print('Say Something')
with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                        chunk_size = chunk_size) as source: 
    #wait for a second to let the recognizer adjust the  
    #energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source) 
        
        #listens for the user's input 
        audio = r.listen(source) 
              
        try: 
            text = r.recognize_google(audio) 
            print ("you said: " + text)
            if text.lower() == 'start':
                '''speech = gTTS(text = 'Hi Tushar How could i help you', lang = 'en', slow = False)
                
                speech.save('reply.mp3')
                playsound('reply.mp3')'''
                
                while True:
                    with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                                        chunk_size = chunk_size) as source: 
                    #wait for a second to let the recognizer adjust the  
                    #energy threshold based on the surrounding noise level 
                        r.adjust_for_ambient_noise(source) 
                        
                        #listens for the user's input 
                        audio = r.listen(source)
                              
                        try: 
                            text = r.recognize_google(audio) 
                            print ("you said: " + text)
                            
                            word = text.split()
                            if word[0].lower() == 'open' and word[1].lower() == 'firefox':
                                print(word)
                                search_words = word[4:]
                                os.system('start firefox.exe')
                                time.sleep(10)
                                a = ''
                                for i in range(len(search_words)):
                                    a = a+' '+search_words[i]
                                try:
                                        
                                            time.sleep(2)
                                            pyautogui.hotkey('ctrl','k')
                                            pyautogui.typewrite(a)
                                            pyautogui.press('enter')
                                except TimeoutException:
                                        print ("Loading took too much time!")
                                    
                            if text.lower() == 'open camera':
                                print('Opening the Web Camera')
                                Open_Camera()
                              
                            if text=='stop':
                                print('Stopping Procedure')
                                break
                                    
                            '''translator = Translator()
                        
                            translated = translator.translate(str(text),src='en',dest='hi')
                        
                            tts = gTTS(text='Successfully Stopped', lang='hi')
                            tts.save("good.mp3")
                            from playsound import playsound
                            playsound('good.mp3')'''
                      
                    #error occurs when google could not understand what was said 
                      
                        except sr.UnknownValueError: 
                            continue
                          
                        except sr.RequestError as e: 
                            continue
            else:
                print("Invalid Command")
        except sr.UnknownValueError: 
                print("Not Recognized")
                          
        except sr.RequestError as e: 
                print('Not Recognized')