# Import graphics packages
import seaborn as sns

sns.set()
import matplotlib.pyplot as plt

# Calculate and inspect Relative Margin of Error
philly["rmoe"] = 100 * philly["median_home_value_moe"] / philly["median_home_value"]
print(philly)

# Create line plot with error bars of 90% MOE
plt.errorbar("year", "median_home_value", yerr="median_home_value_moe", data=philly)
plt.show()
