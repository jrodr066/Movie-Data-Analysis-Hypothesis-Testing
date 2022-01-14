#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
# load numpy 
import numpy as np
#Load:
from scipy.stats import mannwhitneyu
data1 = pd.DataFrame(pd.read_csv('/Users/jenniferrodrigueztrujillo/Downloads/movieReplicationSet.csv'))
#Self Notes:--------------------------------------------------------------------
##Grab the 400 columns, all the rows, and 400 columns 
# CAREFUL W/ iloc(use when we know index) vs loc
#df.rename(columns={'': ''}, inplace=True) 


# In[4]:


data1


# In[35]:


#Question 1 :--------------------------------------------------------------------
##      Are movies that are more popular (operationalized as having more 
##      ratings) rated higher than movies that
##      are less popular? [Hint: You can do a median-split of popularity 
##      to determine high vs. low popularity movies] 
##   it means the null hypothesis is rejected and your test is statistically significant    
#-------------------------------------------------------------------------------
popularities = data1.count() #counting the rows for ratings to determine popularity
median = popularities.median() #taking median of popularities


low_pop = popularities[popularities < median] #Placing lower popularity into an array
high_pop = popularities[popularities >= median] #Placing high popularity into an array

#Array for lower/higher ratings
low_pop_ratings = data1[low_pop.index]
high_pop_ratings = data1[high_pop.index]

#Finding the medians for both categories
med_low_pop = low_pop_ratings.median(skipna=True)
med_high_pop = high_pop_ratings.median(skipna=True)

#Mann-Whitney
mannwhitneyu(med_high_pop, med_low_pop, alternative='greater') #One-Tailed



#Self Notes:---------------------------------------------------------------------------
#Null Hypothesis: Popular Movies have the same rating as unpopular ratings
# If p-val<0.005, reject the null, p-val : 3.418584551895982e-33
# We REJECT the null with a p-val of 3.418584551895982e-33 and alpha of .005
# mannwhitneyu   -movie raitngs are continuos because it is measured variability
#                -we do not reduce this by sample means, mesusred median (Lecture 4)
# MANN WHITENEYU - measures MEDIAN
# x = avg_high_pop , y= avg_low_pop <---- used to find out mannwhitneyu, which comes first
# ONE-TAILED: stats.mannwhitneyu(avg_high_pop, avg_low_pop, use_continuity= True, alternative ='greater')
#Null-Hypothesis: Popular Movies have the same rating as unpopular movies
#Reject the Null Hypothesis if p<0.05


# In[19]:


##QUESTION 2----------------------------------------------------------------------[2-Tailed]
#Are movies that are newer rated differently than movies that are older?
#Count , order, count, drop rating.
#loop through, find movie w/ p less than .05 and divide through 
#-------------------------------------------------------------------------------------------
import pandas as pd

movieratingandtitles = data.iloc[:,:400] #GRAB THE 400 COLUMNS
movieTitles = pd.Series(list(movieratingandtitles)) #Grab the ratings; prints all info

#Years and titls split
movieYears = movieratingandtitles.columns.str.extract('\((\d+)\)').astype(int)
#Ratings
newmovieandyearcolumn= np.column_stack([movieTitles, movieYears])#np.column_stack([movieratingandtitles, movieYears])

newmovieandyearcolumn = newmovieandyearcolumn[(newmovieandyearcolumn[:, 1].argsort())]

#OLDER/NEWER Movies
oldermovie = movieratingandtitles.loc[:, pd.DataFrame(newmovieandyearcolumn[:200])[0].tolist()].median(axis=0) #medianofmovies[:,200]  #split into lower ratings
newermovie = movieratingandtitles.loc[:, pd.DataFrame(newmovieandyearcolumn[200:])[0].tolist()].median(axis=0)#medianofmovies[201:400] #split into higher ratings
#Cleaning data with data split into two categories
oldermovie_e = oldermovie[np.isfinite(oldermovie)]
newermovie_e = newermovie[np.isfinite(newermovie)]

mannwhitneyu(oldermovie_e, newermovie_e, alternative='two-sided') #Two-Tailed


