import requests
import pandas as pd
import json

def get_data(api_key, table_id):
    base_url = "https://api.census.gov/data/2019/acs/acs5"
    params = {
        'get': 'group({})'.format(table_id),
        'for': 'zip code tabulation area:*',
        'in': 'state:48',  # 48 is the state code for Texas
        'key': api_key
    }
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
    api_key = ''
    table_id = 'B23025'
    data = get_data(api_key, table_id)

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data[1:], columns=data[0])

    # List of Fort Worth ZIP codes
    fort_worth_zips = ['76101', '76102', '76103', '76104', '76105', '76106', '76107', '76108', '76109', '76110',
                       '76111', '76112', '76113', '76114', '76115', '76116', '76118', '76119', '76120', '76121',
                       '76122', '76123', '76124', '76126', '76129', '76130', '76131', '76132', '76133', '76134',
                       '76135', '76136', '76137', '76140', '76147', '76148', '76150', '76155', '76161', '76162',
                       '76163', '76164', '76177', '76178', '76179', '76181', '76185', '76191', '76192', '76193',
                       '76195', '76196', '76197', '76198', '76199', '76039', '76036', '76248', '76127', '76053',
                       '76117', '76244', '76012', '76180', '76182', '76013']

    # Filter the DataFrame to include only the rows with ZIP codes in Fort Worth
    df = df[df['zip code tabulation area'].isin(fort_worth_zips)]

    # Read the CSV file with column descriptions into a DataFrame
    column_descriptions_df = pd.read_csv('column_descriptions.csv')

    # Convert the DataFrame to a dictionary
    column_descriptions = column_descriptions_df.set_index('Name')['Label'].to_dict()

    # Rename the columns in the DataFrame
    df.rename(columns=column_descriptions, inplace=True)

    # Remove "!" from column names
    df.columns = df.columns.str.replace('!', ' ')

    # Remove extra spaces from column names
    df.columns = [' '.join(col.split()) for col in df.columns]

    # Save the filtered data to a CSV file
    df.to_csv('acs_employment_data_fort_worth.csv', index=False)


if __name__ == "__main__":
    main()
