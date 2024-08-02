# Specify variables and execute API request
get_vars = ["NAME", "PCT021005", "PCT021015"]
predicates["get"] = ",".join(get_vars)
r = requests.get(base_url, params=predicates)

# Construct DataFrame
col_names = ["name", "in_adult", "in_juvenile", "state"]
states = pd.DataFrame(columns=col_names, data=r.json()[1:])
states[["in_adult", "in_juvenile"]] = states[["in_adult", "in_juvenile"]].astype(int)

# Calculate percentage of incarcerated male minors in adult facilities
states["pct_in_adult"] = (
    100 * states["in_adult"] / (states["in_adult"] + states["in_juvenile"])
)
states.sort_values(by="pct_in_adult", ascending=False, inplace=True)
sns.stripplot(x="pct_in_adult", y="name", data=states)
plt.show()
