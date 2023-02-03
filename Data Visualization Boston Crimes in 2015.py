#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[5]:


get_ipython().system('pip install folium')


# In[6]:


import folium


# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium


# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium

df=pd.read_csv("StudentsPerformance.csv")


# In[14]:


df=pd.read_csv("StudentsPerformance.csv")
df.head()


# In[15]:


df.info()


# In[18]:


df.isna().sum()


# In[19]:


df.describe()


# In[20]:


df.describe(exclude = np.number)


# In[23]:


plt.figure(figsize = (10, 6))
plt.axvline(df['math score'].describe()['mean'], color = 'red', label = 'mean')
plt.axvline(df['math score'].describe()['50%'], color = 'yellow', label = 'median')
sns.distplot(df['math score'])
plt.legend()


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium

df=pd.read_csv("StudentsPerformance.csv")


# In[5]:


import 


# In[6]:


df.info()


# In[7]:


df=pd.read_csv("StudentsPerformance.csv")

for i in df.index:
    print("gender "+df['gender'][i])
    print("parental level of education: "+df['parental level of education'][i])
    print("lunch: "+df['lunch'][i])


# In[9]:


df=pd.read_csv("StudentsPerformance.csv")

lst = []
for i in df.index:
    data = {}
    print("gender "+df['gender'][i])
    print("parental level of education: "+df['parental level of education'][i])
    print("lunch: "+df['lunch'][i])
    lst.append(data)
    print(lst)


# In[10]:


import csv

