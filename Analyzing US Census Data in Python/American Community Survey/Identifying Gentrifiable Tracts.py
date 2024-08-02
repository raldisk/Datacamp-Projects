# Median income below MSA median income
bk_2000["low_mhi"] = bk_2000["mhi"] < bk_2000["mhi_msa"]

# Recent construction below MSA
bk_2000["low_recent_build"] = (
    bk_2000["pct_recent_build"] < bk_2000["pct_recent_build_msa"]
)

# Identify gentrifiable tracts
bk_2000["gentrifiable"] = (bk_2000["low_mhi"]) & (bk_2000["low_recent_build"])

# Plot gentrifiable tracts
bk_2000.plot(column="gentrifiable", cmap="YlGn")
plt.show()
