import numpy as np 
import random 

# Set the average age of employees in the company as 35 and randomize a variance and calculate the expected sigma 
mean_value = 35

sample_sigma_list = []
sample_variance_list = []

for i in range(1000): 
    # Generate a list of 1000 employees and assume the age range from 25 to 50 
    dataset = []
    for j in range(100): 
        dataset.append(random.randrange(25,50))

    # Calculate the sample mean and sample sigma of the generated dataset
    sample_mean = sum(dataset) / len(dataset)

    sample_variance = sum([(x - sample_mean)**2 for x in dataset]) / len(dataset) 
    sample_variance_list.append(sample_variance)

    sample_sigma = np.sqrt(sample_variance)
    sample_sigma_list.append(sample_sigma)

print("Estimated Variance: {}".format(np.average(sample_variance_list))) 
print("Estimated Sigma: {}".format(np.average(sample_sigma_list))) 