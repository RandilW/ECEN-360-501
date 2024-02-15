import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'restTAB'})  # Find the table with class 'restTAB'

    data = []
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) == 8:
            name = cols[0].text.strip()
            users_rating = cols[1].find('div', {'class': 'br_stars'}).get('title', 'n/a')
            type_ = cols[2].text.strip()
            address = cols[3].text.strip()
            zip_code = cols[4].text.strip()
            num_inspections = cols[5].text.strip()
            last_inspection = cols[6].text.strip()
            score = cols[7].text.strip()

            data.append([name, users_rating, type_, address, zip_code, num_inspections, last_inspection, score])

    return data

def main():
    base_url = "http://www.city-data.com/fort-worth-tx-restaurants/index{}.html"
    all_data = []

    for i in range(1, 19):  # Loop through index1 to index18
        url = base_url.format(i)
        data = scrape_data(url)
        all_data.extend(data)

    df = pd.DataFrame(all_data, columns=['Name', 'Users Rating', 'Type', 'Address', 'Zip Code', '# Inspections', 'Last Inspection', 'Score'])  # Convert list of data to pandas DataFrame
    df.to_csv('city_data.csv', index=False)  # Save data to a CSV file

if __name__ == "__main__":
    main()
