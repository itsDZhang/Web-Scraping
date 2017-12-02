
# Web Scrapping 

Practicing Web Scraping with University of California Web Page's Legislative Reports 


```python
from bs4 import BeautifulSoup
import requests
```


```python
import pandas as pd
from pandas import Series, DataFrame
```


```python
url = 'http://www.ucop.edu/operating-budget/budgets-and-reports/legislative-reports/2017-18-legislative-session.html'
```


```python
#Requesting content from the web page 
result = requests.get(url)
cont = result.content

#Setting up as a Beautiful Soup Object
bSoup = BeautifulSoup(cont, "lxml")
```


```python
# After inspecting  
result = bSoup.find("div",{'class':'list-land', 'id':'content'})

#Finding the tables in HTML
tables = result.find_all('table')
```


```python
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


```

    1.
    09/01/17
    2018-19 (EDU 92493 - 92496-2017) Capital Expenditures
    2.
    09/01/17
    9th Amended List of Proposed Energy Projects
    3.
    (in 2018)
    Expenditures for Instruction (biennial) (pdf)
    4.
    11/01/17
    Instruction and Research Space Summary & Analysis (pdf)
    5.
    11/01/17
    Utilization of Classroom and Teaching Laboratories (biennial) (pdf)
    6.
    11/01/17
    Five Year Capital Outlay Plan for State Funds (Capital Financial Plan 2017-27) (pdf)
    7.
    11/30/17
    Innovation and Entrepreneurship Expansion (pdf)
    8.
    11/30/17
    Number of Pupils who Attended a LCFF School: # Admitted to UC, and Enrollment disaggregated by Campus (pdf)
    9.
    12/01/17
    Use of One-time Funds to Support Best Practices in Equal Employment Opportunity in Faculty Employment (pdf)
    10.
    12/01/17
    
    
    11.
    12/01/17
    Project Savings Funded from Capital Outlay Bond Funds (pdf)
    12.
    12/01/17
    Streamlined Capital Projects Funded from Capital (pdf)
    13.
    12/31/17
    Firearm-related Violence Research (pdf)
    14.
    1/01/18
    Contracts with Medical Laboratories
    15.
    01/01/18
    Annual General Obligation Bonds Accountability (pdf)
    16.
    01/01/18
    Small Business Utilization (pdf)
    17.
    01/10/18
    Institutional Financial Aid Programs - Preliminary (pdf)
    18.
    01/10/18
    Summer Enrollment (pdf)
    19.
    01/15/18
    Contracting Out for Services at Newly Developed Facilities (pdf)
    20.
    02/01/18
    Capital Expenditures Progress Report (EDU 92493 - 92496-2017) (pdf)
    21.
    02/01/18
    Statewide Energy Projects (SEP) - Progress (pdf)
    22.
    02/01/18
    Working Families Student Fee Transparency and Accountability Act (pdf)
    23.
    03/01/18
    Student Transfers (pdf)
    24.
    03/01/18
    Entry Level Writing Requirement (ELWR) (pdf)
    25.
    03/15/18
    Performance Outcome Measures (pdf)
    26.
    03/31/18
    Annual Student Financial Support (pdf)
    27.
    04/01/18
    Unique Statewide Pupil Identifier (pdf)
    28.
    05/15/18
    Receipt and Use of Lottery Funds (pdf)
    29.
    TBD
    Draft Long Range Development Plan (LRDP) and LRDP EIR (pdf)
     
    Future Reports
    None
    30.
    09/01/18
    2019-20 (EDU 92493 - 92496-2017) Capital Expenditures (pdf)
    31.
    09/01/18
    10th Amended List of Proposed Energy Projects (pdf)
    32.
    09/01/18
    Support Services/College Readiness (pdf)
    33.
    10/1/18
    Expenditures for Istruction (biennial) (pdf)
    34.
    11/01/18
    Instruction and Research Space Summary and Analysis (pdf)
    35.
    11/01/18
    Utilization of Classroom and Teaching Laboratories (biennial) (pdf)
    36.
    11-30-18
    Five Year Capital Outlay Plan for State Funds (Capital Financial Plan 2018-28) (pdf)
    37.
    12-31-20
    Breast Cancer Research Program (pdf)
    38.
    12-31-20
    Cigarette and Tobacco Products Surtax Research Program (pdf)
    39.
    01-01-21
    California Subject Matter Programs (CSMP) (pdf)
    40.
    04-01-21
    California State Summer School for Mathematics and Science (COSMOS) Program Outcomes (pdf)



```python
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

```


