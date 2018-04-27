import pandas as pd

def viz_data(df,funnames = None, ystart = 1999, yend = 2009):
	"""Export CSV for data viz.
	
	Inputs:
	DataFrame df: MUST BE FINAL MERGED DF! (output of read_data())
	
	"""
	# Export long data for d3 viz
	
	if(funnames == None):
		funnames = ['Cliff Swallow','European Starling','Red-winged Blackbird','Western Meadowlark','(Oregon Junco) Dark-eyed Junco']
	
	y = ystart
	res = df[['RouteName','names','SpeciesTotal','Year']][(df.Year == (ystart-1)) & (df.names.isin(funnames))].groupby(['names','Year']).sum().nlargest(5,'SpeciesTotal')

	while y <= yend:
		res = res.append(df[['RouteName','names','SpeciesTotal','Year']][(df.Year == y) & (df.names.isin(funnames))].groupby(['names','Year']).sum().nlargest(5,'SpeciesTotal'))
		y = y+1

	t1 = res.reset_index()#.pivot(columns = 'names', values = 'SpeciesTotal')
	res1 = t1.set_index('Year').pivot(columns = 'names', values = 'SpeciesTotal').fillna(0)
	res1.to_csv("./app/static/Birds.csv")