#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests

#importing the necesary libraries


# In[2]:


url="http://www.ngtradeonline.com/Home/dailypricelist?extension=txt"
page=requests.get(url)

#request the website


# In[3]:


print(page)


# In[4]:


page.status_code

#view the status code of the request, anything from 200-299 is successful


# In[5]:


len(page.text)

#this gives the length of word characters


# In[6]:


page.text[:500]

#viewing the first 500


# In[7]:


soup=BeautifulSoup(page.content,"html.parser")

#this syntax parses the content of the website


# In[8]:


stock_prices=(soup.prettify())  #you can add prettify() for finer appearance


# In[9]:


table_heading=soup.find("thead",attrs={"class":"headerCell"})
table_header_tags=soup.thead.find_all("th")
table_header_tags

#finding all the header tags in the webpage


# In[10]:


headings = []
for th in table_header_tags:
    # find all the column names in the table
    headings.append(th.text.strip())
headings

#obtain the headers from the header tags in the table and append it to an empty list


# In[11]:


stock_=soup.find("tr",attrs={"class":"style"})
stock_tr=soup.tbody.find_all("tr")
stock_tr


# In[12]:


stock_rows=[]
for tr in stock_tr:
    stock_rows.append(tr.text.strip())
stock_rows
    


# In[13]:


stocks=soup.find("table","style")
stock_tags=soup.tbody.find_all("td")
stock_tags[:10]


# In[14]:


stock_data=[]
for td in stock_tags:
    stock_data.append(td.text)
stock_data


# In[21]:


stock_array=np.reshape(stock_data,(132,8))

#reshape the rows of the data to 132 by 8 columns. Be reminded that the daily pricelist may change so always see the number of rows in the data before reshaping


# In[51]:


stock_price_list=pd.DataFrame(stock_array)
stock_price_list.columns=headings
#stock_price_list=stock_price_list.set_index("Symbol")


# In[52]:


stock_price_list


# In[58]:


stock_price_list=stock_price_list[["Symbol","OPEN","Low","High","Close","Volume","CHANGE"]]

#this is to reset the columns positions for easy reading from the symbol to the percentage change, you can also use the syntax 'stock_price_list.iloc[:,column number] or stock_price_list.reindex([])'


# In[59]:


stock_price_list


# In[1]:


from csv import writer
#this will import a writer to write the pandas dataframe created to csv


# In[105]:


'''with pd.ExcelWriter("C:\\Users\\Dakon\\Documents\\stock_list_today.xlsx") as writer:
    stock_price_list.to_excel(writer,sheet_name="stock_price_list")
    stock_top_gainers.to_excel(writer,sheet_name="top_gainers")
    stock_top_gainers.to_excel(writer,sheet_name="top_losers")
    stock_top_gainers.to_excel(writer,sheet_name="top_volumes")
    '''
    


# In[100]:


stock_price_list.to_csv("C:\\Users\\Dakon\\Documents\\stock_list_today.csv",index=False)

#Exporting the stock_price_list to my local document folder as a csv file


# In[ ]:




