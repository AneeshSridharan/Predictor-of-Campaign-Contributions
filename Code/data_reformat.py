#Post sentiment classification - Data reformat
import matplotlib.pyplot as plt 
sentiment = pd.read_csv("/home/ubuntu/data/NYTSentiment.csv", dtype=unicod e, encoding = "ISO-8859-1") 
sentiment["Date"] = pd.to_datetime(sentiment["Date"]) 
sentcruz = sentiment[sentiment['Candidate']=='Cruz'].pivot_table(index='Da te', columns='Sentiment', aggfunc=len, values='Headline') 
sentsanders = sentiment[sentiment['Candidate']=='Sanders'].pivot_table(ind ex='Date', columns='Sentiment', aggfunc=len, values='Headline') 
senttrump = sentiment[sentiment['Candidate']=='Trump'].pivot_table(index=' Date', columns='Sentiment', aggfunc=len, values='Headline') 
sentclinton = sentiment[sentiment['Candidate']=='Clinton'].pivot_table(ind ex='Date', columns='Sentiment', aggfunc=len, values='Headline')
sentcruz["Total"]=sentcruz.N.fillna(0)+sentcruz.P.fillna(0) 
sentsanders["Total"]=sentsanders.N.fillna(0)+sentsanders.P.fillna(0) 
sentclinton["Total"]=sentclinton.N.fillna(0)+sentclinton.P.fillna(0) 
senttrump["Total"]=senttrump.N.fillna(0)+senttrump.P.fillna(0)
sentclinton.head(5) 
rollcruz = pd.DataFrame(pd.rolling_sum(sentcruz['P'].fillna(0), window=10) .div(pd.rolling_sum(sentcruz['Total'].fillna(0), window=10))) 
rollcruz.columns = ['Cruz'] 
rollclinton = pd.DataFrame(pd.rolling_sum(sentclinton['P'].fillna(0), wind ow=10).div(pd.rolling_sum(sentclinton['Total'].fillna(0), window=10))) 
rollclinton.columns = ['Clinton'] 
rollsanders = pd.DataFrame(pd.rolling_sum(sentsanders['P'].fillna(0), wind ow=10).div(pd.rolling_sum(sentsanders['Total'].fillna(0), window=10))) 
rollsanders.columns = ['Sanders'] rolltrump = pd.DataFrame(pd.rolling_sum(senttrump['P'].fillna(0), window=1 0).div(pd.rolling_sum(senttrump['Total'].fillna(0), window=10))) 
rolltrump.columns = ['Trump'] 
pd.concat([rollsanders,rollclinton,rolltrump,rollcruz], axis=1).plot(title ='Positive sentiment share on rolling basis') 

