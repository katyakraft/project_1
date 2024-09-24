#General settings
import requests
import pandas as pd
from collections import Counter
pd.set_option('display.max_rows', None)

""" Functions for data collection"""

def get_breed_data():
""" This function calls the DogAPI and retrieves characteristics of each breed: name, life span, temperament, breed group, weight, height, bred for and origin"""
    # Initialize an empty list to store breed data
    breed_list = []

    # Fetch the list of breeds from the API
    url = "https://api.thedogapi.com/v1/breeds"
    headers = {"x-api-key": "live_bbCrlls8Jw8I19PRwoKOY8c78YaFNHN60TaHSumPkzBWitHe3R3QTqIVteDxLAWs"}
    
    # Make the request to get all breeds
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        breeds = response.json()  # Get the list of all breeds

        # Loop through the breeds and extract relevant data
        for breed in breeds:
            breed_data = {
                "Breed Name": breed.get("name"),
                "Life Span": breed.get("life_span"),
                "Temperament": breed.get("temperament"),
                "Breed Group": breed.get("breed_group"),
                "Weight": breed.get("weight", {}).get("metric"),
                "Height": breed.get("height", {}).get("metric"),
                "Bred For": breed.get('bred_for'),
                "Origin": breed.get("origin")
            }
            breed_list.append(breed_data)

        # Convert the list of dictionaries into a DataFrame
        df_breeds = pd.DataFrame(breed_list)
        return df_breeds


def count_characteristics(df_breeds):
""" This function picks the 5 most popular characteristics of dog breeds """    
    # Combine all characteristics into a single list
    all_characteristics = []
    for characteristics in df_breeds["Temperament"]:  
        if isinstance(characteristics, str):
            all_characteristics.extend(characteristics.split(', '))
    
    # Count occurrences
    characteristic_counts = Counter(all_characteristics)
    
    # Convert to DataFrame for easy viewing
    result_df = pd.DataFrame.from_dict(characteristic_counts, orient='index', columns=['Count'])
    result_df = result_df.sort_values('Count', ascending=False)
    
    return result_df

def add_columns(df_breeds):
""" This function adds new columns with boolean values of the 5 most popular characteristics """    

    for characteristic in result_characteristics:
        df_breeds['characteristic'] = df_breeds['Temperament'].str.contains("characteristic")

    return df_breeds

