# 1/2
# Calculate percent population change 1990-2010
tracts_cook["pct_pop_change"] = (
    100
    * (tracts_cook["totalpop_2010"] - tracts_cook["totalpop_1990"])
    / tracts_cook["totalpop_1990"]
)

# Examine histogram of percent population change
sns.distplot(tracts_cook["pct_pop_change"], kde=False)
plt.show()


# 2/2
# Calculate percent population change 1990-2010
tracts_cook["pct_pop_change"] = (
    100
    * (tracts_cook["totalpop_2010"] - tracts_cook["totalpop_1990"])
    / tracts_cook["totalpop_1990"]
)

# Filter out very high growth census tracts
tracts_change = tracts_cook[tracts_cook["pct_pop_change"] <= 100]

# Plot population change vs. percent Black in 1990
sns.scatterplot(x="pct_black_1990", y="pct_pop_change", data=tracts_change)
plt.plot([0, 100], [0, 0], linestyle="--", color="red")
plt.show()
