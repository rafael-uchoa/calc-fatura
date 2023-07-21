import pandas as pd
from helpers import combine_and_sum_keywords, filter_by_keywords


def get_expenses(path, keywords_to_filter, keywords_to_combine):
    data = []

    all_sheets = pd.read_excel(path, sheet_name=None)

    for _, df in all_sheets.items():
        for _, row in df.iterrows():
            data.append(row.iloc[1:].tolist())

    data = filter_by_keywords(data, keywords_to_filter)
    data = combine_and_sum_keywords(data, keywords_to_combine)

    return sorted(data, key=lambda x: x[1], reverse=True)
