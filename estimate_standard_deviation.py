import numpy as np 
import random 

# Set the average age of employees in the company as 35 and randomize a variance and calculate the expected sigma 
mean_value = 35
variance = random.randrange(10,50)
expected_sigma = np.sqrt(variance)
print(f"Variance: {variance}")
print(f"Expected Sigma: {expected_sigma}")


# Generate a dataset of 10000 points in normal distribution from the given data attributes
dataset = np.random.normal(mean_value, np.sqrt(variance), 10000) 

# Calculate the sample mean and sample sigma of the generated dataset
sample_mean = sum(dataset) / len(dataset)

sample_variance = sum([(x - sample_mean)**2 for x in dataset]) / len(dataset) 
sample_sigma = np.sqrt(sample_variance)

print(f"Sample Mean: {sample_mean}")
print(f"Sample Sigma: {sample_sigma}")