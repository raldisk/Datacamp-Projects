# Melt DataFrame by demographic group
lf_by_race = lf_by_race.melt(
    id_vars="year", var_name="demographic", value_name="labor_force_participation"
)

# Plot labor force particpation by group by year
sns.barplot(x="year", y="labor_force_participation", hue="demographic", data=lf_by_race)
plt.show()
