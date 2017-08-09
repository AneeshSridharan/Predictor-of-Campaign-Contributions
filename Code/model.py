import numpy as np 
import statsmodels.api as sm 
import statsmodels.tsa.api as smt 
import statsmodels.formula.api as smf

#Cruz 
datacruz = pd.concat([pcruz, sentcruz], axis=1).fillna(0) 
datacruz.drop(["N"], axis=1, inplace=True) 
datacruz["per_pos"] = datacruz['P'].div(datacruz['Total']).fillna(0) 
dcruz = datacruz.diff() 
dcruz = dcruz.drop(dcruz.tail(25).index) 

# Trump 
datatrump = pd.concat([ptrump, senttrump], axis=1).fillna(0) 
datatrump.drop(["N"], axis=1, inplace=True) 
datatrump["per_pos"] = datatrump['P'].div(datatrump['Total']).fillna(0) 
dtrump = datatrump.diff() 
dtrump = dtrump.drop(dtrump.tail(25).index) 

# Clinton 
dataclinton = pd.concat([pclinton, sentclinton], axis=1).fillna(0) 
dataclinton.drop(["N"], axis=1, inplace=True) 
dataclinton["per_pos"] = dataclinton['P'].div(dataclinton['Total']).fillna (0) 
dclinton = dataclinton.diff() 
dclinton = dclinton.drop(dclinton.tail(25).index) 

#Sanders 
datasanders = pd.concat([psanders, sentsanders], axis=1).fillna(0) 
datasanders.drop(["N"], axis=1, inplace=True) 
datasanders["per_pos"] = datasanders['P'].div(datasanders['Total']).fillna (0) 
dsanders = datasanders.diff() 
dsanders = dsanders.drop(dsanders.tail(25).index)

#Model for each candidate individually

#Cruz
mcruz = smt.VAR(dcruz[1:]) 
mcruz.select_order(7)
resultscruz = mcruz.fit(maxlags = 7, ic = 'hqic') 
resultscruz.summary()
resultscruz.plot()
resultscruz.test_causality('Cruz', ['Total', 'per_pos'], kind='f') 
resultscruz.test_causality('Total', ['Cruz'], kind='f')

#Clinton
mclinton = smt.VAR(dclinton[1:]) 
mclinton.select_order(7)
resultsclinton = mclinton.fit(maxlags = 7, ic = 'fpe') 
resultsclinton.summary()
resultsclinton.plot()
resultsclinton.test_causality('Clinton', ['Total', 'per_pos'], kind='f') 
resultsclinton.test_causality('Total', ['Clinton'], kind='f') 

#Sanders
msanders = smt.VAR(dsanders[1:]) 
msanders.select_order(7)
resultssanders = msanders.fit(maxlags = 7, ic = 'fpe') 
resultssanders.summary()
resultssanders.plot()
resultssanders.test_causality('Sanders', ['Total', 'per_pos'], kind='f') 
resultssanders.test_causality('Total', ['Sanders'], kind='f')