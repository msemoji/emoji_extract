#!/usr/bin/env python
# coding: utf-8

# # Example to show how to extract emojis in text based on .ipynb Jupyter notebook

# In[2]:


import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.width', 5000)


# In[3]:


# Code to process the emojis in text to return a list of emojis found

# python library dependencies used in extractEmojis module are  regex, re, and Unicode_emojis_list.py
# if re not on system do pip install re

import extractEmojis


# In[4]:


# Load in data such as csv
df = pd.read_csv('./sample_data/sample_csv_data_w_emojis_utf8.csv')
#df = pd.read_excel('./sample_data/sample_xlsx_data_w_emojis.xlsx')

print(df.shape)
df.head()


# In[7]:


# get list of emojis in text
df['emojis_list'] = df['text'].apply(extractEmojis.getEmojisFromText)

# get sorted list of unique emojis in text so can compare
df['unique_emojis_list'] = df['emojis_list'].apply(extractEmojis.getUniqueEmojisFromEmojiList)

# make a quick check if emojis are present for ease of future processing
df['emoji_present'] = df['unique_emojis_list'].apply(lambda x: True if len(x)>0 else False)


# In[8]:


df.head()


# In[ ]:




