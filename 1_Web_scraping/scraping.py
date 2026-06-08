import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

headers= {'User-Agent': 'Mozilla/5.0'}  

# Websites like AmbitionBox block bots
#  Adding User-Agent makes it look like a browser

url="https://www.ambitionbox.com/list-of-companies?page=1"

response=requests.get(url, headers=headers)

soup=BeautifulSoup(response.text,'html.parser')
#print(Soup.prettify())   # it will format your Html code taki tum usko samjh pao 

print(soup.find_all('h1')[0].text)  #Here we are Extracting from h1 Tag 

# print(soup.find_all('h2'))

# now Printing all the company names from h2 Tag

for i in soup.find_all('h2'):
    print(i.text.strip())   # Strip will eliminate the strip bw the companies names 


for i in soup.find_all('div',class_='rating_text'):
                       print(i.text.strip())

for i in soup.find_all('a',class_='companyCardWrapper_Action_Count'):
                       print(i.text.strip())



company= soup.find_all('div', class_='companyCardWrapper')
print(len(company))

name=[]
rating=[]
reviews = []
salaries = []
interviews = []
jobs = []
benefits = []
photos = []
for i in company:
        name.append(i.find('h2').text.strip())
        rating.append(i.find_all('div',class_='rating_text')[0].text.strip())

        # all counts
        counts = i.find_all('span', class_='companyCardWrapper__ActionCount')
        
        # assign by index (fixed order)
        reviews.append(counts[0].text.strip() )
        salaries.append(counts[1].text.strip())
        interviews.append(counts[2].text.strip())
        jobs.append(counts[3].text.strip() )
        benefits.append(counts[4].text.strip())
        photos.append(counts[5].text.strip())

d={'name':name,'rating':rating,'reviews':reviews,'salaries':salaries,'interviews':interviews,'jobs':jobs,'benifits':benefits,'photos':photos}
df=pd.DataFrame(d)
print(df)
#------------------------------------------------------------------------------------------------------------------------------------------------------

final=pd.DataFrame()

for j in range(1,30):
        headers= {'User-Agent': 'Mozilla/5.0'} 
        url="https://www.ambitionbox.com/list-of-companies?page={}".format(j)

        response=requests.get(url, headers=headers)

        soup=BeautifulSoup(response.text,'html.parser')

        company= soup.find_all('div', class_='companyCardWrapper')
        print(len(company))

        name=[]
        rating=[]
        reviews = []
        salaries = []
        interviews = []
        jobs = []
        benefits = []
        photos = []
        for i in company:
                name.append(i.find('h2').text.strip())
                rating.append(i.find_all('div',class_='rating_text')[0].text.strip())

                # all counts
                counts = i.find_all('span', class_='companyCardWrapper__ActionCount')
                
                # assign by index (fixed order)
                reviews.append(counts[0].text.strip() )
                salaries.append(counts[1].text.strip())
                interviews.append(counts[2].text.strip())
                jobs.append(counts[3].text.strip() )
                benefits.append(counts[4].text.strip())
                photos.append(counts[5].text.strip())

        d={'name':name,'rating':rating,'reviews':reviews,'salaries':salaries,'interviews':interviews,'jobs':jobs,'benifits':benefits,'photos':photos}
        df=pd.DataFrame(d)
        final = pd.concat([final, df], ignore_index=True)
        time.sleep(2)

print(final)