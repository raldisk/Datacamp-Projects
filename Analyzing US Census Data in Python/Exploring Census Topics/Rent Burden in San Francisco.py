# 1/3
# Calculate percentage of rent burdened households
rent_burden = rent[["name"]]
for income in incomes:
    rent_burden[income] = (
        100
        * (
            rent[income + "_rent_30_to_35_pct"]
            + rent[income + "_rent_35_to_40_pct"]
            + rent[income + "_rent_40_to_50_pct"]
            + rent[income + "_rent_over_50_pct"]
        )
        / (rent[income] - rent[income + "_rent_not_computed"])
    )

# 2/3
# Calculate percentage of rent burdened households
rent_burden = rent[["name"]]
for income in incomes:
    rent_burden[income] = (
        100
        * (
            rent[income + "_rent_30_to_35_pct"]
            + rent[income + "_rent_35_to_40_pct"]
            + rent[income + "_rent_40_to_50_pct"]
            + rent[income + "_rent_over_50_pct"]
        )
        / (rent[income] - rent[income + "_rent_not_computed"])
    )

# Melt the DataFrame
rent_burden = rent_burden.melt(
    id_vars="name", var_name="income", value_name="percent_rent_burdened"
)


# 3/3
# Calculate percentage of rent burdened households
rent_burden = rent[["name"]]
for income in incomes:
    rent_burden[income] = (
        100
        * (
            rent[income + "_rent_30_to_35_pct"]
            + rent[income + "_rent_35_to_40_pct"]
            + rent[income + "_rent_40_to_50_pct"]
            + rent[income + "_rent_over_50_pct"]
        )
        / (rent[income] - rent[income + "_rent_not_computed"])
    )

# Melt the DataFrame
rent_burden = rent_burden.melt(
    id_vars="name", var_name="income", value_name="percent_rent_burdened"
)

# Create a barplot
sns.barplot(x="income", y="percent_rent_burdened", hue="name", data=rent_burden)
plt.xticks(rotation=50)
plt.show()
