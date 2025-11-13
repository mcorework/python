"""
# 🌐 Network Automation with Python — Overview

## 📘 Introduction
**Network Automation** is the process of using **software and scripts** to configure, manage, test, and operate network devices automatically.  
Instead of manually logging into routers or switches, you can use **Python** to automate these tasks—saving time, reducing errors, and improving scalability.

Python is widely used for network automation due to:
- Its **readability and simplicity**
- Availability of **powerful libraries** (like `paramiko`, `netmiko`, `napalm`, and `pyntc`)
- Support for **API-based network management** (e.g., RESTCONF, NETCONF, and SNMP)

---

### 3. Links
[Web Scraping - beginner - Tinkernut](https://www.youtube.com/watch?v=QhD015WUMxE&t=240s)
[Web Scraping - Corey Schafer](https://www.youtube.com/watch?v=ng2o98k983k&t=1406s)

"""

import webbrowser
import sys
import urllib.parse
import subprocess
import socket
import requests


# -----------------------------------------------------------------------------------
# ⚙️ 1. Get your IP address (Local + Public)
# -----------------------------------------------------------------------------------

# Local IP
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(f"💻 Local IP Address: {local_ip}")

# Public IP
public_ip = requests.get('https://api.ipify.org').text
print(f"🌐 Public IP Address: {public_ip}")


# -----------------------------------------------------------------------------------
# ⚙️ 2. Simple Port Scanner (Localhost)
# -----------------------------------------------------------------------------------

import socket

target = '127.0.0.1'   # Localhost
ports_to_check = [22, 80, 443, 3306]

print(f"🔍 Scanning {target}...")
for port in ports_to_check:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"✅ Port {port} is open")
    else:
        print(f"❌ Port {port} is closed")
    s.close()

# -----------------------------------------------------------------------------------
# ⚙️ 3. Ping Multiple Hosts
# -----------------------------------------------------------------------------------

import os

hosts = ['google.com', 'github.com', 'openai.com']

for host in hosts:
    print(f"\n🌐 Pinging {host}...")
    response = os.system(f"ping -c 2 {host}")
    if response == 0:
        print(f"✅ {host} is reachable")
    else:
        print(f"❌ {host} is not reachable")
# -----------------------------------------------------------------------------------
# ⚙️ 4. Simple HTTP GET Request
# -----------------------------------------------------------------------------------

import requests

url = "https://api.github.com"
response = requests.get(url)

print(f"🌐 Status Code: {response.status_code}")
print(f"📦 Response Headers: {response.headers['content-type']}")
print(f"📝 Data: {response.text[:200]}...")  # print first 200 chars

# -----------------------------------------------------------------------------------
# ⚙️ 5. Google Search
# -----------------------------------------------------------------------------------

# ✅ List of valid sites (optional — not used in basic search)
valid_websites = [
    'reddit.com',
    'stackoverflow.com',
    'stackexchange.com',
    'medium.com'
]

# ✅ Chrome path for macOS
chrome_path = "open -a /Applications/Google\ Chrome.app %s"

# ✅ Register Chrome as the browser
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def create_query():
    """Create a search query string from command-line arguments."""
    if len(sys.argv) < 2:
        print("⚠️ Usage: python3 search.py <search terms>")
        sys.exit(1)
    query = ' '.join(sys.argv[1:])
    return query

def search_google(query):
    """Open Google Chrome with a search for the given query."""
    encoded_query = urllib.parse.quote(query)
    search_url = f"https://www.google.com/search?q={encoded_query}"

    # ✅ Open in Chrome using macOS 'open' command
    subprocess.run(["open", "-a", "Google Chrome", search_url])
    print(f"🔍 Searching for: {query}")

if __name__ == "__main__":
    q = create_query()
    search_google(q)

