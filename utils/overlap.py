def check_overlap(df):

    df.columns = df.columns.str.strip()

    duplicates = df["Category"].value_counts()

    overlap = duplicates[
        duplicates > 1
    ]

    return overlap.to_dict()