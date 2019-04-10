import numpy as np
import pandas as pd
from datetime import datetime, timedelta

fp = 'data.csv'
wp = 'cnstdata.csv'

Tint = timedelta(minutes = 9)

data = pd.read_csv(fp, header = None)
remove = set()

rows = len(data.index)
for index,row in data.iterrows():
	Ttst = datetime.fromisoformat(row[0])
	for chck in range(index+1,rows):
		Trow = datetime.fromisoformat(data.iat[chck,0])
		if Trow - Ttst < Tint:
			remove.add(chck)
		else: ##assumes data is in assending order but give massive speedup
			break
			
data = data.drop(remove, axis = 0)
data.to_csv(wp, header = None, index = False)