# Are large metros more segregated?
sns.lmplot(x="population", y="D", data=msa)
plt.show()

# Calculate percentage African-American
msa["black_pct"] = 100 * msa["black"] / msa["population"]

# Are more diverse metros more segregated?
sns.lmplot(x="black_pct", y="D", data=msa)
plt.show()

# Display metro size, percent Black, and segregation in one plot
sns.scatterplot(x="black_pct", y="D", size="population", hue="population", data=msa)
plt.show()
