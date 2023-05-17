import pandas as pd

data = pd.read_csv ('transaction.csv')
data = pd.read_csv ('transaction.csv', sep = ';')

# Summary of the dataset
data.info()

#Working with calculations

#defining variables

costPerItem = 11.73
sellingPricePerItem = 21.11
numberOfItemsPurchased = 6

#Mathematical operations on Tableau

profitPerItem = 21.11 - 11.73
profitPerItem = sellingPricePerItem - costPerItem

profitPerTransaction = numberOfItemsPurchased * profitPerItem
costPerTransaction = numberOfItemsPurchased * costPerItem
sellingPricePerTransaction = numberOfItemsPurchased * sellingPricePerItem

#CostPerTransaction Colmun Calculation

#costPerTransaction = numberOfItemsPurchased * costPerItem
# variable = dataframe ['column_name]

costPerItem = data['CostPerItem']
numberOfItemsPurchased = data['NumberOfItemsPurchased']

costPerTransaction = costPerItem * numberOfItemsPurchased

#adding a new column to data

data['costPerTransaction'] = costPerTransaction

#sales per Transaction

data['salesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit per Transaction Sales - Cost

data['profitPerTransaction'] = data['salesPerTransaction'] - data['costPerTransaction']

#Markup = (Sales - cost) / cost

data ['Markup'] = (data['profitPerTransaction']) / data['costPerTransaction']

#Rounding Markup
roundMarkup= round(data ['Markup'],2)
data ['Markup'] = roundMarkup

#combining data fields

#my_date = data['Day'] + '-'

#checking columns data type
print(data['Day'].dtype)

#change columns type
day = data['Day'].astype(str)
print(day.dtype)

year = data['Year'].astype(str)
print(year.dtype)

my_date = day + '-' + data['Month'] + '-' + year

data ['date'] = my_date

#using iloc to view speicfic colums/rows

data.iloc[0] #views the row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) # first 5 rows

data.iloc[:,2] # all rows on the second column

data.iloc[4,2] # 4th row, 2nd column

#using split to split the client keywords field
#new_variable = column.str.split('sep', expand=True)

split_col = data['ClientKeywords'].str.split(',', expand=True)

#creating new columns to display clientkeywords in different column

data['clientAge'] = split_col[0]
data['clientType'] = split_col[1]
data['lengthOfContract'] = split_col[2]

#replacing the square brackets using replace function

data['clientAge'] = data['clientAge'].str.replace('[', '')
data['lengthOfContract'] = data['lengthOfContract'].str.replace(']','')

#using lowercase function

data['ItemDescription'] = data['ItemDescription'].str.lower()

#adding new data set

seasons = pd.read_csv ('value_inc_seasons.csv' , sep = ';')

#merging data sets
# merge_df = pd.merge(df_old, df_new, on='key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns to clear up data 

#df = df.drop('columnname' , axis=1)

data = data.drop('ClientKeywords' , axis = 1)
data = data.drop('Day' , axis = 1)
data = data.drop(['Month' , 'Year'] , axis = 1)

#exporting into csv for tableau

data.to_csv('ValueInc_Cleaned.csv', index = False)
