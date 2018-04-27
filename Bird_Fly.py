import pandas as pd
from develop.eda_functions import *
from develop.data_input import *
from develop.data_output import *

if __name__ == "__main__":
	df = read_data('Oregon')
	#print(len(df))
	
	#top5 = top5_bird(df, year = 2010)
	#top5 = top_routes(df)
	
	bnames = ['Nashville Warbler','Song Sparrow','Red-tailed Hawk','Wood Duck','Cordilleran Flycatcher']
	viz_data(df,funnames = bnames,ystart=2000,yend=2010)
	
	print("Finished")