# Create point GeoDataFrame at centroid of states
geo_state_pt = geo_state.copy()
geo_state_pt["geometry"] = geo_state_pt.centroid

# Set basemap and create variable for markersize
basemap = geo_state.plot(color="tan", edgecolor="black")
ms = sqrt(geo_state_pt["internet"]) / 5

# Plot proportional symbols on top of basemap
geo_state_pt.plot(ax=basemap, markersize=ms, color="lightgray", edgecolor="darkgray")
plt.show()
