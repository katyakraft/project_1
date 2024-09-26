NYC Dog Names & Breed Analysis Project

Overview

This project analyzes dog name trends in NYC based on available datasets and integrates additional breed data from an external API. The goal is to explore and understand the factors behind naming trends, popularity of specific dog names over time, and whether a dog's name is related to its breed or even behavior.
Through this analysis, we aim to identify the most popular dog names by breed, observe naming patterns over the years, and explore whether certain names are associated with specific characteristics of dogs.

Datasets
1. NYC Dog Names Dataset
The NYC dataset contains records of registered dog names, including:

-Dog name
-Breed group
-Year of registration
-Other information such as gender, zip code, etc.

2. The Dog API
The Dog API was used to retrieve additional breed-related data, including breed temperament, weight, and other characteristics that could help us understand trends and relationships between dog names and breed behavior.

Goals & Objectives
The main objectives of this analysis were:
1.Dog Name Popularity: Identify the most popular names given to dogs across different breeds and observe how popularity changes over the years.
2.Breed-Specific Name Trends: Explore if certain dog breeds have specific names commonly associated with them.
3.Yearly Trends: Analyze if trends in dog names correlate with certain events, pop culture, or global trends in the year they were registered.
4.Name-Based Dog Characteristics: Investigate if there are any relationships between a dog’s name and its breed's characteristics, such as temperament or behavior.

Key Features of the Project

Data Cleaning and Preparation:
-Cleaning and Formatting: Handling missing values, inconsistent data formats, and eliminating non-informative or incorrect names like "Unknown" and single-character names.
-Data Enrichment: Fetching additional breed information using the Dog API to supplement the NYC dataset with detailed breed attributes.

Analysis & Visualizations:
1.Most Popular Dog Names:

  -Visualize the top names overall and by breed group.
  -Display yearly trends to see how name popularity has evolved over time.
2.Top Names by Breed:

  -Analyze the top 3 names given to dogs in the top 5 most popular breeds.
3.Correlation between Names & Characteristics:

  -Using the Dog API's breed characteristics (e.g., temperament), we explore potential links between a dog’s name and its expected behavior.

4.Longest & Shortest Dog Names:

  -Determine the longest and shortest names in the dataset and analyze their usage.

Challenges:
-Combining datasets with different structures and resolving inconsistencies.
-Handling missing or incomplete breed data when integrating with the Dog API.

Tools & Libraries Used
-Pandas: For data manipulation and analysis.
-Matplotlib & Seaborn: For creating visualizations to present trends and patterns.
-Requests: For accessing the Dog API and fetching breed data.
-Jupyter Notebooks: To interactively develop and present the analysis.

Contributing Contributions are welcome! Feel free to fork the repository and submit a pull request if you'd like to make improvements or fix issues.
