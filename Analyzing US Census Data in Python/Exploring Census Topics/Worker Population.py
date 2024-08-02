# Merge population data with geopandas DataFrame
geo_nyma = pd.merge(geo_nyma, nyma_counties, on=["state", "county"])

# Calculate population densities
geo_nyma["worker_density"] = 1000**2 * geo_nyma["worker_pop"] / geo_nyma.area
geo_nyma["residential_density"] = 1000**2 * geo_nyma["residential_pop"] / geo_nyma.area

# Compare residential and worker density plots
fig, axes = plt.subplots(ncols=2)
geo_nyma.plot(column="residential_density", cmap="YlGnBu", ax=axes[0])
geo_nyma.plot(column="worker_density", cmap="YlGnBu", ax=axes[1])
plt.show()
