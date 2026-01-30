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

## Author

Developed as part of a Django Developer practical assessment.
