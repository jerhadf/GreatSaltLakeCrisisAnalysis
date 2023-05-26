responses_file = "links.txt"

urls = [
    "https://slco.org/water-conservation/",
    "https://algaeresearchsupply.com/blogs/news/our-interview-with-jaimi-butler-of-the-great-salt-lake-institute",
    "https://www.upr.org/show/lake-effect/2022-06-01/lake-effect-the-science-and-importance-of-great-salt-lake",
    "https://www.visitutah.com/articles/we-are-all-great-salt-lake",
    "https://www.fogsl.org/newsroom/item/963-healing-bear-river-healing-great-salt-lake-a-conversation-with-darren-parry",
    "https://www.cnn.com/2023/02/10/us/utah-great-salt-lake-dust-pollution-weir-wxc/index.html",
    "https://www.washingtonpost.com/climate-environment/2023/01/06/great-salt-lake-utah-drying-up/",
    "https://www.deseret.com/opinion/2022/6/29/23188005/opinion-the-toxic-tale-of-the-great-salt-lake-drought-water-receding-toxic-metals-arsenic-dust-strom",
    "https://pws.byu.edu/GSL%20report%202023",
    "https://www.sltrib.com/news/environment/2022/11/08/great-salt-lakes-ecological/",
    "https://www.upr.org/show/lake-effect/2022-09-15/lake-effect-the-importance-of-great-salt-lakes-brine-shrimp",
    "https://collections.lib.utah.edu/ark:/87278/s65ztg1x",
    "https://collections.lib.utah.edu/search?facet_setname_s=uum_gslohc", 
    "https://www.nytimes.com/2022/06/07/climate/salt-lake-city-climate-disaster.html", 
    "https://www.deseret.com/opinion/2023/5/18/23727766/great-salt-lake-national-park"
]

# Read the existing URLs from the file
links_fp = "data/links.txt"
try:
    with open(links_fp, "r") as file:
        existing_urls = file.read().splitlines()
except FileNotFoundError:
    existing_urls = []

# Combine the existing URLs with the new ones, and remove duplicates
all_urls = list(set(existing_urls + urls))

# Write the URLs back to the file
with open(links_fp, "w") as file:
    for url in all_urls:
        # Ignore lines starting with '#'
        if not url.startswith('#'):
            file.write(url + "\n")
