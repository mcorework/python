"""
FastAPI Tea House API ☕
========================

A simple, self-contained **FastAPI** application to demonstrate how to build
and document RESTful APIs in Python. This single file includes:
- Complete CRUD operations (Create, Read, Update, Delete)
- Pydantic model for request validation
- Inline documentation and FastAPI overview

------------------------------------------------------------
📘 FastAPI Overview
------------------------------------------------------------
FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+.
It is built on **Starlette** (for async web handling) and **Pydantic** (for data validation).

✨ Key Features:
- Automatic API docs at `/docs` and `/redoc`
- Type-checked routes for cleaner and safer code
- Extremely fast performance
- Easy JSON serialization with Pydantic

------------------------------------------------------------
🚀 How to Run
------------------------------------------------------------
1. Install dependencies:
    pip install fastapi uvicorn

2. Run this script:
    uvicorn main:app --reload

3. Open in your browser:
    - Root endpoint: http://127.0.0.1:8000/
    - Interactive docs: http://127.0.0.1:8000/docs
    - ReDoc docs: http://127.0.0.1:8000/redoc

------------------------------------------------------------
📚 Example JSON for POST
------------------------------------------------------------
{
  "id": 1,
  "name": "Darjeeling",
  "origin": "India"
}
"""

# -----------------------------
# Import required libraries
# -----------------------------
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# -----------------------------
# Initialize FastAPI app
# -----------------------------
app = FastAPI(
    title="Tea House API",
    description="A simple example FastAPI project that manages tea data.",
    version="1.0.0"
)


# -----------------------------
# Define Data Model
# -----------------------------
class Tea(BaseModel):
    """
    Represents a tea item with ID, name, and origin.

    Attributes:
        id (int): Unique identifier for the tea.
        name (str): Name of the tea.
        origin (str): Region or country of origin.
    """
    id: int
    name: str
    origin: str


# -----------------------------
# In-memory Data Store
# -----------------------------
# (In a real app, this would connect to a database)
teas: List[Tea] = []


# -----------------------------
# API Routes
# -----------------------------
@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint that displays a welcome message.

    Returns:
        dict: Welcome message for the Tea House API.
    """
    return {"message": "Welcome to the Tea House API! ☕"}


@app.get("/teas", tags=["Teas"])
def get_teas():
    """
    Retrieve all teas from the collection.

    Returns:
        list[Tea]: All tea items currently stored in memory.
    """
    return teas


@app.post("/teas", tags=["Teas"])
def add_tea(tea: Tea):
    """
    Add a new tea to the in-memory list.

    Args:
        tea (Tea): A tea object containing id, name, and origin.

    Returns:
        Tea: The added tea item.
    """
    teas.append(tea)
    return tea


@app.put("/teas/{tea_id}", tags=["Teas"])
def update_tea(tea_id: int, updated_tea: Tea):
    """
    Update an existing tea by ID.

    Args:
        tea_id (int): The unique ID of the tea to update.
        updated_tea (Tea): New tea data.

    Returns:
        Tea | dict: The updated tea or an error if not found.
    """
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": f"Tea with id {tea_id} not found."}


@app.delete("/teas/{tea_id}", tags=["Teas"])
def delete_tea(tea_id: int):
    """
    Delete a tea from the collection by its ID.

    Args:
        tea_id (int): The unique ID of the tea to delete.

    Returns:
        dict: A confirmation or error message.
    """
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas.pop(index)
            return {"message": f"Tea with id {tea_id} deleted successfully."}
    return {"error": f"Tea with id {tea_id} not found."}


# -----------------------------
# Run Instructions for Direct Execution
# -----------------------------
if __name__ == "__main__":
    import uvicorn
    # Launch server for quick testing: python main.py
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
