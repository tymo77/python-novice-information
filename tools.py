import numpy as np

def analyze_csv(filename):
	"""
	Reads the file "filename" and prints the mean, max, and standard deviation
	for the data in "filename"
	"""
	data=np.loadtxt(filename,delimiter=',');
	mean=data.mean();
	max=data.max();
	std_dev=data.std();
	return[mean,max,std_dev];