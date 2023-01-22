import numpy as np
from scipy.stats import pearsonr, t

# Generate two arrays of size 1000 from a Gaussian distribution with mean 0 and std deviation 1
np.random.seed(0)
x = np.random.normal(0, 1, 1000)
y = np.random.normal(0, 1, 1000)

# Calculate the Pearson correlation coefficient and p-value
corr, p_value = pearsonr(x, y)
print("Pearson correlation coefficient: ", corr)

# Comparing with student's t-distribution

df = len(x) - 2
t_value = corr * np.sqrt(df / (1 - corr ** 2))
p_value_student = 2 * (1 - t.cdf(np.abs(t_value), df))
print("p-value calculated using Student-t distribution: ", p_value_student)

#it does not!
