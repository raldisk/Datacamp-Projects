# Calculate percent Black in 1990 and percentage point change from 1990 to 2000
tracts_cook["pct_black_1990"] = (
    100 * tracts_cook["black_1990"] / tracts_cook["totalpop_1990"]
)
tracts_cook["pct_black_change"] = (
    tracts_cook["pct_black_2010"] - tracts_cook["pct_black_1990"]
)

# Retain tracts between 30% and 70% Black in 1990
tracts_mixed = tracts_cook[
    (tracts_cook["pct_black_1990"] >= 30) & (tracts_cook["pct_black_1990"] <= 70)
]

# Plot change vs. percent Black in 1990, with "no change" reference line
sns.regplot(x="pct_black_1990", y="pct_black_change", lowess=True, data=tracts_mixed)
plt.plot([30, 70], [0, 0], linestyle="--", color="red")
plt.show()
