#Cumulative donations plot for each candidate
%matplotlib inline 
import matplotlib.pyplot as plt 
psanders.rename(columns={'Amount':'Sanders'}, inplace=True) 
pclinton.rename(columns={'Amount':'Clinton'}, inplace=True) 
ptrump.rename(columns={'Amount':'Trump'}, inplace=True)
pcruz.rename(columns={'Amount':'Cruz'}, inplace=True) 
funds = pd.concat([psanders,pclinton,ptrump,pcruz], axis=1) 
funds.sum().plot(kind='bar', title="Total 2016 Donations for each candidat e through April")
funds.cumsum(0).plot(subplots=True, figsize=(10,6), title='Cumulative Don ations to Date')