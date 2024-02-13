#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Converting Data types


# In[2]:


num_int = 7
type(num_int)


# In[3]:


num_str = '7'
type(num_str)


# In[4]:


num_sum = num_int + num_str


# In[5]:


#convert str into int

num_str_conv = int(num_str)


# In[9]:


type(num_str_conv)


# In[10]:


num_sum = num_int + num_str_conv
print(num_sum)


# In[11]:


list_type = [1,2,3]
type(list_type)


# In[12]:


#convert into tuple
tuple(list_type)


# In[13]:


type(tuple(list_type))


# In[14]:


list_type = [1,2,3,3,2,1,2,3,2,1]


# In[15]:


set(list_type)


# In[16]:


#set takes the unique value in the list and turn it into set


# In[18]:


dict_type = {'name': 'Wesley', 'age': 28, 'hair': 'N/A'}
type(dict_type)


# In[19]:


dict_type.items()


# In[20]:


dict_type.values()


# In[21]:


#key are the name, age and hair
dict_type.keys()


# In[22]:


list(dict_type.keys())


# In[24]:


long_str = "I like to party"

list(long_str)


# In[25]:


set(long_str)


# In[ ]:




