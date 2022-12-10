# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 01:17:34 2022

@author: ogunb
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

Data = pd.read_excel('articles.xlsx')

#Summary of data
Data.describe()
#Column Summary
Data.info()

#Counting by source (No of article) with groupby function
Data.groupby(['source_id'])['article_id'].count()

#Count by engagement, GRoup by source (Publisher)
Data.groupby(['source_id'])['engagement_reaction_count'].sum()

#Drop a column
Data = Data.drop('engagement_comment_plugin_count', axis = 1)

# #Create Function
# def thisfunction():
#     print('My first attempt at function')
# thisfunction()

# #Create Function with variables
# def aboutme(name,surname,location):
#     print('This is '+name+' my surname is '+surname+' i am from '+location)
#     return name,surname,location

# a = aboutme('lexy', 'ayo', 'saskatoon')


# #Create Function with loops
# def favfood(food):
#     for x in food:
#         print('My top food is '+x)
        
# fastfood = ['Burgers', 'Pizzas', 'Pie', 'Salad', 'Water', 'Fruit']

# favfood(fastfood)

#Create a keyword Flag
#Keyword ='crash'
#Create For loop to isolate each title
# lenght = len(Data)
# Keyword_flag = []
# for x in range (0,lenght):
#     heading = Data['title'][x]
#     if Keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     Keyword_flag.append(flag)
    
#Create Function with keyword with try and accept

def Keywordflag(Keyword):
    lenght = len(Data)
    Keyword_flag = []
    for x in range (0,lenght):
        heading = Data['title'][x]
        try:
            if Keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        Keyword_flag.append(flag)    
    return Keyword_flag

Keywordflag = Keywordflag('murder')

#Create new column for the Flag

Data['Keyword_flag'] = pd.Series(Keywordflag)
 
#SentimentIntensityAnalyzer
sent_int = SentimentIntensityAnalyzer()
text = Data['title'][3]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#Loop through table to extract sentiment per title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

Lenght = len(Data)

for x in range (0,Lenght):
    try:
        text = Data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

Data['title_neg_sentiment'] = title_neg_sentiment
Data['title_pos_sentiment'] = title_pos_sentiment
Data['title_neu_sentiment'] = title_neu_sentiment

#Store as Data
Data.to_excel('blog_me_cleaned.xlsx', sheet_name='blogmedata', index= False)