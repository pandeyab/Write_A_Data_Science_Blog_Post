#!/usr/bin/env python
# coding: utf-8

# ### Project - Write A Data Sceince Blog post
# 
# Key Steps for Project
# Feel free to be creative with your solutions, but do follow the CRISP-DM process in finding your solutions.
# 
# 1) Pick a dataset.
# 
# 2) Pose at least three questions related to business or real-world applications of how the data could be used.
# 
# 3) Create a Jupyter Notebook, using any associated packages you'd like, to:
# 
# Prepare data:
# 
# Gather necessary data to answer your questions
# Handle categorical and missing data
# Provide insight into the methods you chose and why you chose them
# Analyze, Model, and Visualize
# 
# Provide a clear connection between your business questions and how the data answers them.
# 4) Communicate your business insights:
# 
# Create a Github repository to share your code and data wrangling/modeling techniques, with a technical audience in mind
# Create a blog post to share your questions and insights with a non-technical audience

# In[1]:


# import libraries here; add more as necessary
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

# magic word for producing visualizations in notebook
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Pick a dataset
# I picked the 2017 survey of Stack Overflow data to answer all of the below questions:
#     1. Which part of the world is better for software developers, Western countires or Asian countries?
#     2. What is the difference in pay scale of developer in these countries?
#     3. What do developers feel about job statisfaction in these countries?
#     4. Which part of the world provide better carrer satisfaction?

# In[2]:


#Read the data and glimpse it
df = pd.read_csv('survey_results_public_2017.csv')
display(df.head())


# In[3]:


#shape of dataframe
print(df.shape)

#all columns
print(df.columns.values)


# In[4]:


df.describe()


# ### Which part of the world is better for software developers, Western countires or Asian countries?

# In[5]:


# Understanding the data from survey 2017
def bar_chart_plot(df, column, title):
    '''
    Plotting a bar chart
    
    input args:
    df: a dataframe
    column: the column which we want to show
    title: the title of the chart
    
    '''
    plt.figure(figsize=(11,7))
    status_values = df[column].value_counts()
    s= (status_values[:10]/df.shape[0])
    my_colors = list('rgbkymc')
    
    s.plot(kind="bar", color=my_colors,)
    plt.title(title);


# In[6]:


#plotting each Professional status
bar_chart_plot(df, "Professional", "Developer type?")


# In[7]:


#Plotting Employment status
bar_chart_plot(df, "EmploymentStatus", "Employment Status?")


# In[8]:


#plotting origin Country
bar_chart_plot(df, "Country", "origin country?")


# In[9]:


#Plotting jobsatisfaction status
bar_chart_plot(df, "JobSatisfaction", "How job statisfaction spreaded?")


# In[10]:


#Plotting salary status
bar_chart_plot(df, "Overpaid", "How do professionals feel about overpaid status?")


# ### Data preparation
# Here we will devide the data columns from "Countries" int to Western and Asians countires

# In[11]:


def country_data(df):
    '''
    
    Return a dataframe with country seperated
    
    Parameters:
    df: a dataframe
    
    Returns:
    df: a dataframe with a new column 
    
    '''
    # For Categorical variables "Country", we seperate them into 
    # three sessions: western, asian and other
  
    western = ['United States', 'Liechtenstein', 'Switzerland', 
           'Iceland', 'Norway', 'Israel', 'Denmark', 
           'Ireland', 'Canada', 'United Kingdom', 'Germany', 
           'Netherlands', 'Sweden', 'Luxembourg', 'Austria', 
           'Finland', 'France', 'Belgium', 'Spain', 'Italy',
           'Poland']

    top_asians = ['India', 'Thailand', 'Singapore', 'Hong Kong', 
           'South Korea', 'Japan', 'China', 
           'Taiwan', 'Malaysia', 'Indonesia', 'Vietnam']
    rest_asians = ['Malaysia', 'Indonesia', 'Vietnam', 'Sri Lanka', 'Pakistan', 'Bangladesh']
    
    #Add a new catagory seperating to western and eastern
    df['west_or_asians'] = df['Country'].apply(lambda x: 'western' if x in western else ('top_asians' if x in top_asians else ('rest_asians' if x in rest_asians else 'other')))
    
    return df


# Here we select some useful columns for our analysis.
# - Country: Country they are living
# - YearsCodingJob: Years they are coding
# - JobSatisfaction & CareerSatisfaction: Are their satisfy their job and career
# - EmploymentStatus: Their employment status
# - Salary: Their Salary
# 
# We especially focus on employed full-time professional developer.

# In[12]:


