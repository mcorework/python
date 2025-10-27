"""
# 🧵 Threading in Python — Overview

## 📘 Introduction
**Threading** in Python allows you to run multiple parts of your program concurrently.  
Each thread runs in the same memory space, making it efficient for I/O-bound tasks 
(like network requests, file I/O, etc.) but **not ideal for CPU-bound tasks** due to the **Global Interpreter Lock (GIL)**.

---

## ⚙️ Key Concepts

### 1. Thread
A **thread** is a lightweight subprocess — the smallest unit of CPU execution.  
All threads share the same data space, which helps in communication between them.

### 2. Global Interpreter Lock (GIL)
The **GIL** ensures that only one thread executes Python bytecode at a time,  
which means Python threads are not truly parallel for CPU-heavy work.

### 3. When to Use Threads
✅ Ideal for:
- Network operations (API calls, downloads)
- File I/O operations  
❌ Avoid for:
- CPU-bound tasks (use `multiprocessing` instead)

### 3. Links
[Python Threading - Neural Line](https://www.youtube.com/watch?v=A_Z1lgZLSNc)
which means Python threads are not truly parallel for CPU-heavy work.

"""

import concurrent.futures
import threading
import requests
import time


start = time.perf_counter()

threads = []

def do_something(seconds):
    print(f'Sleeping {seconds} second(s) ...')
    time.sleep(seconds)
    print('Done Sleeping')

#1.Using Thread Pool Executor
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

# In Python 3.2, they have added a Python Thread Pool Executor


#do_something()
#do_something()
# finish = time.perf_counter()
# print(f' FInished in {round(finish-start, 2)} second(s)')

#2.Using Thread Pool Executor
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

#3.Download random images asynchronously with various threads
img_urls = [
    'https://unsplash.com/photos/a-boat-on-mountain-lake-9o4U0GBTdu8',
    'https://unsplash.com/photos/airplane-window-clouds-fire-wing-G1rSYvC9QEs',
    'https://unsplash.com/photos/suspension-bridge-hiker-Hf3N5zT1vtY',
    'https://unsplash.com/photos/coastal-road-cliff-turquoise-water-fiftyF'
]

t1 = time.perf_counter()
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

t2 = time.perf_counter()
finish = time.perf_counter()
print(f' FInished in {t2-t1} second(s)')