#Notes: -------------------------
# Null-Hypothesis: Movies that are newever rated are rated differently than oldermovies
#If p-value <0.005, reject null , p-val=0.069
#We FAIL TO REJECT THE NULL with an alpha of 0.05 and a p-val of 0.069
#Summarize using median, compare median of medians between the 2 groups
#using string split


# In[20]:


##QUESTION 3------------------------------------------------------------------------
import numpy as np
from scipy.stats import mannwhitneyu

##Is enjoyment of 'Shrek(2001)' gendered, i.e. do male and female viewers rate it differently?
title= 'Shrek' ##Prints column for Shrek
data.columns.get_loc('Shrek (2001)')

#Creating column of movie and question of interest
dataone = data.iloc[:,[87,474]]

##We have gender, now we need rows where they are female and where they are male 475
dataforfemale =  dataone.loc[dataone['Gender identity (1 = female; 2 = male; 3 = self-described)'] == 1 ]
dataformale =  dataone.loc[dataone['Gender identity (1 = female; 2 = male; 3 = self-described)'] == 2 ]

#Placing female and male into array in relation to the movie Shrek(2001) to clean data
dataformalenp = np.array(dataformale['Shrek (2001)'])
dataforfemalenp = np.array(dataforfemale['Shrek (2001)'])

#Array to clean data of interest
datafem = dataforfemalenp[np.isfinite(dataforfemalenp)]
datamal = dataformalenp[np.isfinite(dataformalenp)]

##Mann-Whitney:
testman = mannwhitneyu(datafem, datamal, use_continuity=True, alternative='two-sided')

print(testman)
##Man-Whitney
#Null: Enjoyment of 'Shrek(2001)' gendered, male and female viewers rate it differently
#p-val:0.0505

#Fail to reject (accept, but do not use ACCEPT because everything is due to chance)
# m/f do not view the movies differently
#We have different sample sizes, makes our samples biased where our males is higher than females
#Viewing can also be biased without acknowledged in here
#wE'RE SPLITTING IN THE 200 MARK IN #1, DEPENDING IN THE FUNCTION WE USE TO SPLIT


# In[21]:


#Question 4 : --------------------------------------------------------------------------
#What proportion of movies are rated differently by male and female viewers?
#---------------------------------------------------------------------------------------

import numpy as np
from scipy.stats import mannwhitneyu

##Getting title for all movies
all_titles = data.columns
count = 0

#For-loop to conduct Mann-Whitney on sample size of 400
for i in range(400):
    
    ##We have gender, now we need rows where they are female and where they are male 475
    dataone = data1.loc[:,[all_titles[i], 'Gender identity (1 = female; 2 = male; 3 = self-described)']]
    
    #Clean data data of gender identity element-wise
    dataone = dataone[np.isfinite(dataone)]
    
    #Categorize into two arrays: female, males
    datafemale =  dataone.loc[dataone['Gender identity (1 = female; 2 = male; 3 = self-described)'] == 1 ].iloc[:,0]
    datamale =  dataone.loc[dataone['Gender identity (1 = female; 2 = male; 3 = self-described)'] == 2 ].iloc[:,0]
    
    #Clean data of female and male
    datafem = datafemale[np.isfinite(datafemale)]
    datamal = datamale[np.isfinite(datamale)]
    
    # For all females,males, run a mannwhitneyu, where for everyp-value above o.005, we add one to our count
    test22, p = mannwhitneyu(datafem, datamal)
    
    if p < 0.005:
        count += 1
#Calculate the proportion based off our out count, out of our sample size of 400
proportion = count/400

print("The proportion of movies rated differently by male and female viewers is ", count, "out of 400, or", proportion, '.')

#NOTE:-----------------------------------
#Cleaned data element wise, 
#Split the group into two groups(males and females), and for every movie 


# In[22]:


##QUESTION 5------------------------------------------------------------
##Do people who are only children enjoy 'The lion King (1994)' more than people with siblings?
##----------------------------------------------------------------------

import numpy as np
from scipy.stats import mannwhitneyu

