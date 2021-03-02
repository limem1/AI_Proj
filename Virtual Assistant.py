import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

warnings.filterwarnings('ignore')

def recordAudio():
    #Record
    r = sr.Recognizer()
     #open micro
    with sr.Microphone as source :
        print("Say Something!")
        audio = r.listen(source)
    #usegoogle
    data = ''
    try:
         data = r.recognize_google(audio)
         print('You said : {} '.format(data))
    except sr.UnknownValueError:
        print('Google speech Recognition could not understand the audio,unknown Error')
    except sr.RequestError as e :
        print('Request resultat from Google speech Recognition service error'+e)
    return  data


def assistantResponse(text):
    print(text)
    #convert the text to speech
    myobj = gTTS(text= text, lang='en',slow=False)
    # save the converted audio to a file
    myobj.save('assistant_response.mp3')
    # play the converted file
    os.system('start assistant_response.mp3')

#it's working for now
#okay let's move on
# a function for wake words
def wakeWord(text):
     Wake_WORD = ['hey computer',"okay compteur"]

     text = text.lower() #low case words
     for i in Wake_WORD :
         if i in text:
             return True

     return False
# Ask for date
def askdate():

    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthnum = now.month
    daynum = now.day

    month_names = ['January','February','March','April','May','June','July','August','September','October','November','December']
    days_numbers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']

    return 'Today is '  + weekday + ' ' + month_names [ monthnum - 1 ] +  ' The '  + days_numbers [ daynum - 1] + '.'


#alles gut bro haha
# we have to return greeting
def greeting(text):

    INPUTS = ['hi','hey','hello','hallo',"what's up "]
    RESPONSES = [" Hey,How are you ? ", "Hello" , "Hey There", "Hey, How was your day ? "]
    for j in text.split():
        if j in INPUTS :
            return random.choice(RESPONSES) + '.'

    return ' '

def askperson (text) :
    wordlist = text.split()
    for w in range(0, len(wordlist)):
        if w + 3 <= (len(wordlist) - 1 ) and wordlist[w].lower() == 'who' and wordlist[w+1].lower() == 'is' :
            return wordlist[w+2] +' ' + wordlist[w+3]
while True :
    text = recordAudio()
    response = ''
    if (wakeWord(text) == True) :
        print('You said the wake word or phrase')
        response = response + greeting(text)

        if ('date' in text ) :
            ask_date = askdate()
            response = response + ' '+ ask_date

        if ('who is 'in text) :
            person = askperson()
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

        assistantResponse(response)
