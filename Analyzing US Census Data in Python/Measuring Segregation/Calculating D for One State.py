# Define convenience variables to hold column names
w = "white"
b = "black"

# Extract Georgia tracts
ga_tracts = tracts[tracts["state"] == "13"]

# Print sums of Black and White residents of Georgia
print(ga_tracts[[w, b]].sum())

# Calculate Index of Dissimilarity and print rounded result
D = 0.5 * sum(
    abs(ga_tracts[w] / ga_tracts[w].sum() - ga_tracts[b] / ga_tracts[b].sum())
)

print("Dissimilarity (Georgia):", round(D, 3))
