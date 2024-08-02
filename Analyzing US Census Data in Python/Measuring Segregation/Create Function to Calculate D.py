def dissimilarity(df, col_A, col_B, group_by):
    # Sum Group A and Group B by grouping column
    grouped_sums = df.groupby(group_by)[[col_A, col_B]].sum()
    tmp = pd.merge(
        df, grouped_sums, left_on=group_by, right_index=True, suffixes=("", "_sum")
    )

    # Calculate inner expression
    tmp["D"] = abs(tmp[col_A] / tmp[col_A + "_sum"] - tmp[col_B] / tmp[col_B + "_sum"])

    # Calculate Index of Dissimilarity and convert to DataFrame
    return 0.5 * tmp.groupby(group_by)["D"].sum().to_frame()


msa_D = dissimilarity(msa_tracts, "white", "black", "msa_name")
print(msa_D.head())
