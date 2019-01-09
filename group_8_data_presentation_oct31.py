# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 00:21:49 2018

@author: ASUSNB
"""

import pandas as pd # data science essentials (read_excel, DataFrame)
import matplotlib.pyplot as plt # data visualization
import numpy as np
import seaborn as sns

file ='after_search_world_data_hult_regions_54 .xlsx'
sheet = pd.read_excel(file)

sheet 
sheet.info()

#Drop columns that miss too much columns
del(sheet["incidence_hiv"])
del(sheet["adult_literacy_pct"])
del(sheet["homicides_per_100k"])

#Change income group to numeric number

sheet["income_level"] = 0

for val in enumerate (sheet.loc[:,"income_group"]):
    print(val)
   
    if val[1] == 'Low income': 
        sheet.loc[val[0],"income_level"] = 1
    elif val[1] == 'Lower middle income':
        sheet.loc[val[0],"income_level"] = 2
    elif val[1] == 'Upper middle income':
        sheet.loc[val[0],"income_level"] = 3
    elif val[1] == 'High income':
        sheet.loc[val[0],"income_level"] = 4
        
    else: 
        sheet.loc[val[0],"income_level"] = 0

#Creat a subset of our team assigned region
team = sheet[sheet["Hult_Team_Regions"] == "Nothern Asia and Northern Pacific" ]
team.isnull().sum()



#Flag the missing values
for col in sheet:

    """ Create columns that are 0s if a value was not missing and 1 if
    a value is missing. """
    
    if sheet[col].isnull().any():
        sheet['m_'+col] = sheet[col].isnull().astype(int)

# check if all missing values have been identified
a = sheet.isnull().sum().sum()
b = sheet.iloc[:,-27:].sum().sum()


"""

