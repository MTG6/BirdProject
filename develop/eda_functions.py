import pandas as pd

def top5_bird(df,state = None,year = None):
	""" Find the top 5 birds that visited a particular state, in a particular year."""
	year = int(year)
	if year != None:
		df_f = df[['RouteName','names','SpeciesTotal']][df.Year == year].groupby(by='names').sum().nlargest(5,'SpeciesTotal')
	else:
		df_f = df[['RouteName','names','SpeciesTotal']].groupby(by='names').sum().nlargest(5,'SpeciesTotal')
		
	return df_f