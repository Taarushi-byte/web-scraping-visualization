import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL
url = "http://quotes.toscrape.com"

# Request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract data
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

data = []

for i in range(len(quotes)):
    data.append({
        "quote": quotes[i].text,
        "author": authors[i].text
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("quotes_data.csv", index=False)

# Count quotes per author
author_counts = df['author'].value_counts()

# Plot graph
plt.figure(figsize=(10,5))
author_counts.plot(kind='bar')

plt.title("Number of Quotes per Author")
plt.xlabel("Author")
plt.ylabel("Count")

# Save image
plt.savefig("quotes_visualization.png")

plt.show()