# Increase in percent BA greater than MSA
bk_2010["increasing_education"] = (bk_2010["pct_ba_2010"] - bk_2010["pct_ba_2000"]) > (
    bk_2010["pct_ba_msa_2010"] - bk_2010["pct_ba_msa_2000"]
)

# Increase in house value
bk_2010["increasing_house_value"] = (
    bk_2010["median_value_2010"] > bk_2010["median_value_2000"] * 1.2612
)

# Identify gentryifying tracts
bk_2010["gentrifying"] = (
    bk_2010["gentrifiable"]
    & bk_2010["increasing_education"]
    & bk_2010["increasing_house_value"]
)

# Plot gentrifying tracts
bk_2010.plot(column="gentrifying", cmap="YlOrRd")
plt.show()
