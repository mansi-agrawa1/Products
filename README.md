# Inventory Management System (Django + DRF)

A simple Inventory Management System built using **Django** and **Django REST Framework**.  
This project provides REST APIs for managing inventory items and includes features to export data as **PDF** and **Excel** reports.

---

## Features

- Full CRUD APIs for inventory items  
- PDF report generation of all items  
- Excel export of inventory data  
- Filtering and pagination support (optional bonus)  
- Built with Django REST Framework  

---

## Tech Stack

- Python 3  
- Django  
- Django REST Framework  
- SQLite (default database)  
- ReportLab (PDF generation)  
- OpenPyXL (Excel export)  

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mansi-agrawa1/Products.git
cd inventory
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Server will run at:

```
http://127.0.0.1:8000/
```

---

## API Endpoints

Base URL:

```
http://127.0.0.1:8000/api/
```

### CRUD Operations

| Action            | Method        | Endpoint              |
|-------------------|--------------|-----------------------|
| Create Item       | POST         | `/api/items/`         |
| Get All Items     | GET          | `/api/items/`         |
| Get Single Item   | GET          | `/api/items/<id>/`    |
| Update Item       | PUT / PATCH  | `/api/items/<id>/`    |
| Delete Item       | DELETE       | `/api/items/<id>/`    |

#### Example POST Request Body

```json
{
  "name": "Laptop",
  "description": "Dell Inspiron",
  "quantity": 10,
  "price": 55000.00
}
```

---

## PDF Report Export

Download a PDF report of all inventory items.

**Endpoint:**

```
GET /api/items/export/pdf/
```

**Output File:** `report.pdf`

Fields included:

- ID  
- Name  
- Quantity  
- Price  
- Created Date  

---

## Excel Export

Download an Excel file of all inventory items.

**Endpoint:**

```
GET /api/items/export/excel/
```

**Output File:** `items_report.xlsx`

Fields included:

- ID  
- Name  
- Quantity  
- Price  
- Created Date  

---

## Bonus Features 

### Filtering

Filter items by fields like quantity or price:

```
GET /api/items/?quantity=10
GET /api/items/?min_price=50000&max_price=80000
```

### Pagination

Large datasets are paginated automatically.

```
GET /api/items/?page=2
```

---

## Project Structure

```
inventory/
│
├── inventory_app/              
│   ├── models.py           
│   ├── serializers.py      
│   ├── views.py            
│   ├── urls.py             
│
├── inventory/      
│   ├── settings.py
│   ├── urls.py
│
└── manage.py
```

---

## API Testing (Postman)

A Postman collection is included in the repository under /postman.

Steps:
1. Open Postman
2. Click Import
3. Select Inventory_API.postman_collection.json
4. Set base URL as http://127.0.0.1:8000
5. Test all endpoints

Alternatively, you can access the Postman collection here:

https://web.postman.co/workspace/My-Workspace~b02b777d-06f2-491c-8c15-4864349c23dd/collection/43034121-2eb66c09-0b81-4dfc-b482-79c6b7b163f6?action=share&source=copy-link&creator=43034121

---

## Author

Developed as part of a Django Developer practical assessment.
