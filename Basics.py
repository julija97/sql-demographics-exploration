#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('capture', '', '%load_ext sql\n%sql sqlite:///factbook.db')


# In[3]:


#overview of the data
%%sql
SELECT *
  FROM sqlite_master
 WHERE type='table';


# In[10]:


get_ipython().run_cell_magic('sql', '', 'SELECT *\nFROM facts\nLIMIT 5;')


# In[12]:


#finding min and max values for population and population growth
%%sql
SELECT MIN(population), MAX(population), MIN(population_growth), MAX(population_growth)
FROM facts;


# In[21]:


# outlier detection - finding countries with min and max populations
%%sql
SELECT *
FROM facts
WHERE population IN ((SELECT MIN(population) FROM facts), (SELECT MAX(population) FROM facts));


# In[22]:


#excluding "world" from countries
%%sql
SELECT MIN(population), MAX(population), MIN(population_growth), MAX(population_growth)
FROM facts
WHERE name <> 'World'


# In[23]:


#finding average population and area values
%%sql
SELECT AVG(population), AVG(area)
FROM facts;


# In[25]:


#finding densely populated countries 
%%sql
SELECT *
FROM facts
WHERE population > (SELECT AVG(population) FROM facts) AND area < (SELECT AVG(area) FROM facts);


# In[28]:


#finding a country with largest water/land ratio
%%sql
SELECT *
FROM facts
WHERE area_water/area_land == (SELECT MAX(area_water/area_land) FROM facts)


# In[29]:


#finding countries that have more water than land
%%sql
SELECT *
FROM facts
WHERE area_water > area_land


# In[30]:


#finding countries that have a higher death rate than birth rate
%%sql
SELECT *
FROM facts
WHERE death_rate > birth_rate


# In[31]:


#finding a country that have the highest population/area ratio
%%sql
SELECT name, population/area
FROM facts
WHERE population/area IN (SELECT MAX(population/area) FROM facts)


# In[ ]:




