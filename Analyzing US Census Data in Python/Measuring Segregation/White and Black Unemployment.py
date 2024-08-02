# Restrict DataFrame to columns of interest, rename columns
tidy_black_emp = msa_black_emp[["msa", "D", "pct_male_unemp"]]
tidy_black_emp.columns = ["msa", "D", "black"]
tidy_white_emp = msa_white_emp[["msa", "pct_male_unemp"]]
tidy_white_emp.columns = ["msa", "white"]
tidy_emp = pd.merge(tidy_black_emp, tidy_white_emp, on="msa")

# Use melt to create tidy DataFrame
tidy_msa_emp = tidy_emp.melt(
    id_vars=["msa", "D"],
    value_vars=["white", "black"],
    var_name="race",
    value_name="unemployment",
)

# Visually compare male and female unemployment
sns.lmplot(x="D", y="unemployment", hue="race", data=tidy_msa_emp)
plt.show()
