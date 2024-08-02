# Import geopandas
import geopandas as gpd

# Load geospatial data
geo_state = gpd.read_file("states_internet.gpkg")

# View GeoDataFrame columns
print(geo_state.columns)

# Calculate percent of households with no internet
geo_state["pct_no_internet"] = 100 * geo_state["no_internet"] / geo_state["total"]

# Create choropleth map using YlGnBu colormap
geo_state.plot(column="pct_no_internet", cmap="YlGnBu")
plt.show()
