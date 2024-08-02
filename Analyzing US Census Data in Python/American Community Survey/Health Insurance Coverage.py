# Calculate percent insured
states["insured_total"] = (
    states["m_school_insured"]
    + states["m_noschool_insured"]
    + states["f_school_insured"]
    + states["f_noschool_insured"]
)
states["pct_insured"] = 100 * states["insured_total"] / states["total"]

# Pivot the table and rename the columns
states_pvt = states.pivot(index="state", columns="year", values="pct_insured")
states_pvt.columns = ["pct_insured_2013", "pct_insured_2017"]

# Calculate the change in insurance rates 2013 to 2017
states_pvt["pct_insured_change"] = (
    states_pvt["pct_insured_2017"] - states_pvt["pct_insured_2013"]
)

# Plot the change against initial (2013) insurance rates
sns.lmplot(x="pct_insured_2013", y="pct_insured_change", data=states_pvt)
plt.show()
