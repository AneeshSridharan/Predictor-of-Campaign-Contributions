import requests 
import re 
import json 
import csv 
def nytimes():    
	news = []    
	candidates=('Trump', 'Clinton','Cruz','Sanders','Kasich')    
	for c in candidates:        
		for j in range(1,101):            
		url1 = 'http://api.nytimes.com/svc/search/v2/articlesearch.json ?' + \
		'&fq=headline:'+ c + \            
		'&begin_date=20160101' + \            
		'&sort=newest'+ \            
		'&fl=headline,pub_date'+ \            
		'&page='+str(j)+ \            
		'&facet_field=source&facet_filter=true' + \            
		'&api-key=0ab297e8ff925ebc9ed44d05cd92cba9:6:75143083'             
		
		resp = requests.get(url1)            
		results = json.loads(resp.text)

        for i in results['response']['docs']:                
			dic = {}                
			dic['headline'] = i['headline']['main']                
			dic['date'] = i['pub_date'][0:10]                
			dic['candidate']= c                
			news.append(dic)    
	return(news) 

import csv 
data=nytimes() 
keys = data[0].keys() 
with open('pruebanyt.csv', 'w') as output_file:    
	dict_writer = csv.DictWriter(output_file, delimiter=',', lineterminato r='\n', fieldnames=keys)    
	dict_writer.writeheader()    
	dict_writer.writerows(data)
