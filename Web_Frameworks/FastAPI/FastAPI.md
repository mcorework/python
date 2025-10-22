# 🚀 FastAPI — Modern Web Framework for Python

[FastAPI](https://fastapi.tiangolo.com/) is a **modern, fast (high-performance)** web framework for building APIs with **Python 3.7+**, based on **standard Python type hints**.  
It’s designed to make development **fast, fun, and efficient**, while ensuring **automatic data validation**, **interactive documentation**, and **excellent performance** powered by **[ASGI](https://asgi.readthedocs.io/en/latest/)** (Asynchronous Server Gateway Interface).

---

## 🧩 Overview

FastAPI is inspired by frameworks like [Flask](https://flask.palletsprojects.com/), [Express](https://expressjs.com/), and [Spring Boot](https://spring.io/projects/spring-boot), but it introduces advanced features such as **async I/O**, **[Pydantic](https://docs.pydantic.dev/)** models, and **automatic [OpenAPI](https://swagger.io/specification/)** documentation.  
It’s ideal for building **RESTful APIs**, **microservices**, and even **GraphQL** backends with minimal setup.
It has few dependancies. 
(1) uvicorn : it is basic web server.
(2) Pydantic : All python web application uses Pydantic. It has data validation libraries.
(3) typing module : data type checker


### ⚙️ Installation Commands

1. `cygnaus@CYGNAUSs-MBP FastAPI % python -m venv .venv  ` — create the virtual environment
2. `cygnaus@CYGNAUSs-MBP FastAPI % source .venv/bin/activate ` — activate the virtual environment
3. `pip install fastapi uvicorn` — insall fastapi and uvicorn
4. `pip freeze > requirements.txt` — freeze all dependencies in a config document
5. `(.venv) cygnaus@CYGNAUSs-MBP FastAPI % uvicorn main:app --reload` --Run the app with the web server
6. http://127.0.0.1:8000
7. http://127.0.0.1:8000/docs


### ✨ Key Features
- ⚡ **Blazing fast** — performance on par with Node.js & Go (thanks to [Starlette](https://www.starlette.io/) and Pydantic)
- 🧠 **Type-driven** — full use of Python type hints for data validation & autocomplete
- 🧾 **Automatic Docs** — built-in [Swagger UI](https://swagger.io/tools/swagger-ui/) and [ReDoc](https://github.com/Redocly/redoc)
- 🔄 **Asynchronous Support** — native `async` / `await` for high-concurrency APIs
- 🧩 **Dependency Injection** — clean, modular design
- 🏭 **Production Ready** — trusted by [Netflix](https://netflixtechblog.com/), [Microsoft](https://techcommunity.microsoft.com/), and [Uber](https://www.uber.com/)

---

## 📜 Brief History

FastAPI was created by **[Sebastián Ramírez](https://github.com/tiangolo)** in **2018** to provide a **high-performance, easy-to-use** API framework for Python developers.  
Its rapid adoption is due to:
- Simplicity & minimal boilerplate  
- Automatic, interactive documentation  
- Async-first design with top-tier performance  

It quickly became one of the **most-starred Python frameworks on GitHub**, surpassing Flask and Django REST Framework in growth and developer satisfaction.

---

## 🔗 Useful Links

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [uvicorn)](https://uvicorn.dev/)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [typing](https://docs.python.org/3/library/typing.html)


## 🔗 Useful Links

- [FastAPIDjango Official Documentation](https://docs.djangoproject.com/en/stable/)
- [Django Tutorial (MDN)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- [Real Python Django Guide](https://realpython.com/tutorials/django/)
- [Full Stack Python: Django](https://www.fullstackpython.com/django.html)

## ⚙️ Installation

```bash
# Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# Install FastAPI and Uvicorn (ASGI server)
pip install fastapi uvicorn
