#Pegasos sentiment classifier algorithm
import numpy as np 
from collections import Counter 
from sklearn.metrics import accuracy_score 

def dotProduct(d1, d2):    
	"""    This function returns the dot product between d1 and d2    """    
	if len(d1) < len(d2):        
		return dotProduct(d2, d1)    
	else:        
		return sum(d1.get(f, 0) * v for f, v in d2.items()) 
		
def increment(d1, scale, d2):    
	"""    This function increments the elements of d1 rather than    build a new dictionary and return it    """    
	for f, v in d2.items():        
		d1[f] = d1.get(f, 0) + v * scale

def scalar_mult(d1, scale):    
	temp = Counter({})    
	if(scale == 0):        
		return temp    
	for f, v in d1.items():        
		temp[f] = v * scale    
	return temp 

def read_data_test_get_accuracy(test_file, decision_function, file_to_dump) :    
	'''    Reads each file into strings    '''    
	f = open(test_file)    
	d = open(file_to_dump,"w")    
	lines = f.read().split('\n')    
	for line in lines:        
		symbols = '${}()[].,:;+-*/&|<>=~" '        
		line1 = line.split(' ')        
		words = map(lambda Element: Element.translate(None, symbols).strip (), line1)        
		words = filter(None, words)        
		pred = dotProduct(decision_function, Counter(words))        
		if pred >= 0:            
			review = "P"        
		else:            
			review = "N"        
		line = line + '\t' + review + '\n'        
		d.write(line) 
		
def read_data(file, label):    
	'''    Read each file into a list of strings.    '''    
	f = open(file)    
	review = []    
	lines = f.read().split('\n')    
	for line in lines:        
		symbols = '${}()[].,:;+-*/&|<>=~" '        
		line = line.split(' ')        
		words = map(lambda Element: Element.translate(None, symbols).strip (), line)        
		words = filter(None, words)        
		words.append(label)        
		review.append(words)    
	return review 
	
def shuffle_data():    
	'''    Paths for positive and negative reviews are given in pos_path    and neg_path, respectively    '''    
	pos_path = "file_path\Positive.txt"    
	neg_path = "file_path\Negative.txt"    
	pos_review = read_data(pos_path,1)    
	neg_review = read_data(neg_path,-1)    
	all_review = pos_review + neg_review    
	return all_review 
	
def convert_to_dict_representation(reviews):    
	"""    Function for sparse representation    """    
	all_reviews = []    
	for review in reviews:        
		all_reviews.append(Counter(review))    
	return all_reviews 

def pegasos(X_train, alpha, lambda_reg, num_epochs):    
	"""    We use the SVM algorithm called pegasos    """    
	num_instances = len(X_train)    
	theta = {}    
	step_size = alpha    
	t = 2    
	for i in range(0, num_epochs):        
		for j in range(0, num_instances):            
			step_size = 1.0/(t * lambda_reg)            
			y = 1            
			if(X_train[j].get(-1)>0):                
				y = -1            
				X = X_train[j]            
			if(y * dotProduct(theta, X) < 1):                
				theta = scalar_mult(theta, 1- step_size * lambda_reg)                
				increment(theta,1, scalar_mult(X, step_size * y))            
			else:                
				theta = scalar_mult(theta,1- step_size * lambda_reg)            
				t= t+1    
	return theta 
	
def model_error(true,pred):    

	f_true = open(true)    
	f_pred = open(pred)    
	lines_true = f_true.read().split('\n')    
	lines_pred = f_pred.read().split('\n')    
	total = len(lines_pred)    
	score = accuracy_score(lines_true,lines_pred, normalize=False)    
	correct = (score * 1.0 / total) * 100.0    
	print "Accuracy(%):" ,correct 
	
def main():    
np.random.seed(10)    
print('Reading and converting data to sparse representation.')    
all_rev = shuffle_data()    
all_reviews = convert_to_dict_representation(all_rev)    
print('Preparing training and test set')    
X_train = all_reviews    
t1 = pegasos(X_train, 0.1,10, 2)
test_file = "file_path\\Test.txt"    
file_to_dump = "file_path\Output.txt"    
print("Classified sentiments!!")    
read_data_test_get_accuracy(test_file, t1, file_to_dump)
if __name__ == "__main__":    
	main()