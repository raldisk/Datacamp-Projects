# Get list of state FIPS Codes
states = list(tracts["state"].unique())

state_D = {}  # Initialize dictionary as collector
for state in states:
    # Filter by state
    tmp = tracts[tracts["state"] == state]

    # Add Index of Dissimilarity to Dictionary
    state_D[state] = 0.5 * sum(abs(tmp[w] / tmp[w].sum() - tmp[b] / tmp[b].sum()))

# Print D for Georgia (FIPS = 13) and Illinois (FIPS = 17)
print("Georgia D =", round(state_D["13"], 2))
print("Illinois D =", round(state_D["17"], 2))