"""

if a == b:
    print('All missing values accounted for.')
else:
    print('Some missing values may be unaccounted for, please audit.')


#Flag missing values in team region
for col in team:

    """ Create columns that are 0s if a value was not missing and 1 if
    a value is missing. """
    
    if team[col].isnull().any():
        team['m_'+col] = team[col].isnull().astype(int)
        

print(team)

team.isnull().sum().sum() == team.iloc[:,-17:].sum().sum()

#drop missing values
missing_values_df_1 = pd.DataFrame.copy(team)

missing_values_df = missing_values_df_1 .dropna().round(3)


#Create the histograms to see data distribution


#1
plt.hist(missing_values_df['access_to_electricity_pop'],
         bins = 25,
         color='blue',
         alpha = 0.3)
plt.title('access_to_electricity_pop')    # MEDIAN

#2
plt.hist(missing_values_df['access_to_electricity_rural'],
         bins = 25,
         color='blue',
         alpha = 0.3)
plt.title('access_to_electricity_rural')  # MEDIAN

#3
plt.hist(missing_values_df['access_to_electricity_urban'],
         bins = 25,
         color='blue',
         alpha = 0.3)
plt.title('access_to_electricity_urban')  # MEDIAN

#4
plt.hist(missing_values_df['CO2_emissions_per_capita)'],
         bins = 25,
         color='blue',
         alpha = 0.3)
plt.title('CO2_emissions_per_capita')     # MEDIAN

#5
plt.hist(missing_values_df['compulsory_edu_yrs'],
         bins = 25,
         color='blue',
         alpha = 0.3)
plt.title('compulsory_edu_yrs')  #MEAN

#6
plt.hist(missing_values_df['pct_female_employment'],
         bins = 25,
         color='blue',
         alpha = 0.3)
plt.title('pct_female_employment') #MEDIAN

#7
plt.hist(missing_values_df['pct_male_employment'],
         bins = 25,
         color='blue',
         alpha = 0.3)
plt.title('pct_male_employment') #MEDIAN

#8
plt.hist(missing_values_df['pct_agriculture_employment'],
         bins = 10,
         color='blue',
         alpha = 0.3)
plt.title('pct_agriculture_employment') #MEDIAN

#9
plt.hist(missing_values_df['pct_industry_employment'],
         bins = 25,
         color='blue',
         alpha = 0.3)
plt.title('pct_industry_employment') #MEDIAN

#10
plt.hist(missing_values_df['pct_services_employment'],
         bins = 70,
         color='blue',
         alpha = 0.3)
plt.title('pct_services_employment')   #MEAN

#11
plt.hist(missing_values_df['fdi_pct_gdp'],
         bins = 50,
         color='blue',
         alpha = 0.3)
plt.title('fdi_pct_gdp')  #MEDIAN

#12
plt.hist(missing_values_df['gdp_usd'],
         bins = 25,
         color='blue',
         alpha = 0.3)
plt.title('gdp_usd') #MEDIAN

#13
plt.hist(missing_values_df['gdp_growth_pct'],
         bins = 25,
         color='blue',
         alpha = 0.3)
plt.title('gdp_growth_pct') #MEDIAN

#14
plt.hist(missing_values_df['internet_usage_pct'],
         bins = 25,
         color='blue',
         alpha = 0.3)
plt.title('internet_usage_pct') #MEDIAN

#15
plt.hist(missing_values_df['child_mortality_per_1k'],
         bins = 25,
         color='blue',
         alpha = 0.3)
plt.title('child_mortality_per_1k') #MEDIAN

#16
plt.hist(missing_values_df['avg_air_pollution'],
         bins = 10,
         color='blue',
         alpha = 0.3)
plt.title('avg_air_pollution') #MEDIAN

#17
plt.hist(missing_values_df['women_in_parliament'],
         bins = 25,
         color='blue',
         alpha = 0.3)
plt.title('women_in_parliament') #MEDIAN

#18
plt.hist(missing_values_df['tax_revenue_pct_gdp'],
         bins = 50,
         color='blue',
         alpha = 0.3)
plt.title('tax_revenue_pct_gdp') #MEAN 

#19
plt.hist(missing_values_df['unemployment_pct'],
         bins = 25,
         color='blue',
         alpha = 0.3)
plt.title('unemployment_pct') #MEDIAN

#20
plt.hist(missing_values_df['urban_population_pct'],
         bins = 25,
         color='blue',
         alpha = 0.3)
plt.title('urban_population_pct') #MEDIAN

#21
plt.hist(missing_values_df['urban_population_growth_pct'],
         bins = 50,
         color='blue',
         alpha = 0.3)
plt.title('urban_population_growth_pct') #MEDIAN

#22
plt.hist(missing_values_df['exports_pct_gdp'],
         bins = 50,
         color='blue',
         alpha = 0.3)
plt.title('exports_pct_gdp') #MEDIAN



#INPUTATION WITH MEDIAN

    #DELETE 3 COLUMNS FOR MEAN

data_columns_median = pd.DataFrame.copy(missing_values_df_1)
del (data_columns_median["compulsory_edu_yrs"])
del (data_columns_median["pct_services_employment"])
del (data_columns_median["tax_revenue_pct_gdp"])


for col in data_columns_median:
    
    """ Impute missing values using the mean of each column """
    
    if data_columns_median[col].isnull().any():
        
        col_median = data_columns_median[col].median()
        
        data_columns_median[col] = data_columns_median[col].fillna(col_median).astype(int)

data_columns_median.isnull().sum()


#INPUTATION WITH MEAN


data_columns_mean = team.loc[:,['country_index','compulsory_edu_yrs','pct_services_employment','tax_revenue_pct_gdp']]

for col in data_columns_mean:
    
    """ Impute missing values using the mean of each column """
    
    if data_columns_mean[col].isnull().any():
        
        col_mean = data_columns_mean[col].mean()
        
        data_columns_mean[col] = data_columns_mean[col].fillna(col_mean).round(2)
        
data_columns_mean.isnull().sum()

#MERGE TWO FILLED DATASETS INTO NEW TEAM DATAFRAME

teamfilled = pd.merge(data_columns_mean,data_columns_median)

teamfilled.info()

teamfilled.to_excel('teamfilled.xlsx')

###################BEFORE IS REORGANIZED


# OUTLIER DETECTION through quantiles

    #OUTLIER FOR NORMAL DISTRIBUTED COLUMNS

file = ('teamfilled_arranged.xlsx')
teamfilled = pd.read_excel(file)

    #compulsory_edu_yrs -- no outliers


    #pct_services_employment
std2 = np.std([teamfilled['pct_services_employment']]).round(2)

services_employment_hi = (teamfilled['pct_services_employment'].mean()) + (3*(std2)) 
print(services_employment_hi.round(2))

services_employment_lo = (teamfilled['pct_services_employment'].mean()) - (3*(std2)) 
print(services_employment_lo.round(2))

    #tax_revenue_pct_gdp
std3 = np.std([teamfilled['tax_revenue_pct_gdp']]).round(2)

tax_revenue_hi = (teamfilled['tax_revenue_pct_gdp'].mean()) + (3*(std3)) 
print(tax_revenue_hi.round(2))

tax_revenue_lo = (teamfilled['tax_revenue_pct_gdp'].mean()) - (3*(std3)) 
print(tax_revenue_lo.round(2))

    #sumup

services_employment_hi = 72
services_employment_lo = 35

tax_revenue_hi = 23
tax_revenue_lo = 9

    #OUTLIER FOR REST OF COLUMNS

exports_pct_gdp_lo = 12
exports_pct_gdp_hi = 86

fdi_pct_gdp_hi = 8

gdp_usd_hi = 900000000000

gdp_growth_pct_lo = -4
gdp_growth_pct_hi = 9

urban_population_pct_lo = 52

urban_population_growth_pct_hi = 3.5

pct_agriculture_employment_lo = 10 
pct_agriculture_employment_hi = 48

pct_industry_employment_lo = 10
pct_industry_employment_hi = 25

#unemployment_pct_hi -- no outlier

#pct_male_employment -- no outlier

pct_female_employment_lo =1 #
pct_female_employment_hi = 28 #

women_in_parliament_hi = 27

access_to_electricity_pop_lo = 68

access_to_electricity_rural_lo = 64

access_to_electricity_urban_lo = 83

#internet_usage_pct -- no outlier

child_mortality_per_lo = 6
child_mortality_per_hi = 41

avg_air_pollution_lo = 8
avg_air_pollution_hi = 34

CO2_emissions_hi = 5

#Customize sns.distplot with outlier line

plt.subplot(2, 2, 1)
sns.distplot(teamfilled['compulsory_edu_yrs'],
             bins = 25,
             color = 'g')

plt.xlabel('education_years')
#################

plt.subplot(2, 2, 2)
sns.distplot(teamfilled['pct_services_employment'],
             bins = 30,
             color = 'b')

plt.xlabel('pct_services_employment')



plt.axvline(x = services_employment_hi,
            label = 'Outlier Thresholds',
            linestyle = '--')

plt.axvline(x = services_employment_lo,
            label = 'Outlier Thresholds',
            linestyle = '--')
#################

plt.subplot(2, 2, 3)
sns.distplot(teamfilled['tax_revenue_pct_gdp'],
             bins = 25,
             color = 'r')

plt.xlabel('tax_revenue_pct_gdp')



plt.axvline(x = tax_revenue_hi,
            label = 'Outlier Thresholds',
            linestyle = '--')

plt.axvline(x = tax_revenue_lo,
            label = 'Outlier Thresholds',
            linestyle = '--')

plt.tight_layout()
plt.savefig('team_normal_distribution_variables.png')
plt.show()
################
################

plt.subplot(2, 2, 4)
sns.distplot(teamfilled['exports_pct_gdp'],
             bins = 25,
             color = 'purple')

plt.xlabel('exports_pct_gdp')



plt.axvline(x = exports_pct_gdp_lo,
            label = 'Outlier Thresholds',
            linestyle = '--')

plt.axvline(x = exports_pct_gdp_hi,
            label = 'Outlier Thresholds',
            linestyle = '--')
################

plt.subplot(3, 3, 2)
sns.distplot(teamfilled['fdi_pct_gdp'],
             bins = 25,
             color = 'purple')
            

plt.xlabel('fdi_pct_gdp')



plt.axvline(x = fdi_pct_gdp_hi,
            label = 'Outlier Thresholds',
            linestyle = '--')
################

plt.subplot(3, 3, 3)
sns.distplot(teamfilled['gdp_usd'],
             bins = 'fd',
             color = 'purple')

plt.xlabel('gdp_usd')



plt.axvline(x = gdp_usd_hi,
            label = 'Outlier Thresholds',
            linestyle = '--')
################

plt.subplot(3, 3, 4)
sns.distplot(teamfilled['gdp_growth_pct'],
             bins = 25,
             color = 'purple')

plt.xlabel('gdp_growth_pct')



plt.axvline(x = gdp_growth_pct_lo,
            label = 'Outlier Thresholds',
            linestyle = '--')

plt.axvline(x = gdp_growth_pct_hi,
            label = 'Outlier Thresholds',
            linestyle = '--')
################

plt.subplot(3, 3, 5)
sns.distplot(teamfilled['urban_population_pct'],
             bins = 25,
             color = 'orange')

plt.xlabel('urban_population_pct')



plt.axvline(x = urban_population_pct_lo,
            label = 'Outlier Thresholds',
            linestyle = '--')
################

plt.subplot(3, 3, 6)
sns.distplot(teamfilled['urban_population_growth_pct'],
             bins = 25,
             color = 'orange')

plt.xlabel('urban_population_growth_pct')



plt.axvline(x = urban_population_growth_pct_hi,
            label = 'Outlier Thresholds',
            linestyle = '--')
################

plt.subplot(3, 3, 7)
sns.distplot(teamfilled['pct_agriculture_employment'],
             bins = 25,
             color = 'pink')

plt.xlabel('pct_agriculture_employment')



plt.axvline(x = pct_agriculture_employment_lo,
            label = 'Outlier Thresholds',
            linestyle = '--')

plt.axvline(x = pct_agriculture_employment_hi,
            label = 'Outlier Thresholds',
            linestyle = '--')
################

plt.subplot(3, 3, 8)
sns.distplot(teamfilled['pct_industry_employment'],
             bins = 25,
             color = 'pink')

plt.xlabel('pct_industry_employment')



plt.axvline(x = pct_industry_employment_lo,
            label = 'Outlier Thresholds',
            linestyle = '--')

plt.axvline(x = pct_industry_employment_hi,
            label = 'Outlier Thresholds',
            linestyle = '--')
################

plt.subplot(3, 3, 9)
sns.distplot(teamfilled['unemployment_pct'],
             bins = 25,
             color = 'pink')

plt.xlabel('unemployment_pct')





plt.tight_layout()
plt.savefig('team_rest_of_variables_1.png')
plt.show()
################
################

plt.subplot(3, 3, 1)
sns.distplot(teamfilled['pct_male_employment'],
             bins = 25,
             color = 'red')

plt.xlabel('pct_male_employment')
################

plt.subplot(3, 3, 2)
sns.distplot(teamfilled['pct_female_employment'],
             bins = 25,
             color = 'red')

plt.xlabel('pct_female_employment')



plt.axvline(x = pct_female_employment_lo ,
            label = 'Outlier Thresholds',
            linestyle = '--')

plt.axvline(x = pct_female_employment_hi ,
            label = 'Outlier Thresholds',
            linestyle = '--')
################

plt.subplot(3, 3, 3)
sns.distplot(teamfilled['women_in_parliament'],
             bins = 25,
             color = 'red')

plt.xlabel('women_in_parliament')



plt.axvline(x = women_in_parliament_hi,
            label = 'Outlier Thresholds',
            linestyle = '--')
################

plt.subplot(3, 3, 4)
sns.distplot(teamfilled['access_to_electricity_pop'],
             bins = 25,
             color = 'brown')

plt.xlabel('access_to_electricity_pop')



plt.axvline(x = access_to_electricity_pop_lo,
            label = 'Outlier Thresholds',
            linestyle = '--')
################

plt.subplot(3, 3, 5)
sns.distplot(teamfilled['access_to_electricity_rural'],
             bins = 25,
             color = 'brown')

plt.xlabel('access_to_electricity_rural')



plt.axvline(x = access_to_electricity_rural_lo,
            label = 'Outlier Thresholds',
            linestyle = '--')
################

plt.subplot(3, 3, 6)
sns.distplot(teamfilled['access_to_electricity_urban'],
             bins = 25,
             color = 'brown')

plt.xlabel('access_to_electricity_urban')



plt.axvline(x = access_to_electricity_urban_lo,
            label = 'Outlier Thresholds',
            linestyle = '--')
################

plt.subplot(3, 3, 7)
sns.distplot(teamfilled['internet_usage_pct'],
             bins = 25,
             color = 'brown')

plt.xlabel('internet_usage_pct')

plt.tight_layout()
plt.savefig('team_rest_of_variables_2.png')
plt.show()
################
################

plt.subplot(2, 2, 1)
sns.distplot(teamfilled['child_mortality_per_1k'],
             bins = 25,
             color = 'gray')

plt.xlabel('child_mortality_per_1k')



plt.axvline(x = child_mortality_per_lo,
            label = 'Outlier Thresholds',
            linestyle = '--')

plt.axvline(x = child_mortality_per_hi,
            label = 'Outlier Thresholds',
            linestyle = '--')
################

plt.subplot(2, 2, 2)
sns.distplot(teamfilled['avg_air_pollution'],
             bins = 25,
             color = 'green')

plt.xlabel('avg_air_pollution')



plt.axvline(x = avg_air_pollution_lo,
            label = 'Outlier Thresholds',
            linestyle = '--')

plt.axvline(x = avg_air_pollution_hi,
            label = 'Outlier Thresholds',
            linestyle = '--')
################

plt.subplot(2, 2, 3)
sns.distplot(teamfilled['CO2_emissions_per_capita)'],
             bins = 25,
             color = 'green')

plt.xlabel('CO2_emissions_per_capita)')



plt.axvline(x = CO2_emissions_hi,
            label = 'Outlier Thresholds',
            linestyle = '--')

plt.tight_layout()
plt.savefig('team_rest_of_variables_3.png')
plt.show()
################

###############################################################################
# CREATING COLUMNS TO FLAG OUTLIERS 
###############################################################################



# Writing a variable for outlier flags
teamfilled['out_pct_services_employment'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'pct_services_employment']):
    
    
    if val[1] < services_employment_lo: 
        teamfilled.loc[val[0], 'out_pct_services_employment'] = -1


    if val[1] > services_employment_hi:
        teamfilled.loc[val[0], 'out_pct_services_employment'] = 1

teamfilled['out_pct_services_employment'].abs().sum()


check = (teamfilled.loc[ : , ['pct_services_employment', 'out_pct_services_employment']]
                             .sort_values(['pct_services_employment'],
                                          ascending = False))        
################

teamfilled['out_tax_revenue_pct_gdp'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'tax_revenue_pct_gdp']):
    
    
    if val[1] < tax_revenue_lo: 
        teamfilled.loc[val[0], 'out_tax_revenue_pct_gdp'] = -1


    if val[1] > tax_revenue_hi:
        teamfilled.loc[val[0], 'out_tax_revenue_pct_gdp'] = 1

teamfilled['out_tax_revenue_pct_gdp'].abs().sum()


check = (teamfilled.loc[ : , ['tax_revenue_pct_gdp', 'out_tax_revenue_pct_gdp']]
                             .sort_values(['tax_revenue_pct_gdp'],
                                          ascending = False))       
################

teamfilled['out_exports_pct_gdp'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'exports_pct_gdp']):
    
    
    if val[1] < exports_pct_gdp_lo: 
        teamfilled.loc[val[0], 'out_exports_pct_gdp'] = -1


    if val[1] > exports_pct_gdp_hi:
        teamfilled.loc[val[0], 'out_exports_pct_gdp'] = 1

teamfilled['out_exports_pct_gdp'].abs().sum()


check = (teamfilled.loc[ : , ['exports_pct_gdp', 'out_exports_pct_gdp']]
                             .sort_values(['exports_pct_gdp'],
                                          ascending = False))       
################

teamfilled['out_fdi_pct_gdp'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'fdi_pct_gdp']):



    if val[1] > fdi_pct_gdp_hi:
        teamfilled.loc[val[0], 'out_fdi_pct_gdp'] = 1

teamfilled['out_fdi_pct_gdp'].abs().sum()


check = (teamfilled.loc[ : , ['fdi_pct_gdp', 'out_fdi_pct_gdp']]
                             .sort_values(['fdi_pct_gdp'],
                                          ascending = False))       
################

teamfilled['out_gdp_usd'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'gdp_usd']):



    if val[1] > gdp_usd_hi:
        teamfilled.loc[val[0], 'out_gdp_usd'] = 1

teamfilled['out_gdp_usd'].abs().sum()


check = (teamfilled.loc[ : , ['gdp_usd', 'out_gdp_usd']]
                             .sort_values(['gdp_usd'],
                                          ascending = False))       

################

teamfilled['out_gdp_growth_pct'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'gdp_growth_pct']):



    if val[1] > gdp_growth_pct_hi:
        teamfilled.loc[val[0], 'out_gdp_growth_pct'] = 1
        
    if val[1] < gdp_growth_pct_lo:
        teamfilled.loc[val[0], 'out_gdp_growth_pct'] = -1

teamfilled['out_gdp_growth_pct'].abs().sum()


check = (teamfilled.loc[ : , ['gdp_growth_pct', 'out_gdp_growth_pctd']]
                             .sort_values(['gdp_growth_pct'],
                                          ascending = False)) 

################

teamfilled['out_gdp_growth_pct'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'gdp_growth_pct']):



    if val[1] > gdp_growth_pct_hi:
        teamfilled.loc[val[0], 'out_gdp_growth_pct'] = 1
        
    if val[1] < gdp_growth_pct_lo:
        teamfilled.loc[val[0], 'out_gdp_growth_pct'] = -1

teamfilled['out_gdp_growth_pct'].abs().sum()


check = (teamfilled.loc[ : , ['gdp_growth_pct', 'out_gdp_growth_pctd']]
                             .sort_values(['gdp_growth_pct'],
                                          ascending = False))        
################

teamfilled['out_urban_population_pct'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'urban_population_pct']):


        
    if val[1] < urban_population_pct_lo:
        teamfilled.loc[val[0], 'out_urban_population_pct'] = -1

teamfilled['out_urban_population_pct'].abs().sum()


check = (teamfilled.loc[ : , ['urban_population_pct', 'out_urban_population_pct']]
                             .sort_values(['urban_population_pct'],
                                          ascending = False))        
################

teamfilled['out_urban_population_growth_pct'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'urban_population_growth_pct']):


        
    if val[1] > urban_population_growth_pct_hi:
        teamfilled.loc[val[0], 'out_urban_population_growth_pct'] = 1

teamfilled['out_urban_population_growth_pct'].abs().sum()


check = (teamfilled.loc[ : , ['urban_population_growth_pct', 'out_urban_population_growth_pct']]
                             .sort_values(['urban_population_growth_pct'],
                                          ascending = False))     
################

teamfilled['out_pct_agriculture_employment'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'pct_agriculture_employment']):


        
    if val[1] > pct_agriculture_employment_hi:
        teamfilled.loc[val[0], 'out_pct_agriculture_employment'] = 1
        
    if val[1] < pct_agriculture_employment_lo:
        teamfilled.loc[val[0], 'out_urban_population_pct'] = -1

teamfilled['out_pct_agriculture_employment'].abs().sum()


check = (teamfilled.loc[ : , ['pct_agriculture_employment', 'out_pct_agriculture_employment']]
                             .sort_values(['pct_agriculture_employment'],
                                          ascending = False))     

################

teamfilled['out_pct_industry_employment'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'pct_industry_employment']):


        
    if val[1] > pct_industry_employment_hi:
        teamfilled.loc[val[0], 'out_pct_industry_employment'] = 1
        
    if val[1] < pct_industry_employment_lo:
        teamfilled.loc[val[0], 'out_pct_industry_employment'] = -1

teamfilled['out_pct_industry_employment'].abs().sum()


check = (teamfilled.loc[ : , ['pct_industry_employment', 'out_pct_industry_employment']]
                             .sort_values(['pct_industry_employment'],
                                          ascending = False))     

################

teamfilled['out_pct_female_employment'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'pct_female_employment']):


        
    if val[1] > pct_female_employment_hi:
        teamfilled.loc[val[0], 'out_pct_female_employment'] = 1
        
    if val[1] < pct_female_employment_lo:
        teamfilled.loc[val[0], 'out_pct_female_employment'] = -1
        
    

teamfilled['out_pct_female_employment'].abs().sum()


check = (teamfilled.loc[ : , ['pct_female_employment', 'out_pct_female_employment']]
                             .sort_values(['pct_female_employment'],
                                          ascending = False)) 
################

teamfilled['out_women_in_parliament'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'women_in_parliament']):


        

        
    if val[1] > pct_female_employment_hi:
        teamfilled.loc[val[0], 'out_women_in_parliament'] = 1
        
    

teamfilled['out_women_in_parliament'].abs().sum()


check = (teamfilled.loc[ : , ['women_in_parliament', 'out_women_in_parliament']]
                             .sort_values(['women_in_parliament'],
                                          ascending = False))

################

teamfilled['out_women_in_parliament'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'women_in_parliament']):


        

        
    if val[1] > pct_female_employment_hi:
        teamfilled.loc[val[0], 'out_women_in_parliament'] = 1
        
    

teamfilled['out_women_in_parliament'].abs().sum()


check = (teamfilled.loc[ : , ['women_in_parliament', 'out_women_in_parliament']]
                             .sort_values(['women_in_parliament'],
                                          ascending = False))

################

teamfilled['out_access_to_electricity_pop'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'access_to_electricity_pop']):


        

        
    if val[1] < access_to_electricity_pop_lo:
        teamfilled.loc[val[0], 'out_access_to_electricity_pop'] = -1
        
    

teamfilled['out_access_to_electricity_pop'].abs().sum()


check = (teamfilled.loc[ : , ['access_to_electricity_pop', 'out_access_to_electricity_pop']]
                             .sort_values(['access_to_electricity_pop'],
                                          ascending = False))

################

teamfilled['out_access_to_electricity_rural'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'access_to_electricity_rural']):


        

        
    if val[1] < access_to_electricity_rural_lo:
        teamfilled.loc[val[0], 'out_access_to_electricity_rural'] = -1
        
    

teamfilled['out_access_to_electricity_rural'].abs().sum()


check = (teamfilled.loc[ : , ['access_to_electricity_rural', 'out_access_to_electricity_rural']]
                             .sort_values(['access_to_electricity_rural'],
                                          ascending = False))
################

teamfilled['out_access_to_electricity_urban'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'access_to_electricity_urban']):


        

        
    if val[1] < access_to_electricity_urban_lo:
        teamfilled.loc[val[0], 'out_access_to_electricity_urban'] = -1
        
    

teamfilled['out_access_to_electricity_urban'].abs().sum()


check = (teamfilled.loc[ : , ['access_to_electricity_urban', 'out_access_to_electricity_urban']]
                             .sort_values(['access_to_electricity_urban'],
                                          ascending = False))

################

teamfilled['out_access_to_electricity_urban'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'access_to_electricity_urban']):


        

        
    if val[1] < access_to_electricity_urban_lo:
        teamfilled.loc[val[0], 'out_access_to_electricity_urban'] = -1
        
    

teamfilled['out_access_to_electricity_urban'].abs().sum()


check = (teamfilled.loc[ : , ['access_to_electricity_urban', 'out_access_to_electricity_urban']]
                             .sort_values(['access_to_electricity_urban'],
                                          ascending = False))

################

teamfilled['out_child_mortality_per_1k'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'child_mortality_per_1k']):


        
    if val[1] > child_mortality_per_hi:
        teamfilled.loc[val[0], 'out_child_mortality_per_1k'] = 1
        
        
    if val[1] < child_mortality_per_lo:
        teamfilled.loc[val[0], 'out_child_mortality_per_1k'] = -1
        
    

teamfilled['out_child_mortality_per_1k'].abs().sum()


check = (teamfilled.loc[ : , ['child_mortality_per_1k', 'out_child_mortality_per_1k']]
                             .sort_values(['child_mortality_per_1k'],
                                          ascending = False))

################

teamfilled['out_avg_air_pollution'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'avg_air_pollution']):


        
    if val[1] > avg_air_pollution_hi:
        teamfilled.loc[val[0], 'out_avg_air_pollution'] = 1
        
        
    if val[1] < avg_air_pollution_lo:
        teamfilled.loc[val[0], 'out_avg_air_pollution'] = -1
        
    

teamfilled['out_avg_air_pollution'].abs().sum()


check = (teamfilled.loc[ : , ['avg_air_pollution', 'out_avg_air_pollution']]
                             .sort_values(['avg_air_pollution'],
                                          ascending = False))

################

teamfilled['out_CO2_emissions_per_capita)'] = 0


# Building a for loop
for val in enumerate(teamfilled.loc[ : , 'CO2_emissions_per_capita)']):


        
    if val[1] > CO2_emissions_hi:
        teamfilled.loc[val[0], 'out_CO2_emissions_per_capita)'] = 1
        
        
    

teamfilled['out_CO2_emissions_per_capita)'].abs().sum()


check = (teamfilled.loc[ : , ['CO2_emissions_per_capita)', 'out_CO2_emissions_per_capita)']]
                             .sort_values(['CO2_emissions_per_capita)'],
                                          ascending = False))
########################
# Analyzing outlier flags
########################


teamfilled['out_sum'] = (teamfilled['out_pct_services_employment']   +
                       teamfilled['out_tax_revenue_pct_gdp']   +
                       teamfilled['out_exports_pct_gdp']   +
                       teamfilled['out_fdi_pct_gdp'] +
                       teamfilled['out_gdp_usd']+
                       teamfilled['out_gdp_growth_pct']+
                       teamfilled['out_urban_population_pct']+
                       teamfilled['out_urban_population_growth_pct']+
                       teamfilled['out_pct_agriculture_employment']+
                       teamfilled['out_pct_industry_employment']+
                       teamfilled['out_pct_female_employment']+
                       teamfilled['out_women_in_parliament']+
                       teamfilled['out_access_to_electricity_pop']+
                       teamfilled['out_access_to_electricity_rural']+
                       teamfilled['out_access_to_electricity_urban']+
                       teamfilled['out_child_mortality_per_1k']+
                       teamfilled['out_CO2_emissions_per_capita)']+
                       teamfilled['out_avg_air_pollution'])


###############################################################################
# Saving things for future use
###############################################################################

teamfilled.to_excel('teamfilled_flagged.xlsx', index = False)


# ANALYSIS

file ='teamfilled_flagged.xlsx'
teamfilled = pd.read_excel(file)


###############################################################################
# Correlation analysis
###############################################################################


# We can find the correlation between two variables using np.corrcoef
y = pd.np.corrcoef(teamfilled['pct_agriculture_employment'],
                   teamfilled['pct_industry_employment']).round(2)

print(y)



# We can generate a single correlation coefficient by specifying [1, 0] 
pd.np.corrcoef(teamfilled['pct_agriculture_employment'],
               teamfilled['pct_industry_employment'])[1,0].round(2)


# See Footnote 1 for an explanation of the code above


"""
Use the space below to check other correlations with pd.np.corrcoef
"""



########################
# Correlation matricies
########################

team_corr = teamfilled.corr().round(2)

print(team_corr)

# Sending df_corr to Excel
team_corr.to_excel("team_corr_matrix.xlsx")



"""
Let's focus on how price relates to other variables. We can do so with
the code below.
"""

team_corr.loc['gdp_usd'].sort_values(ascending = False)
team_corr.loc['pct_agriculture_employment'][team_corr['pct_agriculture_employment']>=0.5].sort_values(ascending = False)
team_corr.loc['CO2_emissions_per_capita)'][team_corr['CO2_emissions_per_capita)']<=-0.5].sort_values(ascending = False)

##
team_corr.loc['CO2_emissions_per_capita)'][team_corr['CO2_emissions_per_capita)']>=0.5].sort_values(ascending = False)

#######################
#######################
#Drop outlier flagged columns before analysis

teamfilled_analysis = pd.DataFrame.copy(teamfilled)
teamfilled_analysis = teamfilled_analysis.drop(teamfilled_analysis.columns[-19:], axis=1) 
print(teamfilled_analysis)


#Create a subset with team region and world data for later analysis

world = sheet.iloc[[217],:]
del (world["m_urban_population_pct"])
del (world["m_urban_population_growth_pct"]) 
del (world["m_compulsory_edu_yrs"])  
del (world["m_access_to_electricity_pop"]) 
del (world["m_access_to_electricity_urban"])  

teamfilled_world = teamfilled_analysis.append(world)

teamfilled_world.to_excel('teamfilled_world.xlsx')


#Choose South Asia for region comparison because of geographically simillar, similar numbe of country, similar income group segment
south_asia = sheet[sheet["Hult_Team_Regions"] == "Southern Asia and Southern Pacific" ]

south_asia.info()
team.info()

south_asia_describe = south_asia.describe()

#Create a subset with team region, world data, South Asia region for later analysis

del (south_asia["m_urban_population_pct"])
del (south_asia["m_urban_population_growth_pct"]) 
del (south_asia["m_compulsory_edu_yrs"])  
del (south_asia["m_access_to_electricity_pop"]) 
del (south_asia["m_access_to_electricity_urban"])  


#Using Histogram Plot to determine whether to fill in missing data with Median or Mean

southasia_missing = pd.DataFrame.copy(south_asia)
southasia_dropped = southasia_missing.dropna().round(3)

plt.hist(southasia_dropped['exports_pct_gdp'], bins = 50)
plt.show()  #Median

plt.hist(southasia_dropped['fdi_pct_gdp'], bins = 50)
plt.show() #Median

plt.hist(southasia_dropped['gdp_usd'], bins = 50)
plt.show() #Median

plt.hist(southasia_dropped['gdp_growth_pct'], bins = 25)
plt.show() #Median

plt.hist(southasia_dropped['tax_revenue_pct_gdp'], bins = 10)
plt.show() #Median

plt.hist(southasia_dropped['urban_population_pct'], bins = 50)
plt.show() #Median

plt.hist(southasia_dropped['urban_population_growth_pct'], bins = 10)
plt.show() #Median

plt.hist(southasia_dropped['pct_agriculture_employment'], bins = 50)
plt.show() #Median

plt.hist(southasia_dropped['pct_industry_employment'], bins = 50)
plt.show() #Median

plt.hist(southasia_dropped['pct_services_employment'], bins = 10)
plt.show() #Median

plt.hist(southasia_dropped['unemployment_pct'], bins = 50)
plt.show() #Median

plt.hist(southasia_dropped['pct_male_employment'], bins = 50)
plt.show() #Median

plt.hist(southasia_dropped['pct_female_employment'], bins = 50)
plt.show() #Median

plt.hist(southasia_dropped['women_in_parliament'], bins = 50)
plt.show() #Median

plt.hist(southasia_dropped['compulsory_edu_yrs'], bins = 50)
plt.show() #Mean

plt.hist(southasia_dropped['access_to_electricity_pop'], bins = 50)
plt.show() #Median

plt.hist(southasia_dropped['access_to_electricity_rural'], bins = 50)
plt.show() #Median

plt.hist(southasia_dropped['access_to_electricity_urban'], bins = 50)
plt.show() #Median

plt.hist(southasia_dropped['internet_usage_pct'], bins = 50)
plt.show() #Mean

plt.hist(southasia_dropped['child_mortality_per_1k'], bins = 25)
plt.show() #Median

plt.hist(southasia_dropped['avg_air_pollution'], bins = 50)
plt.show() #Median

plt.hist(southasia_dropped['CO2_emissions_per_capita)'], bins = 50)
plt.show() #Median

#Imputation

#INPUTATION WITH MEDIAN

    
for col in south_asia:
    
    """ Impute missing values using the mean of each column """
    
    if south_asia[col].isnull().any():
        
       south_asia_median = south_asia[col].median()
        
       south_asia[col] = south_asia[col].fillna(south_asia_median).round(2)

south_asia.isnull().sum()

#Combine with teamfilled_world
teamfilled_world_southasia = teamfilled_world.append(south_asia)
teamfilled_world_southasia.isnull().sum()

teamfilled_world_southasia.to_excel('teamfilled_world_southasia.xlsx')

#Combine with teafilled

teamfilled_southasia = teamfilled_analysis.append(south_asia)
teamfilled_southasia.isnull().sum()
teamfilled_southasia.to_excel('teamfilled_southasia.xlsx')

#Analyze the correlation among North, South Asia and the world

pd.np.corrcoef(teamfilled_world_southasia['pct_agriculture_employment'],
               teamfilled_world_southasia['pct_industry_employment'])[1,0].round(2)


# See Footnote 1 for an explanation of the code above


"""
Use the space below to check other correlations with pd.np.corrcoef
"""
########################
#create a subset of north europe and north america

europe_northamerica = sheet[sheet["Hult_Team_Regions"] == "Northern Europe and Northern Americas" ]

europe_northamerica.info()
europe_northamerica.info()

europe_northamerica_describe = europe_northamerica.describe()

#Create a subset with team region, world data, South Asia region for later analysis

del (europe_northamerica["m_urban_population_pct"])
del (europe_northamerica["m_urban_population_growth_pct"]) 
del (europe_northamerica["m_compulsory_edu_yrs"])  
del (europe_northamerica["m_access_to_electricity_pop"]) 
del (europe_northamerica["m_access_to_electricity_urban"])  

#INPUTATION WITH MEDIAN

    
for col in europe_northamerica:
    
    """ Impute missing values using the mean of each column """
    
    if europe_northamerica[col].isnull().any():
        
       europe_northamerica_median = europe_northamerica[col].median()
        
       europe_northamerica[col] = europe_northamerica[col].fillna(europe_northamerica_median).round(2)

europe_northamerica.isnull().sum()

#Combine with teamfilled_world_southasia
teamfilled_world_southasia_eu = teamfilled_world_southasia.append(europe_northamerica)
teamfilled_world_southasia_eu.isnull().sum()

teamfilled_world_southasia_eu.to_excel('teamfilled_world_southasia_eu.xlsx')

#Combine with teamfilled_southasia

teamfilled_southasia_eu = teamfilled_southasia.append(europe_northamerica)
teamfilled_southasia_eu.isnull().sum()
teamfilled_southasia_eu.to_excel('teamfilled_southasia_eu.xlsx')


########################
# Correlation matricies
########################

team_southasia_world_corr = teamfilled_world_southasia.corr().round(2)

print(team_southasia_world_corr)

# Sending df_corr to Excel
team_southasia_world_corr.to_excel("team_southasia_world_corr_matrix.xlsx")



team_corr.loc['income_level'][team_corr['income_level']>=0.5].sort_values(ascending = False)
##

team_corr.loc['income_level'][team_corr['income_level']>=0.5].sort_values(ascending = False)



########################
# 1 region
########################

# income level and GDP
plt.scatter(x = 'income_level',
            y = 'CO2_emissions_per_capita)',
            alpha = 0.7,
            cmap = 'bwr',
            data = teamfilled)

plt.title('North Asia')
plt.xlabel('income level')
plt.ylabel('CO2_emissions')
plt.grid(True)
plt.show()

########################
# Adding subplots
########################

plt.subplot(2, 2, 1)

plt.scatter(x = 'fdi_pct_gdp',
            y = 'exports_pct_gdp',
            alpha = 0.7,
            color = 'red',
            data = teamfilled)


plt.title('fdi_pct_gdp')
plt.ylabel('exports_pct_gdp')
plt.grid(True)



########################



plt.subplot(2, 2, 2)

plt.scatter(x = 'urban_population_pct',
            y = 'exports_pct_gdp',
            alpha = 0.7,
            color = 'magenta',
            data = teamfilled
            )


plt.title('urban_population_pct')
plt.grid(True)



########################



plt.subplot(2, 2, 3)

plt.scatter(x = 'internet_usage_pct',
            y = 'exports_pct_gdp',
            alpha = 0.7,
            color = 'magenta',
            data = teamfilled)


plt.title('internet_usage_pct')
plt.ylabel('exports_pct_gdp')
plt.grid(True)



########################



plt.subplot(2, 2, 4)

plt.scatter(x = 'pct_services_employment',
            y = 'exports_pct_gdp',
            alpha = 0.7,
            color = 'magenta',
            data = teamfilled)


plt.title('pct_services_employment')

plt.grid(True)
plt.tight_layout()
plt.savefig('Teamfilled Scattersubplots_exportgroup.png')
plt.show()
####################
####################
plt.subplot(2, 2, 1)

plt.scatter(x = 'internet_usage_pct',
            y = 'pct_services_employment',
            alpha = 0.7,
            color = 'orange',
            data = teamfilled)


plt.title('internet_usage_pct')
plt.ylabel('pct_services_employment')
plt.grid(True)



########################



plt.subplot(2, 2, 2)

plt.scatter(x = 'access_to_electricity_urban',
            y = 'pct_services_employment',
            alpha = 0.7,
            color = 'navy',
            data = teamfilled
            )


plt.title('access_to_electricity_urban')
plt.grid(True)



########################



plt.subplot(2, 2, 3)

plt.scatter(x = 'access_to_electricity_rural',
            y = 'pct_services_employment',
            alpha = 0.7,
            color = 'navy',
            data = teamfilled)


plt.title('access_to_electricity_rural')
plt.ylabel('pct_services_employment')
plt.grid(True)




########################



plt.subplot(2, 2, 4)

plt.scatter(x = 'access_to_electricity_pop',
            y = 'pct_services_employment',
            alpha = 0.7,
            color = 'orange',
            data = teamfilled)


plt.title('access_to_electricity_pop')

plt.grid(True)
plt.tight_layout()
plt.savefig('Teamfilled Scattersubplots_service.png')
plt.show()

###
team_fdi_median = teamfilled['fdi_pct_gdp'].median() 
world_list = list(world.values.flatten())
world_fdi = world_list[6]

fig = plt.figure(figsize = (2,3))

ax = fig.add_subplot(111)

x = ['North_Asia','World']

y = [team_fdi_median , world_fdi]

ax.bar(np.arange(len(x)),y, )

ax.set_xticklabels(x, rotation = 45)

###CO2
sns.pairplot(data = teamfilled,
             x_vars = ['pct_services_employment', 'urban_population_pct', 'internet_usage_pct'],
             y_vars = ['CO2_emissions_per_capita)'],
             hue = 'income_level', palette = 'plasma')



plt.savefig('CO2_compared with multiple.png')
plt.show()

###CO2 & air pollution

sns.jointplot(x = 'CO2_emissions_per_capita)',
                     y = 'urban_population_pct',
                     kind = 'reg',
                     joint_kws={'color':'blue'},
                     data = teamfilled)


plt.tight_layout()
plt.show()

########################
# Pairplots
########################


# this can be further focused using subsetting
teamfilled_employment = teamfilled.loc[:,['pct_agriculture_employment', 'pct_industry_employment', 'unemployment_pct', 'pct_male_employment', 'pct_female_employment']]
sns.pairplot(data = teamfilled_employment)
plt.tight_layout()
plt.show()


sns.pairplot(teamfilled_employment)

# 3 variables using hue
sns.pairplot(data = teamfilled,
             x_vars = ['access_to_electricity_pop', 'access_to_electricity_rural', 'access_to_electricity_urban', 'internet_usage_pct'],
             y_vars = ['access_to_electricity_pop', 'access_to_electricity_rural', 'access_to_electricity_urban', 'internet_usage_pct'],
             hue = 'income_level', palette = 'plasma')


plt.tight_layout()
plt.savefig('pairplot_electricity.png')
plt.show()

# Filtering to focus on their relationship with price
sns.pairplot(data = teamfilled,
             x_vars = ['access_to_electricity_pop', 'access_to_electricity_rural', 'internet_usage_pct'],
             y_vars = ['CO2_emissions_per_capita'],
             hue = 'income_group', palette = 'plasma')


plt.tight_layout()
plt.savefig('gdp_electricity.png')
plt.show()

#########

sns.pairplot(data = teamfilled_world_southasia,
             x_vars = ['pct_services_employment',  'urban_population_pct', 'access_to_electricity_urban', 'internet_usage_pct'],
             y_vars = ['urban_population_pct'],
             hue = 'Hult_Team_Regions', palette = 'plasma'
            )



plt.savefig('south_income_multiplecol.png')
plt.show()

sns.pairplot(data = teamfilled,
             x_vars = ['urban_population_pct', 'child_mortality_per_1k'],
             y_vars = ['income_level'],
             palette = 'plasma'
            )



plt.savefig('south_income_multiplecol.png')
plt.show()
###############
###############

# scatter plot with trendline and categorical variables
sns.lmplot(x = 'pct_agriculture_employment',
           y = 'pct_male_employment',
           data = teamfilled,
           hue = 'income_group',
           fit_reg = False,
           palette = 'plasma')

sns.lmplot(x = 'pct_services_employment',
           y = 'pct_male_employment',
           data = teamfilled,
           hue = 'income_group',
           fit_reg = False,
           palette = 'plasma')

sns.lmplot(x = 'pct_agriculture_employment',
           y = 'pct_female_employment',
           data = teamfilled,
           hue = 'income_group',
           fit_reg = False,
           palette = 'plasma')

sns.lmplot(x = 'pct_services_employment',
           y = 'pct_female_employment',
           data = teamfilled,
           hue = 'income_group',
           fit_reg = False,
           palette = 'plasma')

#########


#########


sns.lmplot(x = 'avg_air_pollution',
           y = 'CO2_emissions_per_capita)',
           data = teamfilled,
           fit_reg = True,
           hue= 'income_group',
           scatter_kws= {"marker": "D", 
                        "s": 30},
           palette = 'plasma',
           )

plt.lengend(loc = 'upper right')
plt.title("divided by income level")
plt.grid()
plt.tight_layout()
plt.show()

##########

sns.lmplot(x = 'income_level',
           y = 'urban_population_pct',
           data = teamfilled_southasia,
           fit_reg = True,
           hue= 'Hult_Team_Regions',
           col= 'Hult_Team_Regions',
           scatter_kws= {"marker": "D", 
                        "s": 30},
           palette = 'plasma',
           )

plt.lengend(loc = 'upper right')
plt.title("divided by income level")
plt.grid()
plt.tight_layout()
plt.savefig('why we choose southasia.png')
plt.show()

###############################
#2 region comparison
###############################

sns.lmplot(x = 'access_to_electricity_pop',
           y = 'pct_services_employment',
           data = teamfilled,
           fit_reg = False,
           hue= 'income_group',
           
           
           palette = 'plasma', 
           
           
           
           )

plt.lengend(loc = 'upper right')
plt.title("divided by region")
plt.grid()
plt.tight_layout()
plt.savefig('2region_unemployment_co2_south.png')
plt.show()

sns.lmplot(x = 'urban_population_pct',
           y = 'CO2_emissions_per_capita)',
           data = teamfilled,
           fit_reg = False,
           hue= 'income_group',
           
           
           palette = 'plasma', 
           
           
           
           )

plt.lengend(loc = 'upper right')
plt.title("divided by region")
plt.grid()
plt.tight_layout()
plt.savefig('2region_unemployment_co2_south.png')
plt.show()
#####electricity rural compared to service or agriculture employment
sns.lmplot(x = 'CO2_emissions_per_capita)',
           y = 'pct_industry_employment',
           data = teamfilled_southasia_eu,
           fit_reg = True,
           hue= 'Hult_Team_Regions',
           col= 'Hult_Team_Regions',
           palette = 'plasma', 
           
           
           
           )

plt.lengend(loc = 'upper right')
plt.title("divided by region")
plt.grid()
plt.tight_layout()
plt.savefig('3region_ruralelec_service.png')
plt.show()
#####
sns.lmplot(x = 'access_to_electricity_rural',
           y = 'pct_agriculture_employment',
           data = teamfilled_southasia_eu,
           fit_reg = True,
           hue= 'Hult_Team_Regions',
           col= 'Hult_Team_Regions',
           palette = 'plasma', 
           
           
           
           )

plt.lengend(loc = 'upper right')
plt.title("divided by region")
plt.grid()
plt.tight_layout()
plt.savefig('3region_ruralelec_agriculture.png')
plt.show()


#####

sns.lmplot(x = 'fdi_pct_gdp',
           y = 'exports_pct_gdp',
           data = teamfilled_southasia_eu,
           fit_reg = True,
           hue= 'income_group',
           col = 'income_group',
           col_wrap = 2,        
           palette = 'plasma', 
           
           
           
           )

plt.lengend(loc = 'upper right')
plt.title("divided by region")
plt.grid()
plt.tight_layout()
plt.savefig('2region_fdi_exports_south.png')
plt.show()


###############################
#3 region comparison
###############################
####Bar plot comparison

# library
import matplotlib.pyplot as plt
south_industry_median = south_asia['pct_industry_employment'].median() 
team_industry_median = teamfilled['pct_industry_employment'].median() 
world_list = list(world.values.flatten())
world_industry = world_list[13]


south_air_median = south_asia['avg_air_pollution'].median() 
team_air_median = teamfilled['avg_air_pollution'].median() 
world_air = world_list[25]


# Create bars
barWidth = 0.9
bars1 = [team_industry_median,south_industry_median,world_industry]
bars2 = [10,9,8]

 
# The X position of bars
r1 = [1,2,3]
r2 = [4,5,6]
r3 = r1 + r2 

 
# Create barplot
plt.bar(r1, bars1, width = barWidth, color = (0.3,0.1,0.4,0.6), label='pct_industry_employment')
plt.bar(r2, bars2, width = barWidth, color = (0.3,0.5,0.4,0.6), label='air_pollution')
# Note: the barplot could be created easily. See the barplot section for other examples.
 
# Create legend
plt.legend(loc = 'upper right')
 
# Text below each barplot with a rotation at 90°
plt.xticks([r + barWidth for r in range(len(r3))], ['North Asia','South Asia', 'World', 'North Asia', 'South Asia', 'World'], rotation=90)
 
 
# Adjust the margins
plt.subplots_adjust(bottom= 0.2, top = 0.98)
 
# Show graphic
plt.savefig('3region_air_industry.png')
plt.show()


###############################
#4 region comparison
###############################
####Bar plot comparison

# 4 REGION ENVIRONMENT COMPARISON

europe_industry_median = europe_northamerica['pct_industry_employment'].median()
south_industry_median = south_asia['pct_industry_employment'].median() 
team_industry_median = teamfilled['pct_industry_employment'].median() 
world_list = list(world.values.flatten())
world_industry = world_list[13]

europe_air_median = europe_northamerica['avg_air_pollution'].median()
south_air_median = south_asia['avg_air_pollution'].median() 
team_air_median = teamfilled['avg_air_pollution'].median() 
world_air = world_list[25]

europe_co2_median = europe_northamerica['CO2_emissions_per_capita)'].median()
south_co2_median = south_asia['CO2_emissions_per_capita)'].median() 
team_co2_median = teamfilled['CO2_emissions_per_capita)'].median() 
world_co2 = world_list[25]

europe_urbanpop_median = europe_northamerica['urban_population_pct'].median()
south_urbanpop_median = south_asia['urban_population_pct'].median() 
team_urbanpop_median = teamfilled['urban_population_pct'].median() 
world_urbanpop = world_list[10]


# Create bars
barWidth = 0.9

bars1 = [team_industry_median,south_industry_median,europe_industry_median,world_industry]
bars2 = [team_air_median,south_air_median,europe_air_median,world_air ]
bars3 = [team_urbanpop_median,south_urbanpop_median,europe_urbanpop_median,world_urbanpop] 
bars4 = [team_co2_median,south_co2_median,europe_co2_median,world_co2]
bars5 = bars1+bars2+bars3+bars4
# The X position of bars
r1 = [1,2,3,4]
r2 = [5,6,7,8]
r3 = [9,10,11,12]
r4 = [13,14,15,16]
r5 = r1 + r2 + r3 +r4 


 
# Create barplot
plt.bar(r1, bars1, width = barWidth, color = (0.3,0.1,0.4,0.6), label='industry_employment')
plt.bar(r2, bars2, width = barWidth, color = (0.1,0.5,0.5,0.6), label='avg_air_pollution')
plt.bar(r3, bars3, width = barWidth, color = (0.3,0.2,0.8,0.6), label='urban_population_pct')
plt.bar(r4, bars4, width = barWidth, color = (0.2,0.6,0.2,0.6), label='CO2_emissions')

# Note: the barplot could be created easily. See the barplot section for other examples.
 
# Create legend
plt.legend(loc = 'upper left')
 
# Text below each barplot with a rotation at 90°

plt.xticks([r + barWidth for r in range(len(r5))], ['North Asia','South Asia', 'Europe', 'World', 'North Asia','South Asia', 'Europe', 'World','North Asia','South Asia', 'Europe', 'World','North Asia','South Asia', 'Europe', 'World'], rotation=90)

# Create labels
label = ['4','2','3','1','2','3','4','1','2','4','1','3','3','4','2','1' ]
 
# Text on the top of each barplot
for i in range(len(r5)):
    plt.text(x = r5[i]-0.3 , y = bars5[i]+0.3, s = label[i], size = 10)

 
 
# Adjust the margins
plt.subplots_adjust(bottom= 0.05, top = 1)
 
# Show graphic
plt.savefig('4region_pullution.png')
plt.show()

####################
# 4 REGION ECONOMY COMPARISON

europe_agriculture_median = europe_northamerica['pct_agriculture_employment'].median()
south_agriculture_median = south_asia['pct_agriculture_employment'].median() 
team_agriculture_median = teamfilled['pct_agriculture_employment'].median() 
world_list = list(world.values.flatten())
world_agriculture = world_list[12]

europe_services_median = europe_northamerica['pct_services_employment'].median()
south_services_median = south_asia['pct_services_employment'].median() 
team_services_median = teamfilled['pct_services_employment'].median() 
world_services = world_list[14]

europe_exports_median = europe_northamerica['exports_pct_gdp'].median()
south_exports_median = south_asia['exports_pct_gdp'].median() 
team_exports_median = teamfilled['exports_pct_gdp'].median() 
world_exports = world_list[5]

europe_fdi_median = europe_northamerica['fdi_pct_gdp'].median()
south_fdi_median = south_asia['fdi_pct_gdp'].median() 
team_fdi_median = teamfilled['fdi_pct_gdp'].median() 
world_fdi = world_list[6]


# Create bars
barWidth = 0.9

bars1 = [team_agriculture_median,south_agriculture_median,europe_agriculture_median,world_agriculture]
bars2 = [team_services_median,south_services_median,europe_services_median,world_services ]
bars3 = [team_exports_median,south_exports_median,europe_exports_median,world_exports] 
bars4 = [team_fdi_median,south_fdi_median,europe_fdi_median,world_fdi]
bars5 = bars1+bars2+bars3+bars4
# The X position of bars
r1 = [1,2,3,4]
r2 = [5,6,7,8]
r3 = [9,10,11,12]
r4 = [13,14,15,16]
r5 = r1 + r2 + r3 +r4 

########################
barWidth = 0.5

bars1 = [17]
bars2 = [20.17 ]
bars3 = [20.01] 
bars4 = [22.9]

# The X position of bars
r1 = [1]
r2 = [2]
r3 = [3]
r4 = [4]
r5 = r1 + r2 + r3 +r4 

 
# Create barplot
plt.bar(r1, bars1, width = barWidth, color = (0.6,0.2,0.3,0.6), label='North Asia')
plt.bar(r2, bars2, width = barWidth, color = (0.4,0.3,0.8,0.6), label='South Asia')
plt.bar(r3, bars3, width = barWidth, color = (0.2,0.7,0.5,0.6), label='Europe')
plt.bar(r4, bars4, width = barWidth, color = (0.4,0.4,0.4,0.6), label='World')

# Note: the barplot could be created easily. See the barplot section for other examples.
 
# Create legend
plt.legend(loc = 'upper left')
 
# Text below each barplot with a rotation at 90°

plt.xlabel('pct_industry_employment')

 
# Adjust the margins
plt.subplots_adjust(bottom= 0.05, top = 1.2)
 
# Show graphic
plt.savefig('4region_industry.png')
plt.show()

#############

barWidth = 0.9

bars1 = [85.05,76.5]
bars2 = [92.19,90.63 ]
bars3 = [100,100] 
bars4 = [85.7,43.7]

# The X position of bars
r1 = [1,2]
r2 = [3,4]
r3 = [5,6]
r4 = [7,8]
r5 = r1 + r2 + r3 +r4 

 
# Create barplot
plt.bar(r1, bars1, width = barWidth, color = (0.6,0.2,0.3,0.6), label='North Asia')
plt.bar(r2, bars2, width = barWidth, color = (0.4,0.3,0.8,0.6), label='South Asia')
plt.bar(r3, bars3, width = barWidth, color = (0.2,0.7,0.5,0.6), label='Europe')
plt.bar(r4, bars4, width = barWidth, color = (0.4,0.4,0.4,0.6), label='World')

# Note: the barplot could be created easily. See the barplot section for other examples.
 
# Create legend
plt.legend(loc = 'upper right')
 
# Text below each barplot with a rotation at 90°

plt.xticks([r + barWidth for r in range(len(r5))], ['Electricity_Pop', 'Electricity_Rural', 'Electricity_Pop', 'Electricity_Rural', 'Electricity_Pop', 'Electricity_Rural', 'Electricity_Pop', 'Electricity_Rural'], rotation=90)


 
# Adjust the margins
plt.subplots_adjust(bottom= 0.05, top = 1)
 
# Show graphic
plt.savefig('4region_elec.png')
plt.show()

#############
sns.jointplot(x = 'pct_industry_employment',
                     y = 'gdp_usd',
                     kind = 'reg',
                     joint_kws={'color':'blue'},
                     data = teamfilled)


plt.tight_layout()
plt.show()

##
pearson = sns.jointplot(x = 'pct_service_employment',
                     y = 'gdp_usd',
                     kind = 'reg',
                     joint_kws={'color':'blue'},
                     data = teamfilled)


plt.tight_layout()
plt.show()


############
sns.violinplot(x = 'income_group',
               y = 'gdp_usd',
               data = teamfilled_world_southasia_eu,
               orient = 'v',
               )
plt.xticks(rotation=70)
plt.show()

############

sns.violinplot(x = 'internet_usage_pct',
                     y = 'pct_services_employment',
               data = teamfilled,
               orient = 'v',
               inner = None,
               color = 'white')



# We can use stripplots to visualize the datapoints
sns.stripplot(x = 'internet_usage_pct',
                     y = 'pct_services_employment',
              data = teamfilled,
              jitter = True,
              size = 5,
              orient = 'v')

plt.xticks(rotation=70)
plt.show()
######

sns.jointplot(x = 'internet_usage_pct',
                     y = 'pct_services_employment',
                     kind = 'reg',
                     joint_kws={'color':'blue'},
                     data = teamfilled,
                     x_estimator = pd.np.mean,
                     x_bins = 8)


plt.tight_layout()
plt.show()

sns.jointplot(x = 'urban_population_pct',
                     y = 'pct_agriculture_employment',
                     kind = 'reg',
                     joint_kws={'color':'navy'},
                     data = teamfilled,
                     )


plt.tight_layout()
plt.show()

####
sns.regplot(x = 'income_level',
                     y = 'child_mortality_per_1k',
                     data = teamfilled)


plt.tight_layout()
plt.show()

sns.regplot(x = 'income_level',
                     y = 'urban_population_pct',
                     data = teamfilled)


plt.tight_layout()
plt.show()