title = 'The Lion King (1994)' ##Prints column for Shrek
data.columns.get_loc('The Lion King (1994)') #COLUMN 221, for indexing do ( 221 - 1 )

dataSib = data.iloc[:,[220,475]] #476 - column for "only child" 
                                 # " Are you an only child? (1: Yes; 0: No; -1: Did not respond)

##We have gender, now we need rows where they are ONLY CHILD(1) or NOT(0)
notOnly =  dataSib.loc[dataSib['Are you an only child? (1: Yes; 0: No; -1: Did not respond)'] == 0 ]
onlyChild =  dataSib.loc[dataSib['Are you an only child? (1: Yes; 0: No; -1: Did not respond)'] == 1 ]

#Array for movie in relation to sibling/nosiblings
notOnlynp = np.array(notOnly['The Lion King (1994)'])
onlyChildnp = np.array(onlyChild['The Lion King (1994)'])

#Cleaning data for only sibling or not only sibling
notOnlyprne = notOnlynp[np.isfinite(notOnlynp)]
onlyChildprne = onlyChildnp[np.isfinite(onlyChildnp)]

##Mann-Whitney
testmanSib = mannwhitneyu(notOnlyprne, onlyChildprne, use_continuity=True, alternative='less')

print(testmanSib)

###NOTES:
#- Null Hypothesis:  People who are only children enjoy 'The lion King (1994)' more than people with siblings.
#- If p-val<0.05, reject the null, p-val : 0.978419092554931
#- We FAIL TO REJECT the null with a p-val of 978419092554931
#- 
#-


# In[23]:


##QUESTION 6---------------------------------------------------------------------
# What proportion of movies exhibit an "only child effect", i.e. are rated
# different by viewers with siblings vs. those without?
# Two-tailed
##---------------------------------------------------------------------------------

##Getting title for all movies
import numpy as np
from scipy.stats import mannwhitneyu

##Getting title for all movies 
all_titles = data.columns
count = 0

for i in range(400):
    
    ##We have gender, now we need rows where they are female and where they are male 475
    dataone = data1.loc[:,[all_titles[i], 'Are you an only child? (1: Yes; 0: No; -1: Did not respond)']]
    dataone = dataone[np.isfinite(dataone)]
    
    notonlyChild =  dataone.loc[dataone['Are you an only child? (1: Yes; 0: No; -1: Did not respond)'] == 0 ].iloc[:,0]
    onlyChild =  dataone.loc[dataone['Are you an only child? (1: Yes; 0: No; -1: Did not respond)'] == 1 ].iloc[:,0]
    #print(datafemale)
    notonlyChil = notonlyChild[np.isfinite(notonlyChild)]
    onlyChil = onlyChild[np.isfinite(onlyChild)]
   # print(datafem)
    test22, p = mannwhitneyu(notonlyChil, onlyChil)
    
    if p < 0.005:
        count += 1
proportion = count/400

print("The proportion is..." , proportion)

#NOTES:
#Proportion is  7/400
#Two
#, BUT FOR EVERY SINGLE MOVIE-- FOR-LOOP, separate out only child and 
#         siblings for every single movie
#         -if p-value significant, add one to a counter,
#       count how many of those have a p-value of less than .005:
#####SHOULD BE 1.107

 


# In[33]:


##QUESTION 7------------------------------------------------------------------------
## Do people who like to watch movies socially enjoy 
## ‘The Wolf of Wall Street (2013)’ more than those who
## prefer to watch them alone? 
##----------------------------------------------------------------------------------
##‘The Wolf of Wall Street (2013)’ - COLUMN 358
## "Movies are best enjoyed alone (1: Yes; 0: No; -1: Did not respond)" - COLUMN 477
import numpy as np
from scipy.stats import mannwhitneyu

title = 'The Wolf of Wall Street (2013)' ##Prints column for 'The Wold of Wall Street'
data1.columns.get_loc('The Wolf of Wall Street (2013)') #COLUMN 358, for indexing do ( 358 - 1 = 357 )
dataAlone = data1.iloc[:,[357,476]]    # [movie, question of interest]  
                