```python
date = Series(date)
reports = Series(reports)
legislative_df = pd.concat([date,reports],axis=1)
```


```python
legislative_df.columns = ['Date', 'Reports']
```


```python
legislative_df[1:]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Reports</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>11/01/17</td>
      <td>Instruction and Research Space Summary &amp; Analy...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11/01/17</td>
      <td>Utilization of Classroom and Teaching Laborato...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11/01/17</td>
      <td>Five Year Capital Outlay Plan for State Funds ...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11/30/17</td>
      <td>Innovation and Entrepreneurship Expansion (pdf)</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11/30/17</td>
      <td>Number of Pupils who Attended a LCFF School: #...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>12/01/17</td>
      <td>Use of One-time Funds to Support Best Practice...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>12/01/17</td>
      <td>Project Savings Funded from Capital Outlay Bon...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>12/01/17</td>
      <td>Streamlined Capital Projects Funded from Capit...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>12/31/17</td>
      <td>Firearm-related Violence Research (pdf)</td>
    </tr>
    <tr>
      <th>10</th>
      <td>01/01/18</td>
      <td>Annual General Obligation Bonds Accountability...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>01/01/18</td>
      <td>Small Business Utilization (pdf)</td>
    </tr>
    <tr>
      <th>12</th>
      <td>01/10/18</td>
      <td>Institutional Financial Aid Programs - Prelimi...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>01/10/18</td>
      <td>Summer Enrollment (pdf)</td>
    </tr>
    <tr>
      <th>14</th>
      <td>01/15/18</td>
      <td>Contracting Out for Services at Newly Develope...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>02/01/18</td>
      <td>Capital Expenditures Progress Report (EDU 9249...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>02/01/18</td>
      <td>Statewide Energy Projects (SEP) - Progress (pdf)</td>
    </tr>
    <tr>
      <th>17</th>
      <td>02/01/18</td>
      <td>Working Families Student Fee Transparency and ...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>03/01/18</td>
      <td>Student Transfers (pdf)</td>
    </tr>
    <tr>
      <th>19</th>
      <td>03/01/18</td>
      <td>Entry Level Writing Requirement (ELWR) (pdf)</td>
    </tr>
    <tr>
      <th>20</th>
      <td>03/15/18</td>
      <td>Performance Outcome Measures (pdf)</td>
    </tr>
    <tr>
      <th>21</th>
      <td>03/31/18</td>
      <td>Annual Student Financial Support (pdf)</td>
    </tr>
    <tr>
      <th>22</th>
      <td>04/01/18</td>
      <td>Unique Statewide Pupil Identifier (pdf)</td>
    </tr>
    <tr>
      <th>23</th>
      <td>05/15/18</td>
      <td>Receipt and Use of Lottery Funds (pdf)</td>
    </tr>
    <tr>
      <th>24</th>
      <td>TBD</td>
      <td>Draft Long Range Development Plan (LRDP) and L...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>09/01/18</td>
      <td>2019-20 (EDU 92493 - 92496-2017) Capital Expen...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>09/01/18</td>
      <td>10th Amended List of Proposed Energy Projects ...</td>
    </tr>
    <tr>
      <th>27</th>
      <td>09/01/18</td>
      <td>Support Services/College Readiness (pdf)</td>
    </tr>
    <tr>
      <th>28</th>
      <td>10/1/18</td>
      <td>Expenditures for Istruction (biennial) (pdf)</td>
    </tr>
    <tr>
      <th>29</th>
      <td>11/01/18</td>
      <td>Instruction and Research Space Summary and Ana...</td>
    </tr>
    <tr>
      <th>30</th>
      <td>11/01/18</td>
      <td>Utilization of Classroom and Teaching Laborato...</td>
    </tr>
    <tr>
      <th>31</th>
      <td>11-30-18</td>
      <td>Five Year Capital Outlay Plan for State Funds ...</td>
    </tr>
    <tr>
      <th>32</th>
      <td>12-31-20</td>
      <td>Breast Cancer Research Program (pdf)</td>
    </tr>
    <tr>
      <th>33</th>
      <td>12-31-20</td>
      <td>Cigarette and Tobacco Products Surtax Research...</td>
    </tr>
    <tr>
      <th>34</th>
      <td>01-01-21</td>
      <td>California Subject Matter Programs (CSMP) (pdf)</td>
    </tr>
    <tr>
      <th>35</th>
      <td>04-01-21</td>
      <td>California State Summer School for Mathematics...</td>
    </tr>
  </tbody>
</table>
</div>


