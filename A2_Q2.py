import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Read the data from the url
data = pd.read_csv("http://www.iith.ac.in/~shantanud/test.dat", delimiter=' ', header=None, names=['Luminosity', 'Redshift'],skiprows=1)


# Plot the data on a log-log scale
plt.loglog(data['Redshift'], data['Luminosity'], 'o')
plt.xlabel('Redshift')
plt.ylabel('Luminosity')
plt.show()

# Calculate the correlation coefficients and p-values
spearman_coef, spearman_pvalue = stats.spearmanr(data['Redshift'], data['Luminosity'])
pearson_coef, pearson_pvalue = stats.pearsonr(data['Redshift'], data['Luminosity'])
kendall_coef, kendall_pvalue = stats.kendalltau(data['Redshift'], data['Luminosity'])

print("Spearman correlation coefficient: ", spearman_coef)
print("Spearman p-value: ", spearman_pvalue)
print("Pearson correlation coefficient: ", pearson_coef)
print("Pearson p-value: ", pearson_pvalue)
print("Kendall-tau correlation coefficient: ", kendall_coef)
print("Kendall-tau p-value: ", kendall_pvalue)
