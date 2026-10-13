# 📘 Assignment: Python REST API Client

## 🎯 Objective

Build a Python client that communicates with the item API from the FastAPI assignment. Practice sending HTTP requests, exchanging JSON, and handling API errors.

## 📝 Tasks

### 🛠️ Retrieve Items from the API

#### Description
Complete the client functions that retrieve all items and a single item from the FastAPI service. Run the service locally at `http://127.0.0.1:8000` before testing the client.

#### Requirements
Completed program should:

- Set the API base URL in `client.py`
- Implement `list_items()` to send `GET /items` and display the returned items
- Implement `get_item(item_id)` to send `GET /items/{item_id}` and display the requested item
- Display a useful message when the item is not found or the API cannot be reached

### 🛠️ Create, Update, and Delete Items

#### Description
Complete the client functions that create, update, and delete items. Send item data as JSON and use the ID returned by the API when working with an item.

#### Requirements
Completed program should:

- Implement `create_item(name, description)` with `POST /items` and display the created item
- Implement `update_item(item_id, name, description)` with `PUT /items/{item_id}`
- Implement `delete_item(item_id)` with `DELETE /items/{item_id}`
- Handle the empty response from a successful `204 No Content` delete
- Add test calls in `main()` that create an item, update it, retrieve it, and delete it