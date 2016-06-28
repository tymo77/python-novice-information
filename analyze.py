#Python script for tutorial class
print("Running analysis...\n");
import numpy as np
import matplotlib.pyplot as plt

#import data 
patient_data=np.loadtxt('data/inflammation-01.csv',delimiter=',');


#calculate wholistic statistics
mean=patient_data.mean();
max=patient_data.max();
std_dev=patient_data.std();
print("mean    max  std. dev:")
print(mean,max,std_dev)

#plot mean over time
mean_over_time=np.mean(patient_data, axis=0);

plt.plot(mean_over_time);
plt.show()

