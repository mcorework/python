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

### 3. Links
[Web Scraping - beginner - Tinkernut](https://www.youtube.com/watch?v=QhD015WUMxE&t=240s)
[Web Scraping - Corey Schafer](https://www.youtube.com/watch?v=ng2o98k983k&t=1406s)

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

# -----------------------------------------------------------------------------------
# ⚙️ With Simple html
# -----------------------------------------------------------------------------------
with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

#print(soup)
#print(soup.prettify())
#print(soup.prettify())

#match = soup.title.text
match = soup.find('div', class_='footer')

# one article
article =soup.find('div', class_='article')
#print('headline article ----',article.h2.a.text)
#print('article text ----',article.p.text)

# one article
for article in soup.find_all('div', class_='article'):
    print('headline article ----',article.h2.a.text)
    print('article text ----',article.p.text)


# -----------------------------------------------------------------------------------
# ⚙️ Scraping a website
# -----------------------------------------------------------------------------------

#REQUEST WEBPAGE AND STORE IT AS A VARIABLE
page_to_scrape = requests.get("http://quotes.toscrape.com")

#USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'TEXT'
#AND STORE THE LIST AS A VARIABLE
quotes = soup.findAll('span', attrs={'class':'text'})

#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'AUTHOR'
#AND STORE THE LIST AS A VARIABLE
authors = soup.findAll('small', attrs={"class":"author"})

#LOOP THROUGH BOTH LISTS USING THE 'ZIP' FUNCTION
#AND PRINT AND FORMAT THE RESULTS
for quote, author in zip(quotes, authors):
    print(quote.text + "-" + author.text)
