# Set the critical Z score for 90% confidence
Z_CRIT = 1.645

# Calculate share of bike commuting
dc["bike_share"] = dc["bike_est"] / dc["total_est"]

# Calculate standard errors of the estimate from MOEs
dc["se_bike"] = dc["bike_moe"] / Z_CRIT
dc["se_total"] = dc["total_moe"] / Z_CRIT
dc["se_p"] = (
    sqrt(dc["se_bike"] ** 2 - dc["bike_share"] ** 2 * dc["se_total"] ** 2)
    / dc["total_est"]
)

# Calculate the two sample statistic between 2011 and 2017
Z = (
    dc[dc["year"] == 2017]["bike_share"] - dc[dc["year"] == 2011]["bike_share"]
) / sqrt(dc[dc["year"] == 2017]["se_p"] ** 2 + dc[dc["year"] == 2011]["se_p"] ** 2)
print(Z_CRIT < Z)
