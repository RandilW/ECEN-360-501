import pandas as pd
import json

metadata = {
    "release": {
        "id": "acs2022_5yr",
        "name": "ACS 2022 5-year",
        "years": "2018-2022"
    },
    "tables": {
        "B08006": {
            "columns": {
                "B08006001": {
                    "indent": 0,
                    "name": "Total:"
                },
                "B08006002": {
                    "indent": 1,
                    "name": "Car, truck, or van:"
                },
                "B08006003": {
                    "indent": 2,
                    "name": "Drove alone"
                },
                "B08006004": {
                    "indent": 2,
                    "name": "Carpooled:"
                },
                "B08006005": {
                    "indent": 3,
                    "name": "In 2-person carpool"
                },
                "B08006006": {
                    "indent": 3,
                    "name": "In 3-person carpool"
                },
                "B08006007": {
                    "indent": 3,
                    "name": "In 4-or-more-person carpool"
                },
                "B08006008": {
                    "indent": 1,
                    "name": "Public transportation (excluding taxicab):"
                },
                "B08006009": {
                    "indent": 2,
                    "name": "Bus"
                },
                "B08006010": {
                    "indent": 2,
                    "name": "Subway or elevated rail"
                },
                "B08006011": {
                    "indent": 2,
                    "name": "Long-distance train or commuter rail"
                },
                "B08006012": {
                    "indent": 2,
                    "name": "Light rail, streetcar or trolley (carro p\u00fablico in Puerto Rico)"
                },
                "B08006013": {
                    "indent": 2,
                    "name": "Ferryboat"
                },
                "B08006014": {
                    "indent": 1,
                    "name": "Bicycle"
                },
                "B08006015": {
                    "indent": 1,
                    "name": "Walked"
                },
                "B08006016": {
                    "indent": 1,
                    "name": "Taxicab, motorcycle, or other means"
                },
                "B08006017": {
                    "indent": 1,
                    "name": "Worked from home"
                },
                "B08006018": {
                    "indent": 1,
                    "name": "Male:"
                },
                "B08006019": {
                    "indent": 2,
                    "name": "Car, truck, or van:"
                },
                "B08006020": {
                    "indent": 3,
                    "name": "Drove alone"
                },
                "B08006021": {
                    "indent": 3,
                    "name": "Carpooled:"
                },
                "B08006022": {
                    "indent": 4,
                    "name": "In 2-person carpool"
                },
                "B08006023": {
                    "indent": 4,
                    "name": "In 3-person carpool"
                },
                "B08006024": {
                    "indent": 4,
                    "name": "In 4-or-more-person carpool"
                },
                "B08006025": {
                    "indent": 2,
                    "name": "Public transportation (excluding taxicab):"
                },
                "B08006026": {
                    "indent": 3,
                    "name": "Bus"
                },
                "B08006027": {
                    "indent": 3,
                    "name": "Subway or elevated rail"
                },
                "B08006028": {
                    "indent": 3,
                    "name": "Long-distance train or commuter rail"
                },
                "B08006029": {
                    "indent": 3,
                    "name": "Light rail, streetcar or trolley (carro p\u00fablico in Puerto Rico)"
                },
                "B08006030": {
                    "indent": 3,
                    "name": "Ferryboat"
                },
                "B08006031": {
                    "indent": 2,
                    "name": "Bicycle"
                },
                "B08006032": {
                    "indent": 2,
                    "name": "Walked"
                },
                "B08006033": {
                    "indent": 2,
                    "name": "Taxicab, motorcycle, or other means"
                },
                "B08006034": {
                    "indent": 2,
                    "name": "Worked from home"
                },
                "B08006035": {
                    "indent": 1,
                    "name": "Female:"
                },
                "B08006036": {
                    "indent": 2,
                    "name": "Car, truck, or van:"
                },
                "B08006037": {
                    "indent": 3,
                    "name": "Drove alone"
                },
                "B08006038": {
                    "indent": 3,
                    "name": "Carpooled:"
                },
                "B08006039": {
                    "indent": 4,
                    "name": "In 2-person carpool"
                },
                "B08006040": {
                    "indent": 4,
                    "name": "In 3-person carpool"
                },
                "B08006041": {
                    "indent": 4,
                    "name": "In 4-or-more-person carpool"
                },
                "B08006042": {
                    "indent": 2,
                    "name": "Public transportation (excluding taxicab):"
                },
                "B08006043": {
                    "indent": 3,
                    "name": "Bus"
                },
                "B08006044": {
                    "indent": 3,
                    "name": "Subway or elevated rail"
                },
                "B08006045": {
                    "indent": 3,
                    "name": "Long-distance train or commuter rail"
                },
                "B08006046": {
                    "indent": 3,
                    "name": "Light rail, streetcar or trolley (carro p\u00fablico in Puerto Rico)"
                },
                "B08006047": {
                    "indent": 3,
                    "name": "Ferryboat"
                },
                "B08006048": {
                    "indent": 2,
                    "name": "Bicycle"
                },
                "B08006049": {
                    "indent": 2,
                    "name": "Walked"
                },
                "B08006050": {
                    "indent": 2,
                    "name": "Taxicab, motorcycle, or other means"
                },
                "B08006051": {
                    "indent": 2,
                    "name": "Worked from home"
                }
            },
            "denominator_column_id": "B08006001",
            "title": "Sex of Workers by Means of Transportation to Work",
            "universe": "Workers 16 years and over"
        }
    }
}

# Read the data from a CSV file
df = pd.read_csv('acs2022_5yr_B08006_86000US76431.csv')

# Use the metadata to rename the columns
new_column_names = {col: metadata['tables']['B08006']['columns'][col]['name'] for col in df.columns if col in metadata['tables']['B08006']['columns']}
df.rename(columns=new_column_names, inplace=True)

# List of Fort Worth ZIP codes
fort_worth_zips = ['76101', '76102', '76103', '76104', '76105', '76106', '76107', '76108', '76109', '76110',
                       '76111', '76112', '76113', '76114', '76115', '76116', '76118', '76119', '76120', '76121',
                       '76122', '76123', '76124', '76126', '76129', '76130', '76131', '76132', '76133', '76134',
                       '76135', '76136', '76137', '76140', '76147', '76148', '76150', '76155', '76161', '76162',
                       '76163', '76164', '76177', '76178', '76179', '76181', '76185', '76191', '76192', '76193',
                       '76195', '76196', '76197', '76198', '76199', '76039', '76036', '76248', '76127', '76053',
                       '76117', '76244', '76012', '76180', '76182', '76013']

# Filter the DataFrame to include only the rows with ZIP codes in Fort Worth
df = df[df['name'].isin(fort_worth_zips)]

# Save the DataFrame to a CSV file
df.to_csv('means_of_transportation.csv', index=False)
