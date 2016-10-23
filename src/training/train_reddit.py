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

def inp_data():
	database = []
	movie = raw_input('Enter the movie\n')
	try:
		f = open("out_"+movie+".tsv")
		lines = f.read().decode('utf-8')
	except:
		print('No such file exists. Please ensure that the file is in format out_(moviename).tsv')
	lines = lines.split('\n')

	for line in lines[:-1]:
		line = line.split('\t')
		if len(line[1])>=15:
			database.append(line[1])
	
	database = list(set(database))
	print('length of database is: '+str(len(database)))
	return [database,movie]

[database,movie] = inp_data()
model = file1.load_model()
idx = 1000
cnt = 1
try:
	vectors = np.asarray(file1.encode(model, database[0:min(0+1000,len(database))],verbose=False))
	print(vectors.shape)
	while idx < len(database):
		print(cnt)
		out = np.asarray(file1.encode(model, database[idx:min(idx+1000,len(database))],verbose=False))
		vectors=np.concatenate((vectors,out),axis=0)
		idx+=1000
		cnt+=1
		print(vectors.shape)

except MemoryError:
	print('Vectors cannot be generated. Please check your RAM!')
except:
	print('Some sentences cannot be encoded using this representation. Try debugging!')
	
h5f = h5py.File('vectors_reddit_'+movie+'.h5', 'w')
h5f.create_dataset('dataset', data=vectors)
h5f.close()