#function  to create a dataframe
def data_prep(df):
    '''
    
    Return useful columns with query condition
    
    Parameters:
    df: a raw data dataframe
    
    Returns:
    useful_df: a filtered dataframe with only useful columns
    
    '''
    #Getting some useful columns for analysis
    usefull_col = ['Country', 'YearsCodedJob', 'EmploymentStatus', 'CareerSatisfaction', 'JobSatisfaction', 'JobSeekingStatus', 'HoursPerWeek', 'Salary', 'west_or_asians', 'Overpaid']
    usefull_df = pd.DataFrame(df.query("Professional == 'Professional developer' and (Gender == 'Male' or Gender == 'Female') and EmploymentStatus == 'Employed full-time'"))[usefull_col]
    return usefull_df


# In[13]:


#create a dataframe to work upon and analysis
d_df = country_data(df)
d_df.head(5)
usefull_df = data_prep(d_df)

usefull_df.shape


# In[14]:


usefull_df.head(5)


# For categorical variable Overpaid, we transfer it to calculatable integer value because we want to find out the mean of their opinion.

# In[15]:


def underpaid_check(df):
    """
    
    Parameters:
    df: a dataframe
    
    Returns:
    dataframe: a converted dataframe with Overpaid column
    
    """
    pay_mapping = {
        'Greatly underpaid' : 1,
        'Somewhat underpaid' : 2,
        'Neither underpaid nor overpaid' : 3,
        'Somewhat overpaid' : 4,
        'Greatly overpaid' : 5,
        np.nan: np.nan
    }
    df['Overpaid'] = df['Overpaid'].apply(lambda x: np.nan if x == np.nan else pay_mapping[x] )
    
    return df


# In[16]:


#Compare selected indicators between western and asians region
usefull_df = underpaid_check(usefull_df)
compared = usefull_df.groupby(['west_or_asians','YearsCodedJob']).mean()
compared


# column 'YearsCodedJob' will be  transferred to calculatable integer value because we want to find out the mean of how long they have been coded.

# In[17]:


def handlingExp(df):
    """
    Convert the working year to integer
    
    Parameters:
    df: a dataframe
    
    Returns:
    dataframe: a converted dataframe with YearsCodedJob column
    
    """
    exp_mapping = {'1 to 2 years' : 1, 
                '10 to 11 years' : 10, 
                '11 to 12 years' : 11, 
                '12 to 13 years' : 12,
                '13 to 14 years' : 13, 
                '14 to 15 years' : 14, 
                '15 to 16 years' : 15, 
                '16 to 17 years' : 16,
                '17 to 18 years' : 17, 
                '18 to 19 years' : 18, 
                '19 to 20 years' : 19, 
                '2 to 3 years' : 2,
                '20 or more years' : 20, 
                '3 to 4 years' : 3, 
                '4 to 5 years' : 4, 
                '5 to 6 years' : 5, 
                '6 to 7 years' : 6, 
                '7 to 8 years' : 7, 
                '8 to 9 years' : 8, 
                '9 to 10 years' : 9, 
                'Less than a year' : 0}
    
    df_graph = df.reset_index()
    df_graph['YearsCodedJob'] = df_graph['YearsCodedJob'].apply(lambda x: exp_mapping[x])
    df_graph['YearsCodedJob'] = pd.to_numeric(df_graph['YearsCodedJob'])
    
    return df_graph


# In[18]:


compared_graph = handlingExp(compared)
compared_graph = compared_graph.sort_values(by='YearsCodedJob')


compared_graph.set_index('YearsCodedJob', inplace=True)


# In[19]:


compared_graph.head()


# ### Its time to evaluate the analysis,  based on our questions
# 

# ### Result of 1st question
# 1st question is about better countries to work for a developer. For that we will compare the salaries of developers against thier years of experience to find out which region has better proportions.

# In[20]:


#Plot the Salary Comparison
plt.figure(figsize=(12,10))
compared_graph.groupby('west_or_asians')['Salary'].plot(legend=True)

plt.title("Salary Comparison between Western and Asian region");
plt.xlabel('Years of Exp')
plt.ylabel('Average Salary')


# As we could see above, Western contries pay better salary to their developer as compared to other parts of the world. 

# ### Result of 2nd question
# 2nd question is about pay scale difference for a developer. For that we will compare the overpaid status of developers against thier years of experience to find out which region has better proportions. Overpaid status will tell if they feel good about about their remuneration or not.

# In[21]:


#Plot the overpaid status
plt.figure(figsize=(12,10))
compared_graph.groupby('west_or_asians')['Overpaid'].plot(legend=True)

