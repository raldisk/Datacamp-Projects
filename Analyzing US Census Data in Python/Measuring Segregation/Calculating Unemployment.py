# 1/3
# View the first few rows of msa_black_emp
print(msa_black_emp.head())

# Calculate percentage unemployment for male, female, and all
msa_black_emp["pct_male_unemp"] = (
    100 * msa_black_emp["male_unemp"] / msa_black_emp["male_lf"]
)
msa_black_emp["pct_female_unemp"] = (
    100 * msa_black_emp["female_unemp"] / msa_black_emp["female_lf"]
)
msa_black_emp["pct_unemp"] = (
    100
    * (msa_black_emp["female_unemp"] + msa_black_emp["male_unemp"])
    / (msa_black_emp["female_lf"] + msa_black_emp["male_lf"])
)

# 2/3
## View the first few rows of msa_black_emp
# print(msa_black_emp.head())

# Calculate percentage unemployment for male, female, and all
msa_black_emp["pct_male_unemp"] = (
    100 * msa_black_emp["male_unemp"] / msa_black_emp["male_lf"]
)
msa_black_emp["pct_female_unemp"] = (
    100 * msa_black_emp["female_unemp"] / msa_black_emp["female_lf"]
)
msa_black_emp["pct_unemp"] = (
    100
    * (msa_black_emp["female_unemp"] + msa_black_emp["male_unemp"])
    / (msa_black_emp["female_lf"] + msa_black_emp["male_lf"])
)

# Merge with Index of Dissimilarity calculated previously
msa_black_emp = pd.merge(msa, msa_black_emp, on="msa")

# 3/3
## View the first few rows of msa_black_emp
# print(msa_black_emp.head())

# Calculate percentage unemployment for male, female, and all
msa_black_emp["pct_male_unemp"] = (
    100 * msa_black_emp["male_unemp"] / msa_black_emp["male_lf"]
)
msa_black_emp["pct_female_unemp"] = (
    100 * msa_black_emp["female_unemp"] / msa_black_emp["female_lf"]
)
msa_black_emp["pct_unemp"] = (
    100
    * (msa_black_emp["female_unemp"] + msa_black_emp["male_unemp"])
    / (msa_black_emp["female_lf"] + msa_black_emp["male_lf"])
)

# Merge with Index of Dissimilarity calculated previously
msa_black_emp = pd.merge(msa, msa_black_emp, on="msa")

# Plot unemployment vs. segregation
sns.lmplot(x="D", y="pct_unemp", data=msa_black_emp)
plt.show()
