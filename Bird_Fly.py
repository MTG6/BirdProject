import pandas as pd
from develop.eda_functions import top5_bird
from develop.data_input import *

if __name__ == "__main__":
	df = read_data('Oregon')
	print(len(df))
	
	top5 = top5_bird(df, year = 2010)
	print(top5)