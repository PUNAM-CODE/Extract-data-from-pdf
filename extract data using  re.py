#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


txt='123aasdasd345435dsffd34324ADSDFDVFD'


# In[22]:


#Pattern=re.compile(r"123")
pattern=re.compile(r'\d{4}')


# In[23]:


matches=Pattern.finditer(txt)


# In[24]:


for match in matches:
    print(match)


# In[25]:


matches=re.finditer(r"123",txt)


# In[26]:


print(matches)


# In[27]:


matches=re.findall(r'123',txt)


# In[28]:


print(matches)


# In[29]:


txt1='232334SDFFDGRERGREGdfegrg heuuoGEUUO 1232-'


# In[34]:


#pattern=re.compile(r'[a-z]')
pattern=re.compile(r'\d{4}')


# In[35]:


matches=pattern.finditer(txt1)


# In[36]:


print(matches)


# In[37]:


for match in matches:
    print(match)


# In[38]:


date='2020.04.01 2020/08/11'


# In[42]:


#pattern=re.compile(r'\d\d\d\d.\d\d.\d\d')
pattern=re.compile(r'\d\d\d\d[-/]0[78][-/]\d\d')


# In[43]:


matches=pattern.finditer(date)


# In[44]:


for match in matches:
    print(match)


# In[76]:


condition='Mrs simpson Mrs Simpson Mr.Brown Ms Smith Mr.T  pythonengineer@gmai.com python-engineer@hmx.de python-engineer123@my-domain.org'


# In[63]:


#pattern=re.compile('Mr\s\W+')
pattern=re.compile(r'(Mr|Ms|Mrs)\.?\s\w+')


# In[64]:


matches=pattern.finditer(condition)


# In[65]:


for match in matches:
    print(match)


# In[90]:


pattern=re.compile(r'[a-zA-Z]+@[a-z]+\.(com|de)')


# In[91]:


matches=pattern.finditer(condition)


# In[92]:


for match in matches:
    print(match)


# In[93]:


for match in matches:
    print(match.group(1))


# In[94]:


spit='123asdabc435435ghgadb4543ABC'


# In[96]:


pattern=re.compile(r'abc')
sp=pattern.split(spit)


# In[97]:


print(sp)


# In[98]:


string='word ,you are the best word'


# In[99]:


pattern=re.compile(r'you')
sub=pattern.sub('good',string)


# In[100]:


print(sub)


# In[ ]:




