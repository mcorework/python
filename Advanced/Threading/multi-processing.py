"""
# 🧵 Threading in Python — Overview

## 📘 Introduction
**Threading** in Python allows you to run multiple parts of your program concurrently.  
Each thread runs in the same memory space, making it efficient for I/O-bound tasks 
(like network requests, file I/O, etc.) but **not ideal for CPU-bound tasks** due to the **Global Interpreter Lock (GIL)**.

### 🧩 Topics Covered
1. What are threads
2. When to use threads? (I/O vs CPU, GIL Issue)
3. Thread without join()
4. Thread with join()
5. Thread with input arguments
6. Multithreading
7. Daemon Threads
8. Thread with Lock Synchronization
9. Thread Queue (communication between threads)
10. Thread Pool Executor
11. Thread Events
12. Speed Comparison for I/O Task

### 🔗 References
- [Kevin Wood - Computer Vision](https://www.youtube.com/watch?v=Rm9Pic2rpAQ/)
- [Kevin Wood - Multi Threading](https://www.youtube.com/watch?v=IEEhzQoKtQU&t=2009s)

### 🧠 Notes
1. Python threads are not truly parallel for CPU-bound tasks due to the **GIL**.  
   Use the `multiprocessing` module for CPU-intensive operations.  
2. Threads are excellent for **I/O-bound tasks** (network requests, file I/O, etc.)  
   where the program spends time waiting for external operations.
"""

# ===============================================================
# 📦 Imports
# ===============================================================
from multiprocessing import Process
import concurrent.futures
import threading
import requests
import time
import queue

# ===============================================================
# 🧵 1. Basic Thread Example — Without join()
# ===============================================================
def print_message():
    """Prints a simple message from a thread."""
    for i in range(5):
        print("Hello from the thread!")
        time.sleep(1)


# ===============================================================
# 🧵 2. Thread with Arguments & join()
# ===============================================================
def print_numbers(name: str, count: int):
    """
    Prints numbers from a thread with a given name and count.

    Args:
        name (str): Name of the thread
        count (int): How many times to print
    """
    for i in range(count):
        print(f'Thread Name: {name} says: {i}')
        time.sleep(0.5)


def main_threading():
    """Creates a single thread, starts it, and waits for it to finish."""
    thread = threading.Thread(target=print_numbers, args=["Thread", 5])
    thread.start()
    thread.join()  # Waits for thread to complete
    print("Main thread finished.")


# ===============================================================
# ⚙️ 3. Multiple Threads (Multithreading)
# ===============================================================
def main_multithreading():
    """Demonstrates running multiple threads concurrently."""
    threads = []
    for i in range(3):
        thread = threading.Thread(target=print_numbers, args=[f"Thread-{i+1}", 3])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print("Main thread finished.")


# ===============================================================
# 🕒 4. Daemon Threads (auto-stop with main thread)
# ===============================================================
def infinite_task():
    """Runs indefinitely to simulate a background process."""
    while True:
        print("Running...")
        time.sleep(1)


def main_daemon():
    """Starts a daemon thread that ends when the main thread ends."""
    daemon_thread = threading.Thread(target=infinite_task)
    daemon_thread.daemon = True
    daemon_thread.start()
    time.sleep(3)
    print("Main thread finished...")


# ===============================================================
# 🔒 5. Thread Synchronization using Locks
# ===============================================================
counter = 0
counter_lock = threading.Lock()


def increment():
    """Safely increments a shared counter using a thread lock."""
    global counter
    with counter_lock:
        for _ in range(100000):
            counter += 1


def main_sync_lock():
    """Runs multiple threads that safely update a shared counter."""
    global counter
    threads = []
    for i in range(3):
        thread = threading.Thread(target=increment)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print("Final Counter Value:", counter)
    print("Main thread finished.")


# ===============================================================
# 📦 6. Thread Communication using Queue
# ===============================================================
def producer(queue):
    """Produces items and places them in the queue."""
    for i in range(5):
        item = f"item-{i}"
        print(f"Producing {item}")
        queue.put(item)
        time.sleep(1)
    queue.put(None)  # Signal to consumer that production is done


