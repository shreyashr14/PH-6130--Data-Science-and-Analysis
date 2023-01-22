import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

# Define the degrees of freedom
df = 3

# Draw samples once, 5 times, and 10 times
sample_sizes = [1, 5, 10]

# Create a figure and axes
fig, ax = plt.subplots(1, 3, figsize=(12, 4))

for i, n in enumerate(sample_sizes):
    # Draw samples from the chi-square distribution
    samples = np.random.chisquare(df, size=(int(1E6), n))
    # Compute the mean of the samples
    mean = samples.mean(axis=1)
    # Plot the histogram of the means
    ax[i].hist(mean, bins='auto', density=True,
               histtype='step', color='black')
    # Overplot the Gaussian distribution
    x = np.linspace(0, 15, 100)
    mu = df
    sigma = np.sqrt(2*df/n)
    ax[i].plot(x, stats.norm.pdf(x, mu, sigma), color='red', lw=2)
    ax[i].set_title('n = {0}'.format(n))
    ax[i].set_xlabel('$x$')
    ax[i].set_ylabel('$P(x)$')
