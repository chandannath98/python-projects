import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import urllib.request
import re


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good Evaning")
    speak("I am Friday How can i help you sir")

def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("I did'nt reconize what you said can you say it again please")  
        speak("I did'nt reconize what you said can you say it again please")
        return "None"
    return query

def googlesearch(query):
    url = "https://www.google.co.in/search?q=" +(str(query))+ "&oq="+(str(query))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
    speak(f"Showing search result of {query} in google")
    webbrowser.open_new(url)

def calculation():
    while True:
                print("What you want to do:- addition, subtract, multipication or division")
                speak("What you want to do:- addition, subtract, multipication or division")
                action=takecommand().lower()

            

                if "addition" in action:
                    print("What is first number")
                    speak("What is first number")
                    number1=int(takecommand())
                    print("What is second number")
                    speak("What is second number")
                    number2=int(takecommand())
                    result=number1+number2
                    print(f"The result is {result}")
                    speak(f"The result is {result}")
                elif "subtract" in action:
                    print("What is first number")
                    speak("What is first number")
                    number1=int(takecommand())
                    print("What is second number")
                    speak("What is second number")
                    number2=int(takecommand())
                    result=number1-number2
                    print(f"The result is {result}")
                    speak(f"The result is {result}")
                elif "multiplication" in action:
                    print("What is first number")
                    speak("What is first number")
                    number1=int(takecommand())
                    print("What is second number")
                    speak("What is second number")
                    number2=int(takecommand())
                    result=number1*number2
                    print(f"The result is {result}")
                    speak(f"The result is {result}")
                elif "division" in action:
                    print("What is first number")
                    speak("What is first number")
                    number1=int(takecommand())
                    print("What is second number")
                    speak("What is second number")
                    number2=int(takecommand())
                    result=number1/number2
                    print(f"The result is {result}")
                    speak(f"The result is {result}")

                elif "stop" in action:
                    break
                else:
                    print("Did'nt reconized can you say it again")


if __name__=="__main__":
    wishme()
    
    while True:
        query=takecommand().lower()
        if "wikipedia" in query:
            try:
                query=query.replace("wikipedia"," ")
                print(query)
                result=wikipedia.summary(query,sentences=2)
                print(result)
                speak(result)
            except:
                googlesearch()
        

        elif ("who are you" in query) or ("what is yor name" in query):
            speak(f" My name is friday and i am your assistent")


        elif "time" in query: 
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")



        elif "google" in query:
            query=query.replace("google"," ")
            if "search" in query:
                query=query.replace("search"," ")
            if "in" in query:
                query=query.replace("in"," ")
            googlesearch(query)



        elif "play music" in query:
            url = "https://www.youtube.com/watch?v=JlgkMXex2DI&list=TLPQMjgwMTIwMjHIzKvY4560Eg&index=2"
            speak("Ok Playing music")
            webbrowser.open_new(url)

        elif "what can you do" in query:
            speak("You can say: play music,play news, search in google etc.")
        
        elif "none" in query:
            continue



        elif "play" in query:
            query=query.replace("play"," ")
            query=query.replace("youtube"," ")
            # if "in" in query:
            #     # query=query.replace("in"," ")
            # if "on" in query:
            #     query=query.replace("on"," ")
            l=query.split()
            word=""
            for i in l:
                word=word+i+"_"
            try:
                search_keyword=word
                html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                speak(f"Ok Playing {query} on youtube")
                webbrowser.open_new("https://www.youtube.com/watch?v=" + video_ids[0])
            except:
                googlesearch(query)



        elif "play news" in query:
            from newss import news2
            l=[]
            speak(news2(l))

        # elif "code" in query:
            

        elif "stop" in query:
            speak("Ok bye bye")
            break

        elif "who i am" in query:
            speak("You are my boss chandan nath")

        elif "calculation" in query:
            calculation()
                    


        else: 
            googlesearch(query)
        