#Separating data into 2 groups of interest
notbestalone =  dataAlone.loc[dataAlone['Movies are best enjoyed alone (1: Yes; 0: No; -1: Did not respond)'] == 0 ]
bestalone =  dataAlone.loc[dataAlone['Movies are best enjoyed alone (1: Yes; 0: No; -1: Did not respond)'] == 1 ]

notbestalonenp = np.array(notbestalone['The Wolf of Wall Street (2013)'])
bestalonenp = np.array(bestalone['The Wolf of Wall Street (2013)'])

#Cleaning Data 
notbestaloneprne = notbestalonenp[np.isfinite(notbestalonenp)]
bestalonenpprne = bestalonenp[np.isfinite(bestalonenp)]
#print(onlyChildprne)

##Mann-Whitney
testmanAlone = mannwhitneyu(notbestaloneprne, bestalonenpprne, use_continuity=True, alternative='greater')
print(testmanAlone)


# In[31]:


##QUESTION 8---------------------------------------------------------
## What proportion of movies exhibit such a “social watching” effect?
## ------------------------------------------------------------------

##Getting title for all movies
import numpy as np
from scipy.stats import mannwhitneyu

##Getting title for all movies
all_titles = data1.columns
count = 0

for i in range(400):
    
    ##We have data for "alone", now we need rows where they are bestalone and where they are notbestalone 475
    dataone = data1.loc[:,[all_titles[i], 'Movies are best enjoyed alone (1: Yes; 0: No; -1: Did not respond)']]
    dataone = dataone[np.isfinite(dataone)]
    
    notbestalone =  dataone.loc[dataAlone['Movies are best enjoyed alone (1: Yes; 0: No; -1: Did not respond)'] == 0 ].iloc[:,0]
    bestalone =  dataone.loc[dataAlone['Movies are best enjoyed alone (1: Yes; 0: No; -1: Did not respond)'] == 1 ].iloc[:,0]

    #Clean Data for two categories
    notbestalon = notbestalone[np.isfinite(notbestalone)]
    bestalon = bestalone[np.isfinite(bestalone)]
    # Mann-Whitney
    test88, p = mannwhitneyu(notbestalon, bestalon, alternative='two-sided') 

    #For-loop to count the number of movies that exhibit effect
    if p < 0.005:
        count += 1
        
proportion = count/400

print("The proportion is..." , proportion)
#Self Notes: -------------------------------------------------------------------------------
##Man-Whitney
##Language says "such-as", where question above defines to also do one-sided
##Define social watching-effect
## Why greater? or two-sided? two-sided because its a proportion
###2-sided = .025


# In[26]:


##QUESTION 9--------------------------------------------------------------------------
## Is the rating distribution of 'Home Alone' different than that of 'Finding Nemo'?
##------------------------------------------------------------------------------------

#Prunning
import numpy as np
from scipy import stats

##Unless we have it as a numpy array, we cannot run analysis
datanp = np.genfromtxt('/Users/jenniferrodrigueztrujillo/Downloads/movieReplicationSet.csv', delimiter = ',', skip_header = 1)
HA1 = datanp[:,285] #Home Alone
FN1 = datanp[:,138] #Finding Nemo

datanp = np.transpose(np.array([HA1,FN1])) # array of arrays

temp = np.array([np.isnan(HA1),np.isnan(FN1)],dtype=bool)
missingData = np.where(temp>0) # find participants with missing data
HA1 = np.delete(HA1,missingData) # delete missing data from array
FN1 = np.delete(FN1,missingData) # delete missing data from array

combinedData = np.transpose(np.array([HA1,FN1])) # array of arrays
##KS Test on M1 and M2
stats.ks_2samp(HA1, FN1, alternative='two-sided', mode='auto')

#Self NOTES:
#-row cleaning
#-We reject the null 
#- Why row? bECAUSE ONLY INTERESTED IN THE DISTRIBUTION, 
#_Since the quesition is asking if the distribution is different, we can keep eachu 
#sers perspective, easier to tell if we use the same users and they have different ratings
# If only inteested in the distribution, it does not matter if we do row or element wise


