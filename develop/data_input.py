def read_data(sname):
	"""Read in relevant data."""
	
	sname = sname.upper()
	sname = 'OREGON'
	
	#Get state csv, split route into state blocks
	region = pd.read_csv("../data/Oregon.csv")
	routes = pd.read_csv("../data/routes_clean.csv",encoding = "ISO-8859-1")
	routes_or = routes[routes.statenum == 69]
		
	#Make mappings
	#bird_map = pd.DataFrame({"Aou":AOU,"names":bird_names})
	#state_map = pd.DataFrame({"statenum":state_code , "StateName":state_names})
	bird_map = bird_mapping()
	state_map = state_mapping()
	
	#Final merges
	routes_f = pd.merge(routes,state_map,how="left",on='statenum')
	df_m1 = pd.merge(region,routes_f[['Route','RouteName','Latitude','Longitude']][routes_f.StateName == sname], how="left",on='Route')
	df_final = pd.merge(df_m1,bird_map,how="left",on="Aou")
	
	return df_final


def bird_mapping():
	"""Read bird name txt and extract aou -> name map."""
	i=9
	end =757
	AOU = []
	bird_names = []

	with open("../data/SpeciesList.txt","r",encoding = "ISO-8859-1") as pipe:
		data = pipe.readlines()
		while i < end:
			AOU.append(int(data[i][6:12]))
			bird_names.append(data[i][12:50].strip())
			i=i+1
	pipe.close()
	
	bird_map = pd.DataFrame({"Aou":AOU,"names":bird_names})
	
	return bird_map

def state_mapping():
	"""Read statenum and name from txt for mapping."""
	i=11
	end =108
	state_code = []
	state_names = []
	
	with open("./data/RegionCodes.txt","r",encoding = "ISO-8859-1") as pipe:
		data = pipe.readlines()
		while i < end:
			state_code.append(int(data[i][4:20]))
			state_names.append(data[i][20:64].strip())
			i=i+1
	pipe.close()
	
	state_map = pd.DataFrame({"statenum":state_code , "StateName":state_names})
	
	return state_map