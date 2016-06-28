#Python script for tutorial class
print("Running analysis...\n");
import numpy as np
import matplotlib.pyplot as plt
import glob

def analyze_csv(filename):
	"""
	Reads the file "filename" and prints the mean, max, and standard deviation
	for the data in "filename"
	"""
	#import data 
	patient_data=np.loadtxt(file,delimiter=',');

	#calculate wholistic statistics
	mean=patient_data.mean();
	max=patient_data.max();
	std_dev=patient_data.std();
	print("mean:",mean);
	print("max:",max);
	print("std. dev",std_dev);

#import file names of matching type
filenames=glob.glob('data\inflammation-*csv');
for file in filenames:
	print("\n",file[5:-3])
	#import data 
	patient_data=np.loadtxt(file,delimiter=',');

	#calculate and display wholistic statistics
	analyze_csv(file)

	#plot mean over time
	mean_over_time=np.mean(patient_data, axis=0);
	
	#open figure
	plt.figure(file);
	#decorate
	plt.title(file[5:-3]);
	plt.xlabel("day");
	plt.ylabel("inflammation level");
	
	#plot
	plt.plot(mean_over_time);
	
	#save and close figure
	plt.savefig("figures\\"+file[5:-3]+"png");
	plt.close(file)