def consumer(queue):
    """Consumes items from the queue until None is received."""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consuming {item}")
        time.sleep(2)
    queue.put(None)


def main_queue():
    """Demonstrates producer-consumer communication via Queue."""
    q = queue.Queue()
    producer_thread = threading.Thread(target=producer, args=(q,))
    consumer_thread = threading.Thread(target=consumer, args=(q,))
    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    consumer_thread.join()


# ===============================================================
# ⚡ 7. ThreadPoolExecutor Example
# ===============================================================
def task(n: int):
    """Simulates a time-consuming task."""
    print(f"Task {n} handled by {threading.current_thread().name}")
    time.sleep(n)
    return n * n


def main_thread_pool_executor():
    """Executes multiple tasks using ThreadPoolExecutor."""
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(task, range(1, 6))
    print("Results:", list(results))
    print("Main Thread finished.")


# ===============================================================
# 🚦 8. Thread Events (Controlled Start)
# ===============================================================
def worker(event):
    """Waits for an event signal before starting work."""
    print("Worker waiting for event to start.")
    event.wait()
    print("Worker starting to work...")
    for _ in range(5):
        print("Working...")
        time.sleep(1)
    print("Worker finished.")


def main_event():
    """Triggers a thread to start after a delay using an Event."""
    event = threading.Event()
    thread = threading.Thread(target=worker, args=(event,))
    thread.start()
    time.sleep(3)
    print("Main thread sets the event.")
    event.set()  # Start the worker thread
    thread.join()
    print("Main thread finished.")


# ===============================================================
# 🌐 9. Speed Comparison (Sequential vs Threaded I/O)
# ===============================================================
def fetch_url(url: str):
    """Fetches a URL and prints its byte length."""
    response = requests.get(url)
    print(f"Fetched {url}: {len(response.content)} bytes")


def main_fetch_url():
    """Compares sequential vs threaded URL fetching performance."""
    urls = [
        "https://bostondynamics.com/",
        "https://agilityrobotics.com/",
        "https://huggingface.co/",
        "https://python.org/",
    ]

    # Sequential fetch
    start_time = time.time()
    for url in urls:
        fetch_url(url)
    print("⏱️ Time (sequential):", time.time() - start_time)

    # Threaded fetch
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("⚡ Time (threaded):", time.time() - start_time)


# ===============================================================
# 🌐 10. Speed Comparison CPU Task
# ===============================================================
def cpu_bound_task():
    count = 0
    for i in range(10**7):
        count +=i

def main_cpu_bound_task():
    #No threading here
    start = time.time()
    for _ in range(4):
        cpu_bound_task()
    end = time.time()
    print(f"Elapsed time without threads: {end-start:.3f} seconds")  

    #Threading here      
    start = time.time()
    threads = [threading.Thread(target=cpu_bound_task) for _ in range(4)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    end = time.time()
    print(f"Elapsed time with threads: {end-start:.3f} seconds")    

# ===============================================================
# 🌐 10. Multi Processing
# ===============================================================
def cpu_bound_task():
    count = 0
    for i in range(10**7):
        count +=i

def main_multi_processing():
    #Multi Processes
    start = time.time()
    processes = [Process(target=cpu_bound_task) for _ in range(4)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

    end = time.time()
    print(f"Elapsed time with processes: {end-start:.3f} seconds") 
### ⚡ Performance Comparison
"""
| Execution Type   | Description                     | Time Taken (sec) |
|------------------|----------------------------------|------------------|
| 🧵 No Threads     | Sequential execution (single thread) | **1.578** |
| 🔀 Multithreading | Multiple threads (I/O-bound tasks)   | **1.538** |
| 🧠 Multiprocessing | True parallelism (CPU-bound tasks)   | **0.589** |

"""

# ===============================================================
# 🧩 Entry Point
# ===============================================================
if __name__ == "__main__":
    # Uncomment any function to test specific threading concept
    # main_threading()
    # main_multithreading()
    # main_daemon()
    # main_sync_lock()
    # main_queue()
    # main_thread_pool_executor()
    # main_event()
    #main_fetch_url()
    #main_cpu_bound_task()
    main_multi_processing()


