"""
# 🌐 Web Scraping in Python — Overview

## 📘 Introduction
**Web scraping** is the process of **extracting data from websites** automatically using code, 
instead of manually copying and pasting.  
It’s commonly used for:
- Data collection for research or analysis  
- Price monitoring and market research  
- Job listings, product reviews, or social media data aggregation  

Python provides several libraries to make web scraping **efficient, structured, and reliable**.

---

## ⚙️ Why It’s Important
- **Automation**: Saves time and effort when collecting large-scale data.  
- **Integration**: Helps integrate web data into applications, dashboards, or datasets.  
- **Analysis**: Enables real-time insights from websites that don’t provide APIs.  

---

## 🧰 Common Libraries

| Library | Description | Use Case |
|----------|--------------|----------|
| `requests` | Sends HTTP requests to fetch web pages | Basic page access |
| `BeautifulSoup` | Parses HTML and XML documents | Extracts structured data from HTML |
| `lxml` | High-performance HTML/XML parser | Large or complex documents |
| `selenium` | Automates browsers | Handles JavaScript-heavy sites |
| `pandas` | Converts HTML tables or lists into DataFrames | Data analysis-ready format |

---

## ⚠️ Best Practices
- Always **check a website’s Terms of Service** and **robots.txt** before scraping.  
- Add **delays or random sleep** to avoid overloading servers.  
- Use **headers and user-agents** to simulate a real browser.  
- Prefer **APIs** if available (more stable and ethical).  
- Store scraped data responsibly (avoid sensitive or personal data).  

---

## 💻 Example 1 — Basic Scraping with `requests` + `BeautifulSoup`

```python
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://quotes.toscrape.com/"

# Send an HTTP GET request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract all quotes
quotes = soup.find_all("span", class_="text")

print("Quotes from the website:")
for quote in quotes:
    print("-", quote.text)
"""


from bs4 import BeautifulSoup
import requests
import csv

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

#print(soup)
#print(soup.prettify())
print(soup.prettify())
#match = soup.title.text
match = soup.find('div', class_='footer')
print(match)

source = requests.get('http://cnn.com').text

soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())
match = soup.title.text
#print(match)

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
