
# coding: utf-8

# # Web Scrapping 
# 
# Practicing Web Scraping with University of California Web Page's Legislative Reports 

# In[6]:


from bs4 import BeautifulSoup
import requests


# In[7]:


import pandas as pd
from pandas import Series, DataFrame


# In[8]:


url = 'http://www.ucop.edu/operating-budget/budgets-and-reports/legislative-reports/2017-18-legislative-session.html'


# In[10]:


#Requesting content from the web page 
result = requests.get(url)
cont = result.content

#Setting up as a Beautiful Soup Object
bSoup = BeautifulSoup(cont, "lxml")


# In[12]:


# After inspecting  
result = bSoup.find("div",{'class':'list-land', 'id':'content'})

#Finding the tables in HTML
tables = result.find_all('table')


# In[16]:


#Data List
data = []

#since <tr> defines a row in html, set rows as based on whenever a <tr> is found
rows = tables[0].findAll('tr')

#Grab every HTML cell in each row

for tr in rows:
    cols = tr.findAll('td')
    #Check to see if text is in row 
    for td in cols:
        text = td.find(text = True)
        data.append(text)
        print text



# In[25]:


#Setting up empty lists
reports = []
date = []
#Setting index counter
index = 0
for item in data:
#     print item
    if item and "pdf" in item:
        #Adding the date and reports
        date.append(data[index-1])
        #To avoid unicode errors: https://stackoverflow.com/questions/10993612/python-removing-xa0-from-string
        reports.append(item.replace(u'\xa0',u' '))
        
    index += 1


# In[27]:


date = Series(date)
reports = Series(reports)
legislative_df = pd.concat([date,reports],axis=1)


# In[28]:


legislative_df.columns = ['Date', 'Reports']


# In[30]:


legislative_df[1:]

