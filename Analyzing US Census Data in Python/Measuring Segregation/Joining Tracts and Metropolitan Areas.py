# Find identifiers for 50 largest metros by population
msa50 = list(msa.nlargest(50, "population")["msa"])

# Join MSA identifiers to tracts, restrict to largest 50 metros
msa_tracts = pd.merge(tracts, msa_def, on=["state", "county"])
msa_tracts = msa_tracts[msa_tracts["msa"].isin(msa50)]

# Calculate D using custom function, merge back into MSA
msa_D = dissimilarity(msa_tracts, "white", "black", "msa")
msa = pd.merge(msa, msa_D, left_on="msa", right_index=True)

# Plot five most segregated metros
sns.stripplot(x="D", y="name", data=msa.nlargest(10, "D"))
plt.show()
