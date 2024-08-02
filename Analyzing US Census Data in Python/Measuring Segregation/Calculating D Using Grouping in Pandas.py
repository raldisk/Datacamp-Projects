# Sum Black and White residents grouped by state
sums_by_state = tracts.groupby("state")[[w, b]].sum()
print(sums_by_state.head())

# Merge the sum with the original tract populations
tracts = pd.merge(
    tracts, sums_by_state, left_on="state", right_index=True, suffixes=("", "_sum")
)
print(tracts.head())

# Calculate inner expression
tracts["D"] = abs(tracts[w] / tracts[w + "_sum"] - tracts[b] / tracts[b + "_sum"])

# Calculate Index of Dissimilarity
print(0.5 * tracts.groupby("state")["D"].sum())
