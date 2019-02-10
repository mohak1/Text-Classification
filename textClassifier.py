# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 03:51:30 2019

@author: Mohak

Text Classification for Akaike technologies

"""
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

path = 'G:\\Internships\\Akaike Technologies (NLP task)\\'

train = pd.read_csv(path+'train_data.csv')
label = pd.read_csv(path+'train_label.csv')
test = pd.read_csv(path+'test_data.csv')

catagories = set(label.iloc[:,1])

dic = {}
for i in range(len(catagories)):
    k = list(catagories)
    dic[k[i]] = []

#removing noise from the text
def filterT(text):
    filteredText=[]
    stop = set(stopwords.words('english'))
    stop.add(('the', 'x', 'this', 'use'))
    for i in range(len(text)):
        print(i)
        for w in word_tokenize(text):
            if w not in stop and w.isalpha():
                filteredText.append(w.lower())
    return set(filteredText)

#filtering the text
#adding the filtered text to respective index in the dict
l = label.iloc[:,1].tolist()
l_id = label.iloc[:,0].tolist()

#adding the tokens to respective dict index
for i in range(len(train.iloc[:33255,0])):
    text = train.iloc[i,0]
    t_id = train.iloc[i,1]
    lab = l[l_id.index(t_id)]
    #print(lab)
    filteredText = filterT(text)
    dic[lab].extend(list(filteredText))
    dic[lab] = list(set(dic[lab]))
    print("Iteration = ",i)
print('complete')

newList = list(dic.keys())

Y = newList

#getting data from dic to X
X = []
for i in range(len(Y)):
    X.append(dic[Y[i]])

#creating reverse dictionary of dic
finalDic = {}
for k,v in dic.items():
    for x in v:
        finalDic.setdefault(x,[]).append(k)

#Testing with a sentence
testSentence = 'These C-Channels are rectangular metal channels commonly used in door framing and wire protection or harnessing. Available in various sizes and materials. Popular materials include aluminum and plain steel. C-Channels can be cut to length making it very convenient for custom requirements. Cutting required if less than standard offered lengths are desired.California residents: see&nbsp;Proposition 65 information1-piece per packAluminum constructionAluminum finish3/8 in. W x 1/2 in. H x 96 in. L 1/16 in. thick'
testSentence = filterT(testSentence)
#dictionary is new_dic
#list is cat
#make sure cat[] is 0
def predict(testSentence):
    cat=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in testSentence:
        try:
            for s in finalDic[i]:
                if(s==newList[0]):
                    cat[0] +=1
                if(s==newList[1]):
                    cat[1] +=1
                if(s==newList[2]):
                    cat[2] +=1
                if(s==newList[3]):
                    cat[3] +=1
                if(s==newList[4]):
                    cat[4] +=1
                if(s==newList[5]):
                    cat[5] +=1
                if(s==newList[6]):
                    cat[6] +=1
                if(s==newList[7]):
                    cat[7] +=1
                if(s==newList[8]):
                    cat[8] +=1
                if(s==newList[9]):
                    cat[9] +=1
                if(s==newList[10]):
                    cat[10] +=1
                if(s==newList[11]):
                    cat[11] +=1
                if(s==newList[12]):
                    cat[12] +=1
                if(s==newList[13]):
                    cat[13] +=1
                if(s==newList[14]):
                    cat[14] +=1
        except:
            pass
    total = sum(cat)
    for i in range(len(cat)):
        cat[i] = cat[i]/total
    return cat
        
#predicting the test data and storing it in sample_submission
#convert res list values to probability 0-1    

#save the result in file sample_submission.csv
ss = pd.read_csv(path+'sample_submission.csv')
for i in range(len(test.iloc[:,0])):
    tID = test.iloc[i,1]
    text = test.iloc[i,0]
    t= filterT(text)
    res=predict(t)
    
    for j in range(len(ss.iloc[:,0])):
        if(ss.iloc[j,0]==tID):
            for k in range(0,15):
                ss.iloc[j,k+1] = res[k]
ss.to_csv('Submittion1.csv')