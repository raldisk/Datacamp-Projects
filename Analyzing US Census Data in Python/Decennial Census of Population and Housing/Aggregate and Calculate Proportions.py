# 1/2
# What percentage of Hispanics identify as White?
print(100 * states["hispanic_white"].sum() / states["hispanic"].sum())


# 2/2
# Set list of Hispanic race column names
hispanic_races = [
    "hispanic_white",
    "hispanic_black",
    "hispanic_aian",
    "hispanic_asian",
    "hispanic_pacific",
    "hispanic_other",
    "hispanic_multiracial",
]

# What percentage of Hispanics identify as each race?
print(100 * states[hispanic_races].sum() / states["hispanic"].sum())
