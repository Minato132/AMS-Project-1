import pandas as pd
from sklearn.impute import KNNImputer 
import statsmodels.api as sm
from statsmodels.formula.api import ols

with open('Part A Data/927567_IV.csv') as file:
    IV_data = pd.read_csv(file)


with open('Part A Data/927567_DV.csv') as file1:
    DV_data = pd.read_csv(file1)


IV_data.sort_values(by = 'ID', ascending = True, inplace = True)
DV_data.sort_values(by = 'ID', ascending = True, inplace = True)

#Merged the 2 data sets together
data = IV_data.merge(DV_data, on = 'ID', how = 'outer')

#Using KNNImputer method
imputer = KNNImputer(n_neighbors=2, weights = 'uniform')
data = imputer.fit_transform(data)
data = pd.DataFrame(data)
data.rename(columns={0 : 'ID', 1: "IV", 2:'DV'}, inplace = True)

#Using statsmodels, we are going to generate our OLS
IV = data['IV'].tolist()
DV = data['DV'].tolist()

#Adding the constant term
IV = sm.add_constant(IV)

#Fitting a linear regression model
result = sm.OLS(DV, IV).fit()

print(result.summary())


#Use statmodels to generate our Anova
model = ols('DV~IV', data = data).fit()
table = sm.stats.anova_lm(model, type = 2)
print(table)