plt.title("Do developers think they are overpaid?");
plt.xlabel('YearsCodedJob')
plt.ylabel('Overpaid status')


# Result is pretty interesting. As we could see above the "rest_asian" countries's developer said that they are somehow better paid than "Top_Asians" countries but thier salary is lesser than Top Asian region. 
# 
# And Top Asians feel that they are husly underpaid than their Western countries counterparts.

# ### Result of 3rd question
# 3rd question is about Job Satisfaction for a developer. For that we will compare the job statisfaction status of developers against thier years of experience to find out which region has better proportions.

# In[22]:


#Plot the JobSatisfaction status
plt.figure(figsize=(12,10))
compared_graph.groupby('west_or_asians')['JobSatisfaction'].plot(legend=True)

plt.title("Do developers feel statisfied with job?");
plt.xlabel('YearsCodedJob')
plt.ylabel('Job Satisfaction status')


# Here we can see developer from Western region and other part of the world are satisfied with thier job on an average scale as compared to thier counterparts from Asian countries in the beginning of thier job. After some 18 years in job, Rest_Asian contries data improves a lot than others, while others go same level on an average.
# 
# Final observation is gonna be so much interesting to know which part of the world is better.
# 

# ### Result of 4th question
# 4th question is about Career Satisfaction for a developer. For that we will compare the career statisfaction status of developers against thier years of experience to find out which region has better proportions.

# In[23]:


#Plot the CareerSatisfaction status
plt.figure(figsize=(12,10))
compared_graph.groupby('west_or_asians')['CareerSatisfaction'].plot(legend=True)

plt.title("Do developers feel statisfied with career?");
plt.xlabel('YearsCodedJob')
plt.ylabel('Career Satisfaction status')


# Here we can see developer from Western region and other part of the world are satisfied with thier career on an average scale as compared to thier counterparts from Asian countries in the beginning of thier job. After some 18 years in job, Rest_Asian contries data improves a lot than others, while others go same level on an average.

# ### Combined analysis of Job and Career satisfaction for developers from western and asian countries 

# In[24]:


compared.groupby('west_or_asians').mean().CareerSatisfaction


# In[25]:


compared.groupby('west_or_asians').mean().JobSatisfaction


# In[26]:


compared.groupby('west_or_asians').mean().Salary/50


# In[27]:


#Plot Comparison of Career and Job Satisfaction between Western and Eastern
plt.figure(figsize=(12,10))
plt.scatter(compared.groupby('west_or_asians').mean().CareerSatisfaction, compared.groupby('west_or_asians').mean().JobSatisfaction, compared.groupby('west_or_asians').mean().Salary/50, c=['blue','red', 'green','magenta'])

plt.title('Comparison of Career and Job Satisfaction\n(Blue: Top_Asians; Red: rest_asians, Green: Other; Magenta: Western)')
plt.xlabel('Career Satisfaction')
plt.ylabel('Job Satisfaction')


# As we could see in above comparison scatter plot, combining Salary, Job Sastisfaction, Career Satisfaction against their years of exp in coding, developers feel better satisfied with career and job from these part of the world in following order (1st - better, last - lesser) 
# --> Western - Top_Asians - Others - Rest_Asians

# ### Conclusion
# - Western contries pay better salary to their developer as compared to other parts of the world. 
# - Regarding the pay scale difference, we found that "rest_asian" countries's developer said that they are somehow better paid than "Top_Asians" countries but thier salary is lesser than Top Asian region. And Top Asians feel that they are husly underpaid than their Western countries counterparts.
# - Regarding the Job Satisfaction, we found that developer from Western region and other part of the world are satisfied with thier job on an average scale as compared to thier counterparts from Asian countries in the beginning of thier job. After some 18 years in job, Rest_Asian contries data improves a lot than others, while others go same level on an average.
# - Regarding the Career Satisfaction, we found that developer from Western region and other part of the world are satisfied with thier career on an average scale as compared to thier counterparts from Asian countries in the beginning of thier job. After some 18 years in job, Rest_Asian contries data improves a lot than others, while others go same level on an average
# 
# -After combining Salary, Job Sastisfaction and Career Satisfaction against their years of exp in coding, developers feel better satisfied with career and job from western countries as compared to others.

# ### Final Observation
# 
# Keeping Salary, Job Sastisfaction, Career Satisfaction and other factors against their years of exp in coding in mind, Western part of the world is a bettet place to work for a developer.
# 

# In[28]:


get_ipython().getoutput('jupyter nbconvert *.ipynb')

