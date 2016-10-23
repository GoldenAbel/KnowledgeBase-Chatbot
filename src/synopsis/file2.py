try:
	import warnings
	import sys
	import time
except:
	print('You might get weird python errors. Please ignore!')
try:
	import file1
except:
	print('Please ensure you have all required scripts! 1 file missing!')
	sys.exit()
try:
	import nltk
except:
	print('Install NLTK! Library missing!')
	sys.exit()
try:
	from sklearn.neighbors import NearestNeighbors
except:
	print('Scikit-learn not found. Please install Scikit-learn')
	sys.exit()
try:
	import numpy as np
except:
	print('NumPy not found! Please install NumPy')
	sys.exit()

try:
	import h5py
except:
	print('High speed hierachial data I/O format not found. Please install h5py: The HDF5 wrapper for python')
	sys.exit()

warnings.filterwarnings("ignore")

def get_inp(movie):
	try:
		f = open("synout_"+movie+".txt")
		lines = f.read().decode('utf-8')
		lines = lines.split('\n')
		for line in lines[:-1]:
			database.append(line)
		return database
	except MemoryError:
		print('System out of RAM space! Please use a bigger system! My AI Brain is having trouble in this small a space!')
		sys.exit()
	except:
		print('reddit.tsv: File not found. Please check your data organization!')
		sys.exit()

database = []


try:
	f=open('synopsis_list.txt')
	lines = f.read().split('\n')
	val = 1
	for line in lines:
		print('Press '+str(val)+' to start the movie: '+line)
		val +=1 
except:
	print('synopsis_list.txt not found!')
	sys.exit()
try:
	inp = raw_input()
	inp = int(inp)
	if inp >= 1 and inp <= val:
		movie = lines[inp-1]
		database = get_inp(movie) 
	else:
		print('Incorrect input. Exiting...')
		sys.exit()
except:
	print('Incorrect input. Exiting...')
	sys.exit()
print('Initializing ChatBot Release1- Movie: '+movie+' Version: Synopsis')
print('Initializing... (Optimization might take some time, please wait)')
try:
	h5f = h5py.File('vectors_synopsis_'+movie+'.h5','r+')
	vectors = h5f['dataset'][:]
	h5f.close()
	vectors = np.asarray(vectors)
except MemoryError:
	print('System out of RAM space! Please use a bigger system! My AI Brain is having trouble in this small a space!')
	sys.exit()
except:
	print('vectors_synopsis_*moviename*.h5: File not found. Please check your data organization!')
	sys.exit()
try:
	model = file1.load_model()
except MemoryError:
	print('System out of RAM space! Please use a bigger system! My AI Brain is having trouble in this small a space!')
	sys.exit()
except:
	print('Loading of brain failed! Please check the error!')
	sys.exit()

ques=''
try:
	nbrs = NearestNeighbors(n_neighbors=50, algorithm='ball_tree').fit(vectors)
except:
	print('Database optimization failed! Please check the Ball KD Tree code!')
	sys.exit()

queryno = 0
while ques !='Q':
	try:
	#if 1==1:
		ques=[]
		f = open('input_'+movie+'_synopsis.txt','r+')
		lines = f.read().split('\n')
		f.close()
		ques.append(lines[0])
		postagged = nltk.pos_tag(nltk.tokenize.word_tokenize(ques[0]))
		vec_ques = file1.encode(model, ques, verbose=False)
		f=open('nouns_query_'+movie+'_synopsis.txt','w')
		for pairs in postagged:
			if pairs[1] == 'NN':
				f.write(pairs[0]+'\n')
		f.close()			
		distances, indices = nbrs.kneighbors(vec_ques[0])
		list_indices = list(indices.flatten())
		w=1
		f = open('output_'+movie+'_synopsis.txt','w')
		for i in list_indices:
			f.write(database[i].encode('utf-8')+'\n')
			w+=1
		queryno+=1
		print(' ')
		print(' ')
		time.sleep(1)
	except:
		print('Please ensure your query is in proper English please. Our AI is having trouble understanding you!')
		sys.exit()