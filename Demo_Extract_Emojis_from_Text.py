#!/usr/bin/env python
# coding: utf-8

# # Example to show how to extract emojis in text

# In[1]:


# Code to process the emojis in text to return a list of emojis found

# python library dependencies used in extractEmojis module are  regex, re, and Unicode_emojis_list.py
# if re not on system do pip install re

import extractEmojis


# In[2]:


# Demo of basic code on some text with or without emojis

some_text = "Some emoji 👨🏾‍👩🏾‍👧🏾‍👦🏾 🗳❤️🇦🇺😃🌹 smiles🌹4️⃣🍎🇦 👪🏿 👩🏿‍💻 🗳🗳️"

emojis_list = extractEmojis.getEmojisFromText(some_text)

unique_emojis = extractEmojis.getUniqueEmojisFromEmojiList(emojis_list)

print('emojis in text', emojis_list)
print('unique emojis', unique_emojis)

# Note sometimes the emojis may not render on your device properly, 
# eventhough the emoji is still correct
# when in doubt you can always copy and paste the emoji in to Emojipedia.org


# In[3]:


# Demo of basic code using pandas

import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.width', 5000)


# In[4]:



# Load in data such as csv
df = pd.read_csv('./sample_data/sample_csv_data_w_emojis_utf8.csv')
#df = pd.read_excel('./sample_data/sample_xlsx_data_w_emojis.xlsx')

print(df.shape)
df.head(10)


# In[5]:


# get list of emojis in text 

# if large dataset, it is faster to process emojis on the unique text then merge the results back to the dataframe
# may take a while if large dataset (could take 40 minutes if millions of rows of tweets)
df['emojis_list'] = df['text'].apply(extractEmojis.getEmojisFromText)

# get sorted list of unique emojis in text so can compare
df['unique_emojis_list'] = df['emojis_list'].apply(extractEmojis.getUniqueEmojisFromEmojiList)

# make a quick check if emojis are present
df['emoji_present'] = df['unique_emojis_list'].apply(lambda x: True if len(x)>0 else False)

# get the number of emojis in the emojis list
df['number_of_emojis_used'] = df['emojis_list'].str.len()

# show the first few rows
df.head(10)


# In[6]:


# save the processed data
df.to_csv('sample_output_with_emojis_processed.csv', index=False, encoding='utf8')


# In[7]:


# get the most used unique emojis in this sample dataset

# matrix of unique emojis per row
list_of_lists_of_unique_emojis = df['unique_emojis_list'].tolist()

# get a list of emojis with count of rows in descending order
emojis_w_count_rows_descending = extractEmojis.getUniqueEmojiWithCounts(list_of_lists_of_unique_emojis)

# show the top 10 most common emojis across rows with row count
print(emojis_w_count_rows_descending[:10])
print()

# get just the top emojis
top_10_emojis = [emoji_tuple[0] for emoji_tuple in emojis_w_count_rows_descending[:10]]
print(top_10_emojis)


# In[8]:


# get the most unique emojis per user

users_aggregation_df = df.groupby('userid').agg({'rownum':'count','unique_emojis_list':'sum'}).reset_index()
users_aggregation_df.columns = ['userid','count_rows','combined_list_of_unique_emojis']
users_aggregation_df['unique_emojis_used_list'] = users_aggregation_df['combined_list_of_unique_emojis'].apply(lambda x: sorted(list(set(x))))
users_aggregation_df['number_of_unique_emojis_used'] = users_aggregation_df['unique_emojis_used_list'].str.len()
users_aggregation_df.head(10)    


# In[9]:


# most used emoji across users in this sample dataset

# matrix of unique emojis per row
list_of_lists_of_unique_emojis = users_aggregation_df['unique_emojis_used_list'].tolist()

# get a list of emojis with count of users in descending order
emojis_w_count_users_descending = extractEmojis.getUniqueEmojiWithCounts(list_of_lists_of_unique_emojis)

# show the top 10 most common emojis across users with user count
print(emojis_w_count_users_descending[:10])
print()

# get just the top emojis across users
top_10_emojis_across_users = [emoji_tuple[0] for emoji_tuple in emojis_w_count_users_descending[:10]]
print(top_10_emojis_across_users)


# In[10]:


# example of working with the processed dataset later
df2 = pd.read_csv('sample_output_with_emojis_processed.csv')
df2.head()


# In[11]:


# use the ast module to access the emojis in the list when the list is stored as string

import ast 

# ast.literal_eval() allows you to convert a string version of a list into a list object
# convert the string version of the list to a list
df2['unique_emojis_list'] = df2['unique_emojis_list'].apply(lambda x: ast.literal_eval(x))

# to get the count of number of unique emojis used
df2['number_of_unique_emojis']=df2['unique_emojis_list'].str.len()

# show distribution of number of unique emojis across this sample dataset
df2['number_of_unique_emojis'].value_counts()


# In[ ]:




