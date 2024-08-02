# Calculate new immigrants as percent of current population
us_immigration["pct_new_immigrant"] = (
    100 * us_immigration["new_immigrant"] / us_immigration["total"]
)

# Create a barplot
sns.barplot(
    x="year", y="pct_new_immigrant", data=us_immigration, color="cornflowerblue"
)
plt.show()
