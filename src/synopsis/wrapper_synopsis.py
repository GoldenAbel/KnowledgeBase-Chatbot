import time

movie = ''

def getmovie(inpmovie):
	global movie 
	movie = inpmovie

def query(query):
	global movie
	f = open('input_'+movie+'_synopsis.txt','w')
	f.write(query+'\n')
	f.close()
	f = open('output_'+movie+'_synopsis.txt','w')
	f.write('file created!')
	f.close()
	time.sleep(1)
	f = open('output_'+movie+'_synopsis.txt','r+')
	lines = f.read().split('\n')[:-1]
	f.close()