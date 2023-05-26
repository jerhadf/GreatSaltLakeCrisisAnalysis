################################################# SETUP ################################################# 

# Import libraries
import spacy
import requests
import pandas as pd
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from openai import OpenAI
import os
from urllib.parse import urlparse
from requests.exceptions import RequestException
import configparser
import json

# config API keys 
config = configparser.ConfigParser()
config.read('config.ini')
openai_key = config['openai']['key']
openai = OpenAI(openai_key) # set up OpenAI API

################################################# SETUP ################################################# 

# SETTING UP DATAFRAME 
# List of example URLs on the GSL water crisis 
responses_file = "links.txt"

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

df = pd.DataFrame(columns=["source", "content", "url", "author_names", 
                           "value_types", "stakeholder_types", "keywords", 
                           "methods", "solutions", "facts"])

# define the keywords to use to search for articles 
keywords = [
    "Great Salt Lake watershed",
    "Utah saline lake desiccation",
    "opinions on Great Salt Lake water use", 
    "solutions to the Great Salt Lake drying crisis", 
    "Aral Sea Syndrome Great Salt Lake",
    "water balance Great Salt Lake",
    "Great Salt Lake climate adaptation",
    "Great Salt Lake ecosystem collapse",
    "Great Salt Lake water withdrawals",
    "Great Salt Lake terminal lake management",
    "Great Salt Lake consumptive water uses",
    "Great Salt Lake water conservation policy",
    "Great Salt Lake wetland restoration",
    "Great Salt Lake water rights allocation",
    "Great Salt Lake lake level projections",
    "Great Salt Lake drying up",
    "Great Salt Lake dessication crisis",
    "Great Salt Lake water management",
    "Utah Valley water saving",
    "Great Salt Lake ecosystem",
    "Great Salt Lake wildlife",
    "Great Salt Lake industry",
    "Great Salt Lake tourism",
    "Great Salt Lake climate change",
    "Great Salt Lake water level",
    "Great Salt Lake salinity",
    "Great Salt Lake dust storms",
    "Great Salt Lake air quality",
    "Great Salt Lake brine shrimp",
    "Great Salt Lake mineral extraction",
    "Great Salt Lake Native American tribes",
    "Great Salt Lake research",
    "Great Salt Lake policy",
    "Great Salt Lake stakeholders"
]

################################################# DATA COLLECTION ################################################# 
# Scraping content from URLs in the .txt file 


# Read URLs from file
links_filepath = "links/links.json"
with open(links_filepath, "r") as file:
    data = json.load(file)

# Function to extract base URL (source) from a URL
def get_source(url):
    return urlparse(url).netloc

# Function to extract author from a BeautifulSoup object
def get_author(soup):
    # Try to find a meta tag with name="author"
    author_tag = soup.find("meta", attrs={"name": "author"})
    if author_tag:
        return author_tag["content"]

    # Try to find a span, p, or div tag with class="author"
    for tag_name in ["span", "p", "div"]:
        author_tag = soup.find(tag_name, class_="author")
        if author_tag:
            return author_tag.get_text(strip=True)

    # Try to find the author in the URL (e.g., "www.example.com/author-name/article-title")
    url_path = urlparse(soup.url).path
    for segment in url_path.split("/"):
        if "author" in segment.lower():
            return segment

    # If all else fails, return "Unknown"
    return "Unknown"

# Scrape content from URLs
for source, urls in data.items():
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception if the response status is not 200 (OK)
        except requests.RequestException as e:
            print(f"Failed to fetch {url} due to error: {e}")
            continue  # Skip to the next URL

        soup = BeautifulSoup(response.text, 'html.parser')

        # Get the author
        author = get_author(soup)

        # Get the content
        content = "\n".join([p.get_text() for p in soup.find_all('p')])

        # Save the content to a .txt file
        filename = f"responses/{source.replace('.', '_')}.txt"
        try:
            with open(filename, "w") as file:
                file.write(content)
        except IOError as e:
            print(f"Failed to write to file {filename} due to error: {e}")
            continue  # Skip to the next URL

        # Add the data to the DataFrame
        try:
            df = df.append({
                "source": source,
                "content": filename,
                "url": url,
                "author_names": author,
                # The rest of the columns will be filled in later
                "value_types": None,
                "stakeholder_types": None,
                "keywords": None,
                "methods": None,
                "solutions": None,
                "facts": None
            }, ignore_index=True)
        except Exception as e:
            print(f"Failed to add data to DataFrame due to error: {e}")

# Save resulting DataFrame to a CSV file
output_filepath = "responses/responses.csv"
df.to_csv(output_filepath, index=False)

# # SCRAPING FROM OTHER SOURCES WITHOUT APIs 
# url = "https://www.example.com" 
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find all paragraph tags and print their text
# for p in soup.find_all('p'):
#     print(p.get_text())
#     # Add the text to the DataFrame
    
# # Function to clean text data
# def clean_text(text):
#     # Remove HTML tags
#     soup = BeautifulSoup(text, "html.parser")
#     text = soup.get_text()
    
#     # Remove stop words
#     # You might want to use a library like NLTK for this
    
#     return text

# # Collect and label data
# for url in urls:
#     # Use the VoxScript.GetWebsiteContent API to get the content of the URL
#     # You'll need to replace "your_voxscript_api_key" with your actual VoxScript API key
#     response = requests.get(f"https://api.voxscript.ai/GetWebsiteContent?api_key=your_voxscript_api_key&websiteURL={url}")
#     content = response.json()["content"]
    
#     # Clean the content
#     content = clean_text(content)
    
#     # Use the OpenAI API to label the content
#     # You'll need to replace "your_openai_api_key" with your actual OpenAI API key
#     response = openai.Completion.create(engine="text-davinci-002", prompt=content, max_tokens=60)
#     labels = response.choices[0].text.strip().split("\n")
    
#     # Add the labeled content to the DataFrame
#     df = df.append({
#         "source": "website",
#         "url": url,
#         "author_names": labels[0],
#         "value_types": labels[1],
#         "stakeholder_types": labels[2],
#         "keywords": labels[3],
#         "methods": labels[4],
#         "solutions": labels[5],
#         "facts": labels[6]
#     }, ignore_index=True)
    

# ################################################# DATA CLEANING ################################################# 
    
    
# ################################################# DATA ANALYSIS ################################################# 

# nlp = spacy.load("en_core_web_sm")
# text = "The Great Salt Lake is drying up due to climate change."
# doc = nlp(text)

# for ent in doc.ents:
#     print(ent.text, ent.label_)

# ################################################# DATA VISUALIZATION ################################################# 

# # Create a word map
# text = " ".join(df["keywords"])
# wordcloud = WordCloud().generate(text)

# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")
# plt.show()

    