
import pandas as pd 
import numpy as np

# finds the binary features of a dataframe and creates a list of their names

def findBinary(df):
	lst = []
	for column in df:
		if (df[column].value_counts()).size==2:
			lst.append(column)
	return lst

def makeBoolian(df,lst):
	values = []
	for column in df[lst]:	
		series = df[column].value_counts()
		values.append(series)
	for i in range(len(values)):
		header = values[i].name
		option1 = values[i].index[1]
		option0 = values[i].index[0]
		df[header].replace([option1,option0], [1,0], inplace = True)
	return df

def addNaNData(df):
	noNaN = []
	# get dataframe boolian of nan values
	whereNaN = df.isnull()# df
	# get feature and example wise nan totals
	featureTotalNaN = pd.DataFrame(whereNaN.sum(axis=0).rename("FT_NUMBER_NAN")) # df transpose
	exampleTotalNaN = whereNaN.sum(axis=1).rename("EX_NUMBER_NAN") # series
	# add ex sums to dataframe (row first or error)
	df = pd.concat([df,exampleTotalNaN], axis=1) # add as column
	for column in featureTotalNaN:
	    if featureTotalNaN.iloc[0][column]==0:
	        noNaN.append(column)
	return (noNaN, df)

def findNoNaN(df):
	lst = []
	for column in df:
		if (df[column].value_counts()).size==2:
			lst.append(column)
	return binaryFeatures

def findCategorical(df):
	lst=[]
	for column in df:
		if (df[column].value_counts()).size<30:
			if (df[column].value_counts()).size>2:
				lst.append(column)
	return lst, df

def findNan(df):
	whereNan = df.isnull()#df
	countNan = df_whereNan.sum(axis=0) #seies
	pd.concat([df,numberNan])
	return (df_whereNaN, df_numberNaN)
 
