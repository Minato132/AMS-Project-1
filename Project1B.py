import pandas as pd

with open('Part B Data/927567_PartB.csv') as file:
    data = pd.read_csv(file)

print(data)

