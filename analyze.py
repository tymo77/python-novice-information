#Python script for tutorial class
print("Running analysis...\n");
import numpy as np
import matplotlib.pyplot as plt
import glob
import tools

#import file names of matching type
filenames=glob.glob('data\inflammation-*csv');
for file in filenames:
	print("\n",file[5:-3])
	#import data 
	patient_data=np.loadtxt(file,delimiter=',');

	#calculate and display wholistic statistics
	tools.analyze_csv(file);

	# #plot mean over time
	mean_over_time=np.mean(patient_data, axis=0);
	
	#open figure
	plt.figure(file);
	#decorate
	plt.title(file[5:-3]);
	plt.xlabel("day");
	plt.ylabel("inflammation level");
	
	# #plot
	plt.plot(mean_over_time);
	
	#save and close figure
	plt.savefig("figures\\"+file[5:-3]+"png");
	plt.close(file)

