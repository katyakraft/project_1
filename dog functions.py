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

def top_10_names():
top_names = merged_df['animal_name'].value_counts().head(10)

# Step 2: Create a bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x=top_names.index, y=top_names.values, palette='Set2')

# Step 3: Add title and labels
plt.title('Top 10 Dog Names in NYC')
plt.xlabel('Dog Names')
plt.ylabel('Number of Dogs')

# Step 4: Rotate x labels for better readability
plt.xticks(rotation=45)

# Step 5: Use tight layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()


def popularity_overtime():

    top_names = ["Bella", "Max", "Charlie", "Luna", "Coco"] 
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

def top_increased_popularity:

    """ Makes a graph showing names that gained the most % of popularity in a specific year """
    # Define the names to exclude
    names_to_exclude = ['name', 'dachshund', 'unknow', 'unknown', 'none', 'unkown'] 
    merged_df_with_birth_year['animal_birthyear'] = merged_df_with_birth_year['animal_birthyear'].astype(int)

    # Step 1: Calculate the total count of each name per year
    name_counts = merged_df_with_birth_year.groupby(['animal_birthyear', 'animal_name']).size().reset_index(name='count')

    # Step 2: Exclude specific names
    name_counts = name_counts[~name_counts['animal_name'].isin(names_to_exclude)]

    # Step 3: Calculate the percentage change
    name_counts['percentage_change'] = name_counts.groupby('animal_name')['count'].pct_change()

    # Step 4: Filter for rows with non-null percentage changes
    name_changes = name_counts[name_counts['percentage_change'].notna()]

    # Step 5: Identify the top 10 increases in popularity
    top_increases = name_changes.sort_values(by='percentage_change', ascending=False).head(10)

    # Step 6: Create a bar graph
    plt.figure(figsize=(12, 6))
    plt.barh(top_increases['animal_name'] + " (" + top_increases['animal_birthyear'].astype(str) + ")", 
         top_increases['percentage_change'] * 100, color='skyblue')
    plt.xlabel('Percentage Increase in Popularity (%)')
    plt.title('Top 10 Most Increased Popularity of Animal Names')
    plt.axvline(0, color='gray', linestyle='--')
    plt.show()


""" --- Gender neutral names  --- """

def gender_natural_names():

    # Group by 'animal_name' and 'animal_gender', count occurrences, drop "Dachshund" as name

    name_gender_counts = merged_df.groupby(['animal_name', 'animal_gender']).size().unstack(fill_value=0)
    name_gender_counts = name_gender_counts.drop('Dachshund', errors='ignore')
    name_gender_counts = name_gender_counts.drop('.', errors='ignore')
    name_gender_counts = name_gender_counts.drop('Shiba', errors='ignore')

    # Calculate the difference between 'F' and 'M' counts
    name_gender_counts['gender_difference'] = name_gender_counts['f'] - name_gender_counts['m']

    # Calculate the total count ('all' column)
    name_gender_counts['all_dogs'] = name_gender_counts['f'] + name_gender_counts['m']

    # Filter for at least 30 dogs with a given name
    name_gender_counts = name_gender_counts[name_gender_counts['all_dogs'] >= 45]


    # Calculate the absolute difference between 'F' and 'M' counts
    name_gender_counts['abs_difference'] = (name_gender_counts['f'] - name_gender_counts['m']).abs()

    # Filter for small difference
    name_gender_counts = name_gender_counts[name_gender_counts['abs_difference'] < 20]

    # Sort by the absolute difference in ascending order to prioritize small differences
    name_gender_counts = name_gender_counts.sort_values(by='all_dogs', ascending=False)

    top_gender_neutral_names = name_gender_counts.head(10)

    top_gender_neutral_names

    #Make the graph
    colors = sns.color_palette('Set2', len(top_increases))
    top_gender_neutral_names[['f', 'm']].plot(kind='bar', figsize=(10, 6), color=colors)
    plt.title('Top 10 Gender-Neutral Dog Names')
    plt.xlabel('Dog Names')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend(title='Gender')
    plt.tight_layout()
    plt.show()

""" --- Colleration name/weight --- """

def name_vs_weight():
    #Exclude Name from names
    merged_df = merged_df[merged_df['animal_name'] != "Name"]
    
    # Get the weight groups (names of the weight groups)
    top_weight_groups = ["2 - 3", "7 - 8", "14 - 27", "23 - 41"]

    # Filter the DataFrame to include only the top weight groups
    top_weight_groups_df = merged_df[merged_df['weight'].isin(top_weight_groups)]

    # Group by weight category and name, then count occurrences
    name_counts_by_weight = top_weight_groups_df.groupby(['weight', 'animal_name']).size().reset_index(name='count')

    # Find the top 5 names for each weight group
    top_names_by_weight = name_counts_by_weight.groupby('weight').apply(lambda x: x.nlargest(5, 'count')).reset_index(drop=True)

    # Create a color mapping for each weight group
    unique_weight_groups = top_names_by_weight['weight'].unique()
    colors = sns.color_palette('Set2', len(unique_weight_groups))  # Get a distinct color for each weight group
    weight_color_mapping = dict(zip(unique_weight_groups, colors))  # Map weight groups to colors

    # Plot the top names for each weight group with consistent colors
    plt.figure(figsize=(14, 8))

    # Loop through weight groups and plot each one with the assigned color
    for weight_group in unique_weight_groups:
        group_data = top_names_by_weight[top_names_by_weight['weight'] == weight_group]
        plt.barh(group_data['animal_name'] + f" ({weight_group})", group_data['count'], color=weight_color_mapping[weight_group],             label=weight_group)

    # Add grid lines for better readability
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    # Add title and labels
    plt.xlabel('Number of Dogs')
    plt.ylabel('Dog Name')
    plt.title('Top 5 Most Popular Dog Names in different Weight Groups')

    #  Improve legend visibility
    plt.legend(title='Weight Group', loc='upper right', bbox_to_anchor=(1.15, 1))

    #Use tight layout for better spacing
    plt.tight_layout()

    # Show the plot
    plt.show()
