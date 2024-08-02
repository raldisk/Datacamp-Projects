# Calculate percent Black in 2010
tracts_cook["pct_black_2010"] = (
    100 * tracts_cook["black_2010"] / tracts_cook["totalpop_2010"]
)

# Examine histogram of percent Black
sns.distplot(tracts_cook["pct_black_2010"], kde=False)
plt.show()
