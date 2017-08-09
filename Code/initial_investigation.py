#Initial investigations of financial trends US Campaign Contributions

import pandas as pd 
import json 

#Candidate Trump
indivtrump = pd.read_csv("/home/ubuntu/data/indivtrump.csv", dtype=unicode , encoding="utf-8", usecols=["Receipt Date", "Amount"]) 
indivtrump["Receipt Date"] = pd.to_datetime(indivtrump["Receipt Date"]) 
indivtrump = indivtrump[indivtrump['Receipt Date'].dt.year == 2016] 
indivtrump['Amount'] = indivtrump['Amount'].str.replace(r'[$,]','') 
indivtrump['Amount'] =indivtrump['Amount'].convert_objects(convert_numeric =True) 
ptrump = indivtrump.groupby('Receipt Date').sum() 
ptrump.head(3)

#Candidate Sanders
indivsanders = pd.read_csv("/home/ubuntu/data/indivsanders.csv", dtype=uni code, encoding="utf-8", usecols=["Receipt Date", "Amount"]) 
indivsanders["Receipt Date"] = pd.to_datetime(indivsanders["Receipt Date"] ) 
indivsanders = indivsanders[indivsanders['Receipt Date'].dt.year == 2016] 
indivsanders['Amount'] = indivsanders['Amount'].str.replace(r'[$,]','')
indivsanders['Amount'] =indivsanders['Amount'].convert_objects(convert_num eric=True) 
psanders = indivsanders.groupby('Receipt Date').sum() 

#Candidate Clinton
indivclinton = pd.read_csv("/home/ubuntu/data/indivclinton.csv", dtype=uni code, encoding="utf-8", usecols=["Receipt Date", "Amount"]) 
indivclinton["Receipt Date"] = pd.to_datetime(indivclinton["Receipt Date"] ) 
indivclinton = indivclinton[indivclinton['Receipt Date'].dt.year == 2016] 
indivclinton['Amount'] = indivclinton['Amount'].str.replace(r'[$,]','') 
indivclinton['Amount'] =indivclinton['Amount'].convert_objects(convert_num eric=True) 
pclinton = indivclinton.groupby('Receipt Date').sum() 

#Candidate Cruz
indivcruz = pd.read_csv("/home/ubuntu/data/indivcruz.csv", dtype=unicode, encoding="utf-8", usecols=["Receipt Date", "Amount"]) 
indivcruz["Receipt Date"] = pd.to_datetime(indivcruz["Receipt Date"]) 
indivcruz = indivcruz[indivcruz['Receipt Date'].dt.year == 2016] 
indivcruz['Amount'] = indivcruz['Amount'].str.replace(r'[$,]','') 
indivcruz['Amount'] =indivcruz['Amount'].convert_objects(convert_numeric=T rue) 
pcruz = indivcruz.groupby('Receipt Date').sum() 