# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 00:44:30 2022

@author: ogunb
"""
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open ('loan_data_json.json') as json_file:
    Data = json.load(json_file)

#Transform to dataframe
Loandata = pd.DataFrame(Data)

#Using exp to get annual income

Income = np.exp(Loandata['log.annual.inc'])

Loandata['Annualincome'] = Income

#Apply for-loops

lenght = len(Loandata)

ficocat = []
for x in range(0,lenght):
    category = Loandata['fico'][x]
    if category >= 300 and category < 400: 
        cat = 'Very Poor'
    elif category >= 400 and category < 600: 
        cat = 'Poor'
    elif category >= 601 and category < 660: 
        cat ='Fair'
    elif category >= 660 and category < 780: 
        cat = 'Good'
    elif category >=780: 
        cat = 'Excellent'   
    else:
        cat = 'Unknown'     
    ficocat.append(cat)  

ficocat = pd.Series(ficocat)

Loandata['Fico.category'] = ficocat

#df.loc as conditional statement

Loandata.loc[Loandata['int.rate']> 0.12, 'int.rate.type']= 'High'
Loandata.loc[Loandata['int.rate']<= 0.12, 'int.rate.type']= 'Low'


#Groupby Function and row count as No of loan for fico,category

#BARCHART
catplot = Loandata.groupby(['Fico.category']).size()
catplot.plot.bar( color = 'red',width =0.75)
plt.show()


#PIECHART
Purposecount = Loandata.groupby(['purpose']).size()
Purposecount.plot.pie ()
plt.show()

#scatter Plot

xpoint = Loandata['dti']
ypoint = Loandata['Annualincome']
plt.scatter(xpoint,ypoint, color = 'green')
plt.show()


#Export to Csv 

Loandata.to_csv('Loan_cleaned.csv', index = True)




