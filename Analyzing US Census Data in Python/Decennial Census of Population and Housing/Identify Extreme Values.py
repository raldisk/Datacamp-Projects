# Import seaborn and matplotlib.plt
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# Create a boxplot
sns.boxplot(data=states_hr, orient="h")
plt.show()

# Show states with extreme values in various columns
print(states_hr.nlargest(1, "hispanic_white").squeeze())
print(states_hr.nsmallest(1, "hispanic_other").squeeze())
print(states_hr.nlargest(1, "hispanic_asian").squeeze())
