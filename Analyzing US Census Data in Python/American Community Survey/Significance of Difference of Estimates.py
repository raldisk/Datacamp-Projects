# Set the critical Z score for 90% confidence, prepare message
Z_CRIT = 1.645
msg = "Philadelphia median home values in {} were {}significantly different from {}."
for year in range(2012, 2018):
    # Assign current and prior year's median home value to variables
    x1 = int(philly[philly["year"] == year]["median_home_value"])
    x2 = int(philly[philly["year"] == year - 1]["median_home_value"])

    # Calculate standard error as 90% MOE / critical Z score
    se_x1 = float(philly[philly["year"] == year]["median_home_value_moe"] / Z_CRIT)
    se_x2 = float(philly[philly["year"] == year - 1]["median_home_value_moe"] / Z_CRIT)

    # Calculate two-sample z-statistic, output message if greater than critical Z score
    z = (x1 - x2) / sqrt(se_x1**2 + se_x2**2)
    print(msg.format(year, "" if abs(z) > Z_CRIT else "not ", year - 1))
