# Loop over years 2011 to 2017
for year in range(2011, 2018):
    base_url = "/".join([HOST, str(year), dataset])
    r = requests.get(base_url, params=predicates)
    df = pd.DataFrame(columns=col_names, data=r.json()[1:])
    # Add column to df to hold year value, append df to collector dfs
    df["year"] = year
    dfs.append(df)

# Concatenate all DataFrames, fix column type
states = pd.concat(dfs, ignore_index=True)
states["median_home_value"] = states["median_home_value"].astype(int)

sns.lineplot("year", "median_home_value", data=states)
plt.show()
