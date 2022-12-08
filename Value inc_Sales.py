# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 02:05:28 2022

@author: ogunb
"""
import pandas as pd
data = pd.read_csv ('transaction.csv')

Data = pd.read_csv ('transaction.csv',sep = ';')
data.info()

#Declare Variables

Costperitem = 11.73
Sellingpriceperitem = 21.11
Numberofitempurchased = 6
Profitperitem = Sellingpriceperitem - Costperitem


#Define Calculations

Costpertransaction = Costperitem * Numberofitempurchased 
Sellingpricepertransaction = Sellingpriceperitem * Numberofitempurchased
ProfitPertransaction = Profitperitem * Numberofitempurchased 

#Define Dataframe

Costperitem = Data['CostPerItem']
Numberofitempurchased = Data['NumberOfItemsPurchased']
Sellingpriceperitem = Data['SellingPricePerItem']

Costpertransaction = Costperitem * Numberofitempurchased
Sellingpricepertransaction = Sellingpriceperitem * Numberofitempurchased
Profitperitem = Sellingpriceperitem - Costperitem
ProfitPertransaction = Profitperitem * Numberofitempurchased 

#Create Column for calculation

Data['ProfitPertransaction'] = ProfitPertransaction

Data['Sellingpricepertransaction'] = Sellingpricepertransaction

Data['Costpertransaction'] = Costpertransaction

#Mark up profit/cost calculation & create Column

Data['Markup'] = round((ProfitPertransaction/Costpertransaction),2)
Data['%Markup'] = round(((ProfitPertransaction/Costpertransaction) * 100),2)

#Combine year,month and date concatenation

Myname ='Ibikunle' +'/' + 'Ogunbanwo'

# Change data type

Day = Data['Day'].astype(str)
print(Day.dtype)

Year = Data['Year'].astype(str)

TransactionDate = Day + '-' + Data['Month']+ '-' + Year

Data['TransactionDate '] = TransactionDate 

#View Specific Column

Data.iloc[0]
Data.iloc[0:3]
Data.iloc[-5:]

Data.head(5)

#Data cleaning with Split 

SplitKeyword = Data['ClientKeywords'].str.split (',' , expand = True)

#Create column for the Splitted Keyword

Data['Client Agegrade'] = SplitKeyword[0]
Data['Client Type'] = SplitKeyword[1]
Data['Length of Contract'] = SplitKeyword[1]

#Using the replace function

Data['Client Agegrade'] = Data['Client Agegrade'].str.replace('[', '')

Data['Length of Contract']= Data['Length of Contract'].str.replace(']', '')

#Change case to Lower Case 

Data['ItemDescription'] = Data['ItemDescription'].str.lower()

#Bring in new Dataset and merge 

Data_Season = pd.read_csv ('value_inc_seasons.csv', sep = ';')

Data = pd.merge(Data, Data_Season, on = 'Month')

#Drop Colum DF= Df.drop('Columname', axis =1)

Data = Data.drop('ClientKeywords', axis = 1)
Data = Data.drop('Day', axis = 1)
Data = Data.drop(['Month', 'Year'], axis = 1)

#Export to CSV 

Data.to_csv ('Value_inc_cleaned.csv', index = False)









