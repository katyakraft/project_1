#General settings
import requests
import pandas as pd
from collections import Counter
pd.set_option('display.max_rows', None)
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so
import re

""" ---Functions for data collection--- """

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
                "Breed Name": breed.get("name").lower(),
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
    for characteristics in df_breeds["temperament"]:  
        if isinstance(characteristics, str):
            all_characteristics.extend(characteristics.split(', '))
    
    # Count characteristics
    characteristic_counts = Counter(all_characteristics)
    
    # Convert to DataFrame and shorten
    result_characteristics = pd.DataFrame.from_dict(characteristic_counts, orient='index', columns=['Count'])
    result_characteristics = result_characteristics.sort_values('Count', ascending=False)
    result_characteristics = result_characteristics.head(5)
    
    return result_characteristics

def add_columns(df_breeds, result_characteristics):
    """ This function adds new columns with boolean values of the 5 most popular characteristics """    

    for characteristic in result_characteristics.index:  
        df_breeds[characteristic] = df_breeds['temperament'].str.contains(characteristic, case=False)

    return df_breeds


""" ---Functions for data cleaning--- """
def breed_groups(breedname):
    
    if re.search(r'pit bull|pitbull', breedname):  
        return 'pitbull'
    elif re.search(r'chihuahua', breedname): 
        return 'chihuahua'
    elif re.search(r'poodle', breedname):  
        return 'poodle'
    elif re.search(r'crossbread|crossbreed| mixed| cross breed|mix|cross bread' , breedname):  
        return 'crossbreed'
    elif re.search(r'dachshund|dachs hund' , breedname):  
        return 'dachshund'
    elif re.search(r'labrador' , breedname):  
        return 'labrador'
    elif re.search(r'beagle|beagel' , breedname):  
        return 'beagle'
    elif re.search(r'german shepherd' , breedname):  
        return 'german shepherd'
    elif re.search(r'golden' , breedname):  
        return 'golden retriever'
    elif re.search(r'shih tzu|shihtzu' , breedname):  
        return 'shih tzu'
    elif re.search(r'maltese' , breedname):  
        return 'maltese' 
    elif re.search(r'husky|siberianhusky' , breedname):  
        return 'siberian husky' 
    elif re.search(r'cocker spaniel' , breedname):  
        return 'cocker spaniel' 
    elif re.search(r'boxer' , breedname):  
        return 'boxer' 
    elif re.search(r'rotweiler' , breedname):  
        return 'rotweiler' 
    elif re.search(r'dalmatian' , breedname):  
        return 'dalmatian'
    elif re.search(r'yorkshire terrier' , breedname):  
        return 'yorkshire terrier'
    elif re.search(r'pomeranian' , breedname):  
        return 'pomeranian'
    elif re.search(r'havanese' , breedname):  
        return 'havanese'
    elif re.search(r'french bulldog' , breedname):  
        return 'french bulldog'
    elif re.search(r'jack russell terrier' , breedname):  
        return 'jack russell terrier'
    elif re.search(r'cavalier king charles spaniel' , breedname):  
        return 'cavalier king charles spaniel'
    elif re.search(r'shiba inu|shibainu' , breedname):  
        return 'shiba inu'
    elif re.search(r'not provided|unknown' , breedname):  
        return 'unknown'    
    elif re.search(r'pug|pugg' , breedname):  
        return 'pug'
    elif re.search(r'australian shepherd' , breedname):  
        return 'australian shepherd'
    elif re.search(r'boston terrier|bostonterrier|boston' , breedname):  
        return 'boston terrier'
    elif re.search(r'labradoodle' , breedname):  
        return 'labradoodle'
    elif re.search(r'bichon frise|bichon' , breedname):  
        return 'bichon frise'
    elif re.search(r'morkiamerican staffordshire terrier|morkie' , breedname):  
        return 'morkie'
    elif re.search(r'maltipoo' , breedname):  
        return 'maltipoo'
    elif re.search(r'miniature schnauzer|schnauzer, miniature|schnauzer miniature' , breedname):  
        return 'miniature schnauzer'
    elif re.search(r'miniature pinscher' , breedname):  
        return 'miniature pinscher'
    elif re.search(r'puggle' , breedname):  
        return 'puggle' 
    elif re.search(r'lhasa apso' , breedname):  
        return 'lhasa apso'
    elif re.search(r'pekingese' , breedname):  
        return 'pekingese'
    elif re.search(r'cockapoo ' , breedname):  
        return 'cockapoo '
    elif re.search(r'cairn terrier|cairn' , breedname):  
        return 'cairn terrier'
    elif re.search(r'border collie' , breedname):  
        return 'border collie'
    elif re.search(r'corgi' , breedname):  
        return 'pembroke welsh corgi'
    elif re.search(r'australian cattledog' , breedname):  
        return 'australian cattledog'
    elif re.search(r'jindo dog|jindo' , breedname):  
        return 'jindo dog'
    elif re.search(r'papillon' , breedname):  
        return 'papillon'
    elif re.search(r'wheaton terrier' , breedname):  
        return 'wheaton terrier'
    elif re.search(r'bernese' , breedname):  
        return 'bernese'
    elif re.search(r'chow chow|chowchow' , breedname):  
        return 'chow chow'
    else:
       pass 
        
""" --- Name popularity over time --- """

def popularity_overtime()

    top_names = ["bella", "max", "charlie", "luna", "coco"]
    #remove invalid birth years 
    merged_df['animal_birthyear'] = pd.to_numeric(merged_df['animal_birthyear'], errors='coerce')
    #create a copy with valid birth years
    only_with_birthyear_df = merged_df.dropna(subset=['animal_birthyear'])
    only_with_birthyear_df['animal_birthyear'] = pd.to_numeric(only_with_birthyear_df['animal_birthyear'].astype(int), errors='coerce')

    # Normalize: group by year and stack to use name as index
    result = only_with_birthyear_df[only_with_birthyear_df['animal_name'].isin(top_names)].groupby(['animal_name', 'animal_birthyear'])['animal_name'].count().unstack(fill_value=0)
    # Filter the DataFrame for years from 2000
    filtered_df = only_with_birthyear_df[only_with_birthyear_df['animal_birthyear'] >= 2000]

    # Calculate total dogs registered per year for the filtered DataFrame
    total_dogs_per_year = filtered_df.groupby('animal_birthyear')['animal_name'].count()


    # Normalize the result DataFrame by the total number of dogs per year

    normalized_result = (result / total_dogs_per_year) * 1000
    
    # Plot the normalized data
    normalized_result.T.plot(figsize=(15, 8))
    plt.title('Normalized Popularity of Animal Names Over Time (2000-2022)')
    plt.xlabel('Year of Birth')
    plt.ylabel('Normalized Count of Names (Relative to Total Dogs Registered)')
    plt.xlim(2000, 2022)  # Keep the x-axis range the same
    plt.ylim(0, 20)  # Set the y-axis limits

    # Adjust the range 
    plt.xticks(range(2000, 2022))  

    plt.legend(title='Animal Names', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

