# Throughout this code, we will use an example dataset which could be loaded into python for checks and 
# tests could be carried out if necessary
import pandas as pd
import numpy as np

'''
Reading Data:
You can use the read functions to read from a variety of files
csv: use read_csv
sas: use read_sas
Special note: In case you want to read sas7bdat files, it is recommended to use the pyreadstat library:
https://github.com/Roche/pyreadstat

parquet: use pyarrow.parquet
'''

#reading df from a csv
df = pd.read_csv('C://Work/Python/279df7e5-e540-4e2f-9b4b-dc655e8007e1_Data.csv')
#read sas:
df_sas = pd.read_sas('path/to/sas/my_sas.sas7bdat')
# with the new library for SAS7bdat:
import pyreadstat
df_sas,meta = pyreadstat.read_sas7bdat('path/to/sas/my_sas.sas7bdat')

# parquet:
import pyarrow.parquet as pq
df_parquet = pq.read_table('path/to/pq/my_parquet')
df = df_parquet.to_pandas()
# optional - delete pq in RAM to save space:
del df_parquet
# Update: In newer version of pandas, there is a function which will automatically read parquet files
# df.read_parquet() - works similar to read_csv



'''
Exploratory Data Analysis: 
Exploring data could be a very simple examination of data, quick stats on the 
data columns to complex univariate and bivariate tests. 
'''

'''
Data cleaning: 
During the course of EDA, it is often seen that we might also need to clean the data a bit
based on the understanding. So, EDA and cleaning/ wrangling usually go together
Here we try to summarise as many EDA/data clean functions as possible: 
'''

# Try with the example dataset: 
df = pd.read_csv('data/train-data_car.csv')

#checking its contents
df.info()
df.head()
df.tail()

#describe will give quick information
df.describe()

# Create a new empty column with empty values / 'None' values
df = df.assign(newCol1 =None, newCol2='', newCol3=np.NaN)
# this is equivalent to 
# df.loc[:,newCol1] = None
# df.loc[:,newCol2] = ''
# df.loc[:,newCol3] = NaN
#However, this second way throws warnings on modern versions of pandas
# In the latest version, this even throws an error. So avoid! 
# WARNING: Use the inplace option very CAREFULLY - it will still create a copy - but reassign the copy to original! 
df.drop(columns=['newCol1','newCol2','newCol3'],inplace=True)
# A better way to do it would be like this:
cols_to_drop = ['newCol1','newCol2','newCol3']
df2 = df.drop(columns=[cols_to_drop],inplace=True)
# If you dont know the column names, but want to filter columns which match a regular expression:
cols_to_drop = df.filter(like='newC').columns.to_list()


# If there are duplicate rows, you could drop them.
# drop_duplicates works for the entire data frame, or by columns
df.drop_duplicates(subset = ['Unnamed:0'],inplace = True)

# If you want to drop duplicates by mulitple columns, then you can extend the subset argument.
# Suppose, you want to keep only the last row of every Name Location combination, then:
df.drop_duplicates(subset = ['Name','Location'], keep='last', inplace = True)


# Concatenate columns to create a new column:
df['ConcatCol'] =  df['Location'] + '_' + df['Name'].str.title()
# Here, Name contains a string that is not in proper case : Ex: 35 RUE De LAEKEN.
# str.title() will get the case to title case
# In case you want to concatenate a numeric column to a string, for example PolicyNumber(string) with a RiskNumber(integer), then use
# df['Policyrisk'] = df['PolicyNumber'] + '_' + df['RiskNumber'].map(str)


#Initialise an empty dataframe with column names
emptyDf = pd.DataFrame(columns = ['col1','col2'])
# If you already have a df from which it should copy, then it is even better:
emptyDf = pd.DataFrame(columns = otherdf.columns)

# Append a second df to the first one:
unionDf.append(secondDf,ignore_index=True) 
# the above just displays the appended DF. If you want the unionDf to hold the appended information, use: 
unionDf = unionDf.append(secondDf,ignore_index=True) 

# Once a df is read into memory, if you want to change the data types of the columns, 
# for individual column names, you use : 
df["strcol"]= df["strcol"].to_numeric()
# for strings, the better way to do this would be to use astype
df["intcol"]= df["intcol"].astype(str)

# However, if you have a huge list and prefer to do it via dictionary, first create one:
dtype_dict = {'col1': 'float32', 
 'col2': 'category',
 'col3': 'object'}
df = df.astype(dtype_dict)

 ### Lookup from another table is done using:
# 1. Map if the lookup is just based on one single column
# 2. JOIN / merge if the lookup is based on multiple columns

# map
map_dict = pd.Series(df2.needed_column.values,index=df2.lookup_values_col).to_dict()
df['needed_column'] = df['lookup_values_col'].map(map_dict)

# SQL join equivalent is pd.merge
# If we want a column from second df on the first:
df_first = df_first.merge(df_second[['lookup_key','needed_column']], on = ['lookup_key'],how='left')



# Rename columns in dataframe (if you already know the names)

# Rename columns by order / position:
df.rename(columns={df[0]: "new_col1"}, inplace = True)
# Rename columns by variable name:
df.rename(columns={catvar: "new_col1"}, inplace = True)

# Quick value counts / count and Group by a column:
df.column.value_counts()
# include NAs
df.column.value_counts(dropna=False)

# Unique values in a column: equivalent of select distinct column
df.column.unique()
# Count of unique values in a column: equivalent of select count (distinct column)
df.column.nunique()
# If you want the count of more than one column, there are multiple ways to do it. If it is just two string columns, do this: 
# even if one is string and one is integer, you can do this: 
df['concat_col'] = df['str_col_1'] + '_' + df['num_col_1'].map(str)
df['concat_col'].unique()
df['concat_col'].nunique()

# The second way (for only string columns), would be:
df.groupby(['str_col_1','str_col_2']).ngroups
# This will exclude NaNs. 

# If you want to see for multiple columns, mix of str/numeric -- RECOMMENDED
mix_cols = ['str_col_1','str_col_2','num_col_1','num_col_2']
df[mix_cols].drop_duplicates().shape

# Sort a data frame by columns
df = df.sort_values(by=['col1','col2'], ascending = [True,False], ignore_index=True)
# will sorty by col1  ascending and then on col2 descending
# if ignore_index=True, then the resulting df will have a new_index

# https://stackoverflow.com/questions/47152691/how-to-pivot-a-dataframe


# Quick univariate plots: 
# Histogram
df['continuous_column'].plot.hist()
# barplot - for value counts of cat vars
df['catvar'].plot.bar()