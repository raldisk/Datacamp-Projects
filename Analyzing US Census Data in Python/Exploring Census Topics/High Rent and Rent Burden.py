# Merge geometries with rent data
sf_tracts = sf_tracts.merge(sf_rent, on=["state", "county", "tract"])

# Plot median rent by Census tract
sf_tracts[sf_tracts["median_rent"].notnull()].plot(column="median_rent", cmap="YlGnBu")
plt.show()
plt.close()

# Plot median rent as percentage of income
sf_tracts.plot(column="median_rent_pct_of_income", cmap="YlGnBu")
plt.show()

# Show correlation between median rent and percent of income
print(sf_tracts["median_rent"].corr(sf_tracts["median_rent_pct_of_income"]))
