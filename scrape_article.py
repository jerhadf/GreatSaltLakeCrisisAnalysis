# Import requests, BeautifulSoup and os libraries
import requests
from bs4 import BeautifulSoup
import os

# Define the url to scrape
url = "https://greenly.earth/en-gb/blog/ecology-news/what-is-the-problem-with-the-great-salt-lake-drying-up"

# Send a GET request to the url and store the response
response = requests.get(url)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Parse the response content using BeautifulSoup and html.parser
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the title of the article using the h1 tag
    title = soup.find("h1").text

    # Find the author of the article using the span tag with class "author"
    author = soup.find("span", class_="author").text

    # Find the date of the article using the span tag with class "date"
    date = soup.find("span", class_="date").text

    # Find the main content of the article using the div tag with class "content"
    content = soup.find("div", class_="content")

    # Extract all the text from the content using get_text method
    text = content.get_text()

    # Define the file name using the title and replace any spaces with underscores
    file_name = title.replace(" ", "_") + ".txt"

    # Define the file path using the current working directory and the file name
    file_path = os.path.join(os.getcwd(), file_name)

    # Open the file in write mode and write the title, author, date and text of the article
    with open(file_path, "w") as f:
        f.write(f"Title: {title}\n")
        f.write(f"Author: {author}\n")
        f.write(f"Date: {date}\n")
        f.write(f"Text: {text}\n")

    # Print a success message with the file path
    print(f"Successfully saved {url} to {file_path}")

else:
    # Print an error message if the response status code is not 200
    print(f"Error: Unable to scrape {url}. Status code: {response.status_code}")
