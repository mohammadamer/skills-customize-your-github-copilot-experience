# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI that lets clients manage a collection of items. Practice defining HTTP endpoints, validating request data, and returning appropriate status codes.

## 📝 Tasks

### 🛠️ Create the API and Read Endpoints

#### Description
Set up a FastAPI application for a simple item catalog. Store items in memory while the application runs, and let clients retrieve the collection or an individual item.

#### Requirements
Completed program should:

- Create a FastAPI application that can be started with Uvicorn
- Define an item data model with a name and description
- Implement `GET /items` to return all items as JSON
- Implement `GET /items/{item_id}` to return one item
- Return HTTP `404 Not Found` when the requested item does not exist

### 🛠️ Add Create, Update, and Delete Endpoints

#### Description
Expand the API so clients can add items, change an existing item, and remove an item from the in-memory catalog.

#### Requirements
Completed program should:

- Implement `POST /items` to validate and create an item, returning HTTP `201 Created`
- Implement `PUT /items/{item_id}` to validate and replace an existing item
- Implement `DELETE /items/{item_id}` to remove an existing item
- Return HTTP `404 Not Found` when an update or delete targets a missing item
- Use FastAPI's interactive API documentation to try each endpoint