# Write a Data Science blog post
Udacity DSND project 4 - writing a blog post on data science

### Table of Contents

1. [Installation](#installation)
2. [Data]  (#data)
3. [Project Motivation](#motivation)
4. [File Description](#files)
5. [Results](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)


## Installation <a name="installation"></a>

This project requires **Python 3.x** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)

You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html)

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 


## Data <a name="data"></a>

You need some data in this project to work upon. For that I have selected Stackoverflow’s 2017, 2018 and 2019 Annual Developer Survey data. You can find the data to download [here](https://insights.stackoverflow.com/survey). </br>

To move the downloaded files to the specific folder, you can execute. </br>

1. Stackoverflow’s 2017 data </br>
` mv survey_results_public.csv Write-a-Data-Science-Blog-Post/data/2017/survey_results_public.csv `</br>

2. Stackoverflow’s 2018 data </br>
` mv survey_results_public.csv Write-a-Data-Science-Blog-Post/data/2018/survey_results_public.csv `</br>

3. Stackoverflow’s 2019 data </br>
` mv survey_results_public.csv Write-a-Data-Science-Blog-Post/data/2019/survey_results_public.csv `</br>

The data is mainly made up of two files:

survey_results_public.csv - CSV file with main survey results, one respondent per row and one column per answer
survey_results_schema.csv - CSV file with survey schema, i.e., the questions that correspond to each column name



## Project Motivation <a name="motivation"></a>

This is an Udacity Nanodegree project.I was interested in using Stackoverflow Developer Survey Data to better understand:</br>
1. Which part of the world is better for software developers, Western countires or Asian countries? </br>
2. What is the difference in pay scale of developer in these countries? </br>
3. What do developers feel about job statisfaction in these countries? </br>



## File Description <a name="files"></a>

**Write_a_Data_Science_Blog.ipynb**: Notebook containing the data analysis. </br>
**data/2017/survey_results_public.csv**: Stackoverflow's 2017 Annual Developer Survey data. </br>
**data/2018/survey_results_public.csv**: Stackoverflow's 2018 Annual Developer Survey data. </br>
**data/2019/survey_results_public.csv**: Stackoverflow's 2019 Annual Developer Survey data. </br>



## Results <a name="results"></a>
The main findings of the code can be found at the post available [here]()




## Licensing, Authors, Acknowledgements<a name="licensing"></a>
Must give credit to Stackoverflow for the data. Data is directly taken from StackOverflow and licensed under the ODbL license. You can find the Licensing for the data and other descriptive information at the Stackoverflow link available [here](https://insights.stackoverflow.com/survey).