with open('StudentsPerformance.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    print(csv_reader)
    for row in csv_reader:
        print(row)


# In[14]:


import csv

df = []

with open('StudentsPerformance.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        df.append(row)

print(df)


# In[18]:


import csv

lunch= []

with open('StudentsPerformance.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        lunch.append(row)

labels = lunch.pop(0)

print(labels)
print(lunch)


# In[23]:


import csv

df = []

with open('StudentsPerformance.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        df.append(row)


labels = df.pop(0)

#print(labels)
#print(df)

print(f'{labels[0]} \t {labels[1]} \t\t {labels[2]}')
print("-"*34)
for data in df:
    print(f'{data[0]} \t {data[1]} \t {data[2]}')


# In[26]:


import csv

df = []

with open('StudentsPerformance.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        df.append(row)

print(df)


# In[27]:


import csv

contacts = []

with open('StudentsPerformance.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        contacts.append(row)

print("gender \t race/ethnicity \t\t math score")
print("-" * 32)

for data in contacts:
    print(f"{data['gender']} \t {data['race/ethnicity']} \t {data['math score']}")


# In[8]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium

df=pd.read_csv("boston-crimes.csv", encoding='latin-1')


# In[7]:


df.info()


# In[10]:


df.head()


# In[11]:


df.tail()


# In[12]:


# Menghapus Kolom Atau Fitur Yang tidak Berguna Untuk Analisa Data
df = df.drop(['INCIDENT_NUMBER','OFFENSE_CODE','UCR_PART','Location'], axis=1)


# In[15]:


# Mengganti tipe data di kolom Occured_on_Date
df['OCCURRED_ON_DATE'] = pd.to_datetime(df['OCCURRED_ON_DATE'])


# In[16]:


# Mengisi NAN Value di Kolom Shooting
df.SHOOTING.fillna('N', inplace=True)


# In[17]:


# Convert DAY_OF_WEEK to an ordered category
df.DAY_OF_WEEK = pd.Categorical(df.DAY_OF_WEEK, 
              categories=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
              ordered=True)


# In[18]:


# Replace -1 values in Lat/Long with Nan
df.Lat.replace(-1, None, inplace=True)
df.Long.replace(-1, None, inplace=True)


# In[19]:


# Rename columns to something easier to type (the all-caps are annoying!)
rename = {'OFFENSE_CODE_GROUP':'Group',
         'OFFENSE_DESCRIPTION':'Description',
         'DISTRICT':'District',
         'REPORTING_AREA':'Area',
         'SHOOTING':'Shooting',
         'OCCURRED_ON_DATE':'Date',
         'YEAR':'Year',
         'MONTH':'Month',
         'DAY_OF_WEEK':'Day',
         'HOUR':'Hour',
         'STREET':'Street'}
df.rename(index=str, columns=rename, inplace=True)


# In[36]:


def create_list_number_crime(name_column, list_unique):
    i = 0
    
    list_number = list()
    
    while i < len(list_unique):
        list_number.append(len(df.loc[df[name_column] == list_unique[i]]))
        i += 1
        
    return list_unique, list_number

def pie_plot(list_number, list_unique):
    plt.figure(figsize=(20,10))
    plt.pie(list_unique,
           labels=list_number,
           autopct='%1.1f%%',
           shadow=True,
           startangle=140)
    
    plt.axis('equal')
    plt.show()
    return 0

def bar_chart(list_number, list_unique):
    objects = list_unique
    y_pos = np.arrange(len(objects))
    performance = list_number
    
    plt.figure(figsize=(20,10))
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Number')
    plt.show()
    
    return 0


# In[27]:


plt.figure(figsize=(16,8))
df['District'].value_counts().plot.bar()
plt.show()


# In[37]:


list_unique_year, list_number_year = create_list_number_crime('Year',df['Year'].unique())
pie_plot(list_unique_year, list_number_year)


# In[7]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import folium

df=pd.read_csv("boston-crimes.csv", encoding='latin-1')


# In[8]:


df.tail()


# In[9]:


df = df.drop(['INCIDENT_NUMBER','OFFENSE_CODE','UCR_PART','Location'], axis=1)


# In[10]:


df['OCCURRED_ON_DATE'] = pd.to_datetime(df['OCCURRED_ON_DATE'])


# In[11]:


df.SHOOTING.fillna('N', inplace=True)


# In[13]:


# Convert DAY_OF_WEEK to an ordered category
df.DAY_OF_WEEK = pd.Categorical(df.DAY_OF_WEEK, 
              categories=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
              ordered=True)


# In[14]:


# Replace -1 values in Lat/Long with Nan
df.Lat.replace(-1, None, inplace=True)
df.Long.replace(-1, None, inplace=True)


# In[15]:


# Rename columns to something easier to type (the all-caps are annoying!)
rename = {'OFFENSE_CODE_GROUP':'Group',
         'OFFENSE_DESCRIPTION':'Description',
         'DISTRICT':'District',
         'REPORTING_AREA':'Area',
         'SHOOTING':'Shooting',
         'OCCURRED_ON_DATE':'Date',
         'YEAR':'Year',
         'MONTH':'Month',
         'DAY_OF_WEEK':'Day',
         'HOUR':'Hour',
         'STREET':'Street'}
df.rename(index=str, columns=rename, inplace=True)


# In[39]:


def create_list_number_crime(name_column, list_unique):
    i = 0
    
    list_number = list()
    
    while i < len(list_unique):
        list_number.append(len(df.loc[df[name_column] == list_unique[i]]))
        i += 1
        
    return list_unique, list_number

def pie_plot(list_number, list_unique):
    plt.figure(figsize=(20,10))
    plt.pie(list_unique,
           labels=list_number,
           autopct='%1.1f%%',
           shadow=True,
           startangle=140)
    
    plt.axis('equal')
    plt.show()
    return 0

def bar_chart(list_number, list_unique):
    objects = list_unique
    y_pos = np.arange(len(objects))
    performance = list_number
    
    plt.figure(figsize=(20,10))
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Number')
    plt.show()
    
    return 0


# In[17]:


plt.figure(figsize=(16,8))
df['District'].value_counts().plot.bar()
plt.show()


# In[42]:


list_unique_month, list_number_month = create_list_number_crime('Month',list(range(1, 12)))
bar_chart(list_unique_month, list_number_month)


# In[43]:


list_unique_hour, list_number_hour = create_list_number_crime('Hour', list(range(0, 24)))
bar_chart(list_number_hour, list_unique_hour)


# In[44]:


#countplot for crime types
sns.catplot(y='Group',
           kind='count',
           height=8,
           aspect=1.5,
           order=df.Group.value_counts().head().index,
           data=df)


# In[45]:


to_delete = df[pd.isna(df.Lat) | pd.isna(df.Long)].index
df.drop(to_delete,axis=0,inplace=True)


# In[51]:


import folium
from folium.plugins import HeatMap

map_hooray = folium.Map(location=[42.35122731, -71.05621744],
                       zoom_start = 12, min_zoom=12)

heat_df = df[df['Year']==2015]
heat_df = heat_df[heat_df['Group']=='Larceny']
heat_df = heat_df[['Lat', 'Long']]

folium.CircleMarker([42.35122731, -71.05621744],
                    radius=50,
                    popup='Homicide',
                    color='red',
                    ).add_to(map_hooray)

heat_data = [[row['Lat'],row['Long']] for index, row in heat_df.iterrows()]

HeatMap(heat_data, radius=10).add_to(map_hooray)
map_hooray
                  
                    

