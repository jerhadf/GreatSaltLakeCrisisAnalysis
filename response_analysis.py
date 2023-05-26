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
    - author_names: A list of the authors involved in creating the response. This could be the username of a Reddit or Twitter user, the name of a YouTube channel, or the author of a news article or report.
    - value_types: A list of the major value types in the response. This represents the main themes or values that the response is promoting or discussing.
    - stakeholder_types: A list of the types of stakeholders in the response. This represents the groups or individuals who have a stake in the Great Salt Lake crisis, as identified in the response.
    - keywords: A list of the top 5 significant non-stop-words used in the response. These are the words that are most relevant to the content of the response, excluding common stop words like 'the', 'and', 'is', etc.
    - methods: A list of the research methods, techniques, or ways of analyzing the problem that are mentioned in the response. This could include scientific research methods, policy analysis techniques, or other methods of understanding and addressing the crisis.
    - solutions: A list of the solutions to the crisis proposed in the response. These are the specific actions or strategies suggested to address the Great Salt Lake crisis.
    - facts: A list of the facts, numbers, results, or takeaways in the response. This includes any specific data or factual information presented in the response, such as the cost of a proposed solution or the amount of water it could save.
"""

responses_df = pd.DataFrame(columns=["source", "content", "url", "author_names",
                           "value_types", "stakeholder_types", "keywords",
                           "methods", "solutions", "facts"])


# ################################################# DATA CLEANING #################################################

# Function to read in all of the responses from the /responses folder into the DataFrame
# Put the response text in the "content" column and the source (folder) in the "source" column
# while reading the responses, clean up the 
 
# Function to clean text data
def clean_text(text):
    # Remove HTML tags
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text()
    
    # Remove stop words
    # You might want to use a library like NLTK for this
    
    return text
    
# ################################################# DATA ANALYSIS ################################################# 

# nlp = spacy.load("en_core_web_sm")
# text = "The Great Salt Lake is drying up due to climate change."
# doc = nlp(text)

# for ent in doc.ents:
#     print(ent.text, ent.label_)

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
