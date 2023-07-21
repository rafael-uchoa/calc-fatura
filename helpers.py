def combine_and_sum_keywords(data, keywords):
    combined_items = []

    for keyword in keywords:
        # Calculate the total sum of expenses with the specified keyword
        total_sum = sum(item[1] for item in data if keyword in item[0])

        # Remove all individual items with the specified keyword from the original list
        data = [item for item in data if keyword not in item[0]]

        # Add the combined item with the total sum rounded to two decimal places
        combined_items.append([keyword, round(total_sum, 2)])

    data.extend(combined_items)

    return data


def filter_by_keywords(data, keywords):
    # Filter out items containing any of the specified keywords
    filtered_data = [item for item in data if not any(
        keyword in item[0] for keyword in keywords)]

    return filtered_data
