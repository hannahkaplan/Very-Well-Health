#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[9]:


response = requests.get("https://www.verywellhealth.com/")
doc = BeautifulSoup(response.text, 'html.parser')


# In[10]:


doc


# In[105]:


stories = doc.select('.main')[0]
stories


# In[ ]:





# In[ ]:





# In[46]:


stories.select("span")[0].text.strip()


# In[103]:


stories.select(".block__title")[0].text.strip()


# In[84]:


stories.select_one(".block__content").get("data-kicker")


# In[58]:


stories.select_one("a").get('href')


# In[154]:


stories = doc.select(".comp.block.block")
rows =[]

for story in stories:
    print("---")
    row = {}
  
    row['title'] = story.select_one(".block__title").text.strip()
    row['category'] = story.select_one(".block__content").get("data-kicker")
    
    
    try:
        row['url'] = story.get('href')
    except:
        print("Couldn't find a link")
        

 
    rows.append(row)
    print(row)
print(rows)


# In[155]:


import pandas as pd


# In[156]:


df = pd.DataFrame(rows)
df


# In[157]:


df.to_csv("verywellhealth.csv")


# In[ ]:




