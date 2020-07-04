import numpy as np
import pandas as pd
df = pd.read_csv("data.csv")
#print(df)

df = df[["quest", "ans"]]
#print(df)

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(df["quest"])
y = df["ans"]

classifier = LogisticRegression(random_state=0, solver="liblinear", multi_class="auto")
classifier.fit(x,y)

predict = ["Hi"]
predict = vectorizer.transform(predict)
prediction = classifier.predict(predict)
print(prediction)


import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
    try:
        # using google speech recognition
        predict = [r.recognize_google(audio_text)]
        print("Text: "+predict)
    except:
        #global predict
        print("Sorry, I did not get that")
        predict = [input("please write input: ")]


predict = ["Banana"]

import numpy as np
import pandas as pd
df = pd.read_csv("product_dataset.csv")
df = df.sort_values('PRODUCT NAME')
#print(df.columns.values)
#print(df.head(20))
col1 = df["SALES"].astype(str) 
col2 = df["RATING"].astype(str)
df['Rank'] = (col1+col2).astype(int).rank(method='dense', ascending=False).astype(int)
df = df.sort_values('Rank')

#print(df.columns.values)
#print(df.head(20))

df.index = df["PRODUCT NAME"].astype(str)  
df = df.filter(like=predict[0], axis=0)
df = df.reset_index(drop=True)

print(df["PRODUCT NAME"])

import win32com.client 
  
speaker = win32com.client.Dispatch("SAPI.SpVoice") 

speaker.Speak(df["PRODUCT NAME"].astype(str) ) 



'''
#int main(void)
# Driver Code 
if __name__ == '__main__':
'''