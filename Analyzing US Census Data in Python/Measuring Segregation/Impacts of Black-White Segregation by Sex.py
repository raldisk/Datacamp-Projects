# 1/3
# Restrict DataFrame to columns of interest, rename columns
tidy_black_emp = msa_black_emp[["msa", "D", "pct_male_unemp", "pct_female_unemp"]]
tidy_black_emp.columns = ["msa", "D", "male", "female"]

# 2/3
# Restrict DataFrame to columns of interest, rename columns
tidy_black_emp = msa_black_emp[["msa", "D", "pct_male_unemp", "pct_female_unemp"]]
tidy_black_emp.columns = ["msa", "D", "male", "female"]

# Use melt to create tidy DataFrame, and view the first few rows
tidy_msa_emp = tidy_black_emp.melt(
    id_vars=["msa", "D"],
    value_vars=["male", "female"],
    var_name="sex",
    value_name="unemployment",
)
print(tidy_msa_emp.head())

# 3/3
# Restrict DataFrame to columns of interest, rename columns
tidy_black_emp = msa_black_emp[["msa", "D", "pct_male_unemp", "pct_female_unemp"]]
tidy_black_emp.columns = ["msa", "D", "male", "female"]

# Use melt to create tidy DataFrame, and view the first few rows
tidy_msa_emp = tidy_black_emp.melt(
    id_vars=["msa", "D"],
    value_vars=["male", "female"],
    var_name="sex",
    value_name="unemployment",
)

# Visually compare male and female unemployment
sns.lmplot(x="D", y="unemployment", hue="sex", data=tidy_msa_emp)
plt.show()
