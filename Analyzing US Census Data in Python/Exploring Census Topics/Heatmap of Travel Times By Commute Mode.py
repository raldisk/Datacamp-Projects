# Set iter_len to the number of commute times
iter_len = len(times)

# Break row into list of lists by travel mode
data = [data_row[i : i + iter_len] for i in range(0, len(data_row), iter_len)]

# Create DataFrame, set data type to int
commuting = pd.DataFrame(data=data, index=modes, columns=times)
commuting = commuting.astype(int)

# Create heatmap of commuters by mode by income
sns.heatmap(commuting, annot=commuting // 1000, fmt="d", cmap="YlGnBu")
plt.xticks(rotation=50)
plt.yticks(rotation=50)
plt.show()
