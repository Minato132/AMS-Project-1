import numpy as np
import pandas as pd
import csv

with open('Part B Data/927567_PartB.csv') as file:
    data = pd.read_csv(file)

data.sort_values(by = 'x', ascending= True, inplace = True, ignore_index = True)
max = max(data['x']) // 1
min = min(data['x']) // 1

bins = np.arange(min, max + 1, .1)

data_bin = np.digitize(data['x'], bins)

data_bin = pd.Series(data_bin, name = 'bins')

data = data.merge(data_bin, left_index = True, right_index = True)
data = data.loc[:, ['x', 'y', 'bins']]

x = []
for i in range(1, len(bins)+1):
    test = data.loc[data['bins'] == i]
    avg =  test['x'].mean()
    for i in range(len(test)):
        test.iat[i, 0] = avg
    
    x.append(test.loc[:, ['x','y']].to_numpy())

datastart = pd.DataFrame(x[0])
for i in range(1,len(x)):
    data1 = pd.DataFrame(x[i])
    datastart = datastart.merge(data1, how = 'outer')

datastart.rename(columns = {0:'x', 1:'y'}, inplace = True)

print(datastart)
datastart.to_csv('binned_data')

    

    
    


