import win32com.client      
def textToSpeech(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice") 
    speaker.Speak(text) 

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
def responce(df, predict):
    vectorizer = CountVectorizer()
    x = vectorizer.fit_transform(df["quest"])
    y = df["ans"]
    classifier = LogisticRegression(random_state=0, solver="liblinear", multi_class="auto")
    classifier.fit(x,y)
    predict = vectorizer.transform([predict])
    prediction = classifier.predict(predict)
    print(prediction[0])
    textToSpeech(prediction[0])

import sys
def processing(chatbot, products, conversation):
    if chatbot["quest"].str.contains(conversation).any():
        responce(chatbot, conversation)
    elif products["PRODUCT NAME"].str.contains(conversation).any():
        options = list(products[products["PRODUCT NAME"].str.contains(conversation)]["PRODUCT NAME"].head(10))
        if(len(options) > 1):
            print(options)
            textToSpeech("would you like to have")
            textToSpeech(options)
        else:
            print("Okey, "+conversation+" is added to your cart...")
            textToSpeech("Okey,"+conversation+"is added to your cart...")
    elif conversation == "bye" or  conversation == "thank you":
        textToSpeech("Thank You Have a great Day")
        sys.exit("Thank You Have a great Day")
    else:
        print("I didnot get that can you please repeate")
        textToSpeech("I didnot get that can you please repeate")
    
import speech_recognition as sr
def speechToText(chatbot, products):
    r = sr.Recognizer()  
    try: 
        with sr.Microphone() as source2: 
            r.adjust_for_ambient_noise(source2, duration=0.2) 
            print("How may I assist you?")
            audio2 = r.listen(source2) 
            print("Your Request is been processed...")
            textToSpeech("Your Request is been processed...") 
            global conversation
            conversation = r.recognize_google(audio2) 
            conversation = conversation.lower() 
            print(conversation) 
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
        conversation = input("please type Your Request: ")
    except sr.UnknownValueError: 
        print("unknown error occured")
        conversation = input("please type Your Request: ")
    processing(chatbot, products, conversation)

import numpy as np
import pandas as pd
#int main(void)
# Driver Code 
if __name__ == '__main__':
    chatbot = pd.read_csv("data.csv")
    #print(chatbot)
    products = pd.read_csv("product_dataset.csv")
    products = products.sort_values('PRODUCT NAME')
    col1 = products["SALES"].astype(str) 
    col2 = products["RATING"].astype(str)
    products['Rank'] = (col1+col2).astype(int).rank(method='dense', ascending=False).astype(int)
    products = products.sort_values('Rank')
    #print(products.head(20))
    print("Welcome to Search Assistent. Your finding is just one voice away")
    textToSpeech("Welcome to Search Assistent.")
    textToSpeech("How may I help you?")
    while(True):
        speechToText(chatbot,products)
