#Python script for tutorial class
print("Running analysis...\n");
import numpy as np
import matplotlib.pyplot as plt
import glob

#import file names of matching type
filenames=glob.glob('data\inflammation-*csv');
for file in filenames:
	print("\n",file[5:-3])
	#import data 
	patient_data=np.loadtxt(file,delimiter=',');


	#calculate wholistic statistics
	mean=patient_data.mean();
	max=patient_data.max();
	std_dev=patient_data.std();
	print("mean:",mean);
	print("max:",max);
	print("std. dev",std_dev);


	#plot mean over time
	mean_over_time=np.mean(patient_data, axis=0);
	
	plt.figure(file)
	plt.title(file[5:-3])
	plt.xlabel("day");
	plt.ylabel("inflammation level")
	plt.plot(mean_over_time);
	plt.savefig("figures\\"+file[5:-3]+"png");
	plt.close(file)

