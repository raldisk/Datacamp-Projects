# Create a basemap
basemap = bk_2000.plot(color="white", edgecolor="lightgray")

# Filter and plot gentrifiable tracts
gentrifiable_tracts = bk_2000[bk_2000["gentrifiable"]]
gentrifiable_tracts.plot(ax=basemap, color="lightgray")

# Filter and plot gentrifying tracts
gentrifying_tracts = bk_2010[bk_2010["gentrifying"]]
gentrifying_tracts.plot(ax=basemap, color="red")
plt.show()
