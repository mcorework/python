# 🧪 Software Testing Overview

This repository provides information and guidelines on **Unit Testing, Integration Testing, End-to-End (E2E) Testing, and Load Testing**.  
Understanding these testing types is essential for ensuring software **quality, reliability, and performance**.

---

### 📚 Other Reference URLs

- [Unit Testing - Corey Schafer](https://www.youtube.com/watch?v=6tNS--WetLI/)
- [Load Testing - Nicolai Gram](https://www.youtube.com/watch?v=SOu6hgklQRA/)

## 1️⃣ Unit Testing
**Definition:** Testing individual units or components of a software in isolation.  
**Goal:** Ensure that each function, method, or class works as intended.  

**Key Points:**
- Focus on small, self-contained pieces of code.
- Usually automated with frameworks like **pytest**, **unittest** (Python), **JUnit** (Java).
- Tests should be **fast and independent**.

**Example (Python with pytest):**
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

# 🧩 Integration Testing

**Definition:**  
Integration Testing verifies that **different modules or components of a system work together correctly**. Unlike unit testing, which focuses on individual functions or classes, integration testing ensures that the **interfaces and interactions between modules function as expected**.  

**Purpose:**  
- Detects **issues in data flow** between modules.  
- Catches **interface mismatches** and dependency problems.  
- Ensures that combined modules produce the **expected behavior** when integrated.  

**Key Points:**  
- Usually performed after **unit testing** and before **end-to-end testing**.  
- Can be done using **real components** or **mocked dependencies**.  
- Helps to uncover **integration bugs** that are not visible during unit testing.  

**Types of Integration Testing:**  
1. **Big Bang Integration:** All components are combined and tested at once.  
2. **Incremental Integration:** Modules are tested and integrated **step by step**.  
   - **Top-down:** Starts testing from the top-level modules downwards.  
   - **Bottom-up:** Starts from lower-level modules and moves upward.  
   - **Sandwich / Hybrid:** Combines top-down and bottom-up approaches.  

**Example (Python using pytest):**  
```python
# user_service.py
def get_user_name(user_id):
    return database_get_user(user_id)['name']

# database.py
def database_get_user(user_id):
    # Mock database access
    return {"id": user_id, "name": "Alice"}

# test_integration.py
from user_service import get_user_name

def test_get_user_name():
    assert get_user_name(1) == "Alice"
```
## 🌐 End-to-End (E2E) Testing

**Definition:**  
End-to-End Testing verifies the **complete workflow of an application** from start to finish. It ensures that the **entire system, including all integrated components, works as expected** in real-world scenarios.  

**Purpose:**  
- Validates **user workflows** and business processes.  
- Ensures that **all integrated components interact correctly**.  
- Detects issues that might **not appear in unit or integration tests**.  

**Key Points:**  
- Performed in a **production-like environment**.  
- Typically involves **user interface testing**, API testing, and database interactions.  
- Simulates **real user actions** to verify system behavior.  

**Tools:**  
- **Selenium** – Automates browser actions.  
- **Cypress** – Modern JavaScript-based E2E testing framework.  
- **Playwright** – Cross-browser automation tool.  

**Example (Python with Selenium):**  
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Simulate user login
driver.find_element("id", "username").send_keys("testuser")
driver.find_element("id", "password").send_keys("password")
driver.find_element("id", "login-button").click()

# Verify successful login
assert "Dashboard" in driver.title

driver.quit()
```
## ⚡ Load Testing

**Definition:**  
Load Testing evaluates how a system performs under **high traffic or heavy usage conditions**. It helps identify performance bottlenecks, measure response times, and ensure the system can handle expected user loads.  

**Purpose:**  
- Determine **system scalability and stability**.  
- Measure **response times, throughput, and resource utilization**.  
- Detect performance issues before production deployment.  

**Key Points:**  
- Simulates **concurrent users or requests**.  
- Can uncover **CPU, memory, or database bottlenecks**.  
- Often combined with **stress testing** for extreme conditions.  

**Tools:**  
- **Apache JMeter** – Widely used open-source load testing tool.  
- **Locust** – Python-based tool for distributed load testing.  
- **Gatling** – Scala-based load testing framework with detailed reporting.  

**Example (Python using Locust):**  
```python
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_homepage(self):
        self.client.get("/")

    @task
    def load_dashboard(self):
        self.client.get("/dashboard")
