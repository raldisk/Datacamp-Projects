# Rename columns
unemp_by_race.rename(columns=col_rename, inplace=True)

# Melt DataFrame by demographic group
unemp_by_race = unemp_by_race.melt(
    id_vars="year", var_name="demographic", value_name="pct_unemployed"
)

# Plot unemployment by group by year
sns.barplot(x="year", y="pct_unemployed", hue="demographic", data=unemp_by_race)
plt.show()
