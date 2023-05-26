################################################# SETUP #################################################

# Import libraries
import spacy
import requests
import pandas as pd
from bs4 import BeautifulSoup
import PyPDF2
from io import BytesIO
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import openai
import os
from urllib.parse import urlparse
from requests.exceptions import RequestException
import configparser
import json

# config API keys
config = configparser.ConfigParser()
config.read('config.ini')
openai_key = config['openai']['key']
openai.api_key = openai_key

# Initialize an empty DataFrame to store the data
"""
DataFrame Columns:
    - source: The origin of the response as a name/type (e.g., 'website', 'youtube', 'reddit', etc.).
    - content: The filepath to the text content of the response. This is the main body of the response.
    - url: The URL or source link of the original response. This provides a reference to the original content.
    - stakeholder_type: The type of stakeholders in the response. This represents the groups or individuals who have a stake in the Great Salt Lake crisis, as identified in the response.
    - values A list of the major value types in the response. This represents the main themes or values that the response is promoting or discussing.
    - keywords: A list of the top 5 significant non-stop-words used in the response. These are the words that are most relevant to the content of the response, excluding common stop words like 'the', 'and', 'is', etc.
    - methods: A list of the research methods, techniques, or ways of analyzing the problem that are mentioned in the response. This could include scientific research methods, policy analysis techniques, or other methods of understanding and addressing the crisis.
    - solutions: A list of the solutions to the crisis proposed in the response. These are the specific actions or strategies suggested to address the Great Salt Lake crisis.
    - facts: A list of the facts, numbers, results, or takeaways in the response. This includes any specific data or factual information presented in the response, such as the cost of a proposed solution or the amount of water it could save.
"""

responses_df = pd.DataFrame(columns=["source", "content", "url", "author_names",
                           "value_types", "stakeholder_types", "keywords",
                           "methods", "solutions", "facts"])

# make dictionary for matching stakeholders to stakeholder_types
stakeholder_mapping = {
    "Academic_Researchers_on_Great_Salt_Lake": "academics",
    "Agricultural_Sector_in_Utah": "agriculture",
    "Air_Quality_Management_Agencies_in_Utah": "government",
    "Brine_Shrimp_Harvesters": "industry",
    "Environmental_Activists_in_Utah": "environmentalists",
    "Federal_Environmental_Agencies_(e.g.,_EPA)": "government",
    "Fishing_Industry_in_Utah": "industry",
    "Friends_of_Great_Salt_Lake": "environmentalists",
    "Great_Salt_Lake_Advisory_Council": "government",
    "Great_Salt_Lake_Audubon": "environmentalists",
    "Great_Salt_Lake_Institute": "academics",
    "Local_Businesses_in_Salt_Lake_City": "industry",
    "Local_Media_Outlets_in_Salt_Lake_City": "media",
    "Mineral_Extraction_Industry": "industry",
    "Native_American_Tribes_with_Ties_to_Great_Salt_Lake": "native_american_tribes",
    "Outdoor_Recreation_Enthusiasts_in_Utah": "recreation",
    "Public_Health_Officials_in_Utah": "health",
    "Real_Estate_Developers_in_Salt_Lake_City": "industry",
    "Salt_Lake_City_Residents": "residents",
    "Tourism_Industry_in_Utah": "industry",
    "Utah_Department_of_Environmental_Quality": "government",
    "Utah_Department_of_Natural_Resources": "government",
    "Utah_Department_of_Transportation": "government",
    "Utah_Division_of_Water_Resources": "government",
    "Utah_Geological_Survey": "government",
    "Utah_Religious_Communities": "religious_communities",
    "Utah_State_Legislators": "government",
    "Wildlife_Conservation_Organizations_in_Utah": "environmentalists",
    "Young_people_and_youth_groups_in_Utah": "youth"
}

# ################################################# AI RESPONSES #################################################

# Define the directory
directory = 'responses/AI/'

# Initialize an empty DataFrame
df = pd.DataFrame()

# Initialize an empty DataFrame with the desired columns
df = pd.DataFrame(columns=["source", "filepath", "content", "stakeholder_type", "values", "keywords", "methods", "solutions", "facts"])

# Directory containing the AI-generated responses
directory = "responses/AI/"

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        # Construct the full file path
        filepath = os.path.join(directory, filename)
        
        # Read the content of the file
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Split the content into question-answer pairs
        qa_pairs = content.split("# ")[1:]  # Skip the first split result, as it will be empty due to the leading "# "
        qa_dict = {}
        for qa_pair in qa_pairs:
            question, answer = qa_pair.split("\n", 1)  # Split on the first newline to separate the question from the answer
            qa_dict[question] = answer.strip()  # Remove leading/trailing whitespace from the answer
        
        # Extract the stakeholder type from the filename
        stakeholder_type = filename.split("_response.txt")[0].replace('"', '')
        stakeholder_type = stakeholder_mapping.get(stakeholder_type, stakeholder_type)  # Use the mapping if available, otherwise use the original type
        
        # Add a new row to the DataFrame with the 'source' and 'filepath' attributes
        df = df.append({
            "source": "AI",
            "filepath": filepath,
            "content": qa_dict,
            "stakeholder_type": stakeholder_type,
            "values": [],
            "keywords": [],
            "methods": [],
            "solutions": [],
            "facts": []
        }, ignore_index=True)

# Print the DataFrame to check the result

# ################################################# DATA ANALYSIS ################################################# 

# Define value types
value_types = ["personal_finance", "sense_of_place", "aesthetics", "health_safety",
               "government_finance", "autonomy", "social_cohesion", "economic_growth", "environmental_protection", 
               "place_attachment", "loss_material_or_emotional", "other"] 

# Initialize a list to store the value types for each response
df["value_types"] = [[] for _ in range(len(df))]

# For each response, classify the content into value types
for i, row in df.iterrows():
    for question_answer in row["content"]:
        # Generate a prompt to classify the content
        prompt = f"Given the following statement, identify the main value types: {question_answer['answer']}"
        
        # Use OpenAI to classify the content
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=60
        )

        # Parse the model's response to extract the identified value types
        identified_value_types = [value_type for value_type in value_types if value_type in response.choices[0].text.strip().lower()]
        
        # Add the identified value types to the dataframe
        df.at[i, "value_types"].extend(identified_value_types)



# ################################################# AI STUFF ################################################# 

# response = openai.Completion.create(
#   engine="text-davinci-002",
#   prompt="Translate the following English text to French: '{}'",
#   max_tokens=60
# )

# ################################################# DATA VISUALIZATION ################################################# 

# # Create a word map
# text = " ".join(df["keywords"])
# wordcloud = WordCloud().generate(text)

# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()
