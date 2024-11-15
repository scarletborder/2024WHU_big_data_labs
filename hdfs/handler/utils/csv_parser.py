from datetime import datetime


def csv_to_json(csv_string: str):
    # Split the CSV data into lines
    lines = csv_string.strip().split("\n")

    # Extract the headers
    headers = lines[0].split(", ")

    # Process each line and convert to a dictionary format
    json_result = []
    for line in lines[1:]:
        values = line.split(", ")
        entry = {headers[i]: values[i] for i in range(len(headers))}
        json_result.append(entry)

    return json_result


def accumulate_csv_to_json(existing_json: list, csv_string: str):
    # Split the CSV data into lines
    lines = csv_string.strip().split("\n")

    # Extract the headers
    headers = lines[0].split(", ")

    # Process each line and convert to a dictionary format
    for line in lines[1:]:
        values = line.split(", ")
        entry = {headers[i]: values[i] for i in range(len(headers))}
        existing_json.append(entry)

    return existing_json