# In[27]:


##QUESTION 10---------------------------------------------------------------------------------
##    There are ratings on movies from several franchises 
##    ([‘Star Wars’, ‘Harry Potter’, ‘The Matrix’, ‘Indiana
##    Jones’, ‘Jurassic Park’, ‘Pirates of the Caribbean’, ‘Toy Story’, ‘Batman’]) 
##    in this dataset. How many of these are of inconsistent quality, as experienced 
##    by viewers? [Hint: You can use the keywords in quotation marks featured in this 
##    question to identify the movies that are part of each franchise]
#---------------------------------------------------------------------------------------------

import pandas as pd
#Key-words(movies) of interest
trilogylist = ["Star Wars", "Harry Potter", "The Matrix", "Indiana Jones", "Jurassic Park", "Pirates of the Caribbean", "Toy Story", "Batman"]

#Empty array for counter
counting_inconsistent = []

#For-loop to find
for f in trilogylist: 
    trilmatching = [s for s in data1.columns if f in s]
    print(trilmatching)
    #Cleaning data
    select_df = data1.loc[:,trilmatching].dropna()
    #Running Kruskal-Wallis
    arg = [select_df[l] for l in select_df]
    h,p = stats.kruskal(*arg)
    print(p)
#Self Notes:--------------------------------
#-Row-wise Removal( DROPNA)
#-Anova takes the means,
#-Null: of consistent quality(avrg rating is the same across all movies)
#    - within each series were they rated the same?
#    - can we use ANOVA? NO, because assumes it is normally distributed
#    - element-wise: takes the value out
#    - row-wise, for two independent values that may have different sizes, each movie is independent with
#    - theres only stat. sig. in qulaity for one movie: Harry Potter. 
    # Nonparametric tests equivalent to ANOVA - Kruskal-Wallis:
    # Same assumptions as above, but for more than 2 groups
    # h,p = stats.kruskal(combinedData[0],combinedData[1])


# In[14]:


## Extra Credit: Tell us something interesting and true (supported by a significance 
##    test of some kind) about the movies in this dataset that is not already covered by 
##    the questions above [for 5% of the grade score].
#-----------------------------------------------------------------------------------------


# In[15]:


##EXTRA Credit----------------------------------------------------------------------------
import numpy as np
from scipy.stats import mannwhitneyu

##Is enjoyment of 'What Women Want'(2000)' gendered, i.e. do male and female viewers rate it differently?
title= 'What Women Want' ##Prints column for 'What Women Want'
data.columns.get_loc('What Women Want (2000)')

#Gtabbing data for gender and movie
dataone = data.iloc[:,[284,474]]

##We have gender, now we need rows where they are female and where they are male 475
datafemaleWWW =  dataone.loc[dataone['Gender identity (1 = female; 2 = male; 3 = self-described)'] == 1 ]
datamaleWWW =  dataone.loc[dataone['Gender identity (1 = female; 2 = male; 3 = self-described)'] == 2 ]

#Placing data of interest into array 
datamalenpWWW = np.array(datamaleWWW['What Women Want (2000)'])
datafemalenpWWW = np.array(datafemaleWWW['What Women Want (2000)'])

#Cleaning data of interest
datafemWWW = datafemalenpWWW[np.isfinite(datafemalenpWWW)]
datamalWWW = datamalenpWWW[np.isfinite(datamalenpWWW)]

#Running MannWhitney
testmanWWW = mannwhitneyu(datafemWWW, datamalWWW, use_continuity=True, alternative='two-sided')

print(testmanWWW)
#Self Notes: -------------------------------------------------------------------------------
##Man-Whitney
#Null: Enjoyment of ''What Women Want'' gendered, male and female viewers DO NOT rate it differently
##Mann-Whitney:
    # Nonparametric tests equivalent to t-tests - Mann-Whitney U test:
    # Test for comparing medians of ordinal data (such as movie ratings)
    # from 2 groups 


# In[ ]:





# In[ ]:





# In[ ]:




