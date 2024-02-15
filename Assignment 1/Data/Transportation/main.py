import requests
import pandas as pd
import json


def get_data(api_key, table_id):
    base_url = "https://api.census.gov/data/2019/acs/acs5"
    params = {
        'get': 'group({})'.format(table_id),
        'for': 'place:*',
        'in': 'state:48',  # 48 is the state code for Texas
        'key': api_key
    }
    params_str = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"{base_url}?{params_str}"

    print(url)  # Print the URL
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: HTTP {response.status_code} returned from API request")
        return None

    # Check if the response is not empty
    if not response.text:
        print("Error: Empty response from API request")
        return None

    # Try to parse the response as JSON
    try:
        data = response.json()
    except json.JSONDecodeError:
        print("Error: Response is not valid JSON. Here's the response text:")
        print(response.text)
        return None

    return data


def main():
    api_key = '4e084339c10cc3e5a2314cda67d6d50ab4907b2b'  # Replace with your actual API key
    table_id = 'B08301'  # Replace with the table ID for the data you're interested in
    data = get_data(api_key, table_id)

    # Convert the data to a pandas DataFrame and save it to a CSV file
    df = pd.DataFrame(data[1:], columns=data[0])
    df.to_csv('acs_data.csv', index=False)


if __name__ == "__main__":
    main()
