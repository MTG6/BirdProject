import pandas pd

def top5_bird(df,state,year = None):
	""" Find the top 5 birds that visited a particular state, in a particular year."""
	if year not None:
		df_f = df[['RouteName','names','SpeciesTotal']][df.year == Year].groupby(by='names').sum().nlargest(5,'SpeciesTotal')
	else:
		df_f = df[['RouteName','names','SpeciesTotal']].groupby(by='names').sum().nlargest(5,'SpeciesTotal')
		
	return df_f