# Create point GeoDataFrame at centroid of states
geo_state_pt = geo_state.copy()
geo_state_pt["geometry"] = geo_state_pt.centroid

# Calculate percentage of internet households with broadband
geo_state["pct_broadband"] = 100 * geo_state["broadband"] / geo_state["internet"]

# Set choropleth basemap
basemap = geo_state.plot(column="pct_broadband", cmap="YlGnBu")

# Plot transparent proportional symbols on top of basemap
geo_state_pt.plot(
    ax=basemap,
    markersize=sqrt(geo_state["internet"]) / 5,
    color="lightgray",
    edgecolor="darkgray",
    alpha=0.7,
)
plt.show()
