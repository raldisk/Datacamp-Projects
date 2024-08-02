# Retain only rows and columns of Midwest states
midwest = state_to_state[midwest_states][state_to_state.index.isin(midwest_states)]

# Are rows and columns still in the same order?
print(midwest.index == midwest.columns)

# Sort the rows (by index) and columns (by name)
midwest.sort_index(axis=0, inplace=True)
midwest.sort_index(axis=1, inplace=True)

# Create a heatmap of migration flows
sns.heatmap(midwest, cmap="YlGnBu")
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.show()
