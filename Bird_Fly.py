import pandas as pd
from develop.eda_functions import *
from develop.data_input import *

if __name__ == "__main__":
	df = read_data('Oregon')
	print(len(df))
	
	#top5 = top5_bird(df, year = 2010)
	top5 = top_routes(df)
	print(top5)