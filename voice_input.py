# Python program to translate speech to text and text to speech

import speech_recognition as sr 
import speak as spk

#function to return spoken text

def get_speech():
    # Initialize the recognizer 
    r = sr.Recognizer() 

    # Loop infinitely for user to speak 

    while(1):	 
            
            # Exception handling to handle exceptions at the runtime 
            try: 	
                    # use the microphone as source for input. 
                    with sr.Microphone() as source2:
                            
                            # wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level 
                            r.adjust_for_ambient_noise(source2, duration=0.2) 
                            print("taking input...")
                            
                            #listens for the user's input 
                            audio2 = r.listen(source2)                            
                            
                            # Using ggogle to recognize audio 
                            MyText = r.recognize_google(audio2) 
                            MyText = MyText.lower()                                                         
                            return MyText
                            
            except sr.RequestError as e:
                    spk.speak("sorry could not connect to the server")
                    print("Could not request results; {0}".format(e)) 
                    
            except sr.UnknownValueError:
                    spk.speak("sorry could not hear you")
                    print("plz speak again")    
