# 📚 BookStore API (Version 1)

A Django + DRF API for managing authors and books, now with **filtering, pagination, nested relationships, and Swagger docs**.  

---

## 🔥 Features  
### **Core**  
✅ **CRUD** for `Author` and `Book` models.  
✅ **Relationships**: Each book belongs to one author; authors have many books.  

### **New in Version 1**  
🔍 **Search & Filtering**  
- Filter books by `author__name`, `publication_year` (exact/range).  
- Filter authors by `name` (case-insensitive partial match).  

📖 **Pagination**  
- Default: `10 items per page` (customizable).  

🔄 **Nested Responses**  
- Fetch an author with their books listed in the response.  

🛡️ **Validation**  
- `publication_year` cannot be in the future.  
- `title` must be ≥ 2 characters.  

📜 **Swagger Documentation**  
- Interactive API docs at `/swagger/`.  

---

## 🗄️ Models  
### **Author**  
| Field | Type      | Description          |  
|-------|-----------|----------------------|  
| `id`  | AutoField | Primary key.         |  
| `name`| CharField | Author's full name.  |  

### **Book**  
| Field               | Type        | Description                         |  
|---------------------|-------------|-------------------------------------|  
| `id`                | AutoField   | Primary key.                        |  
| `title`             | CharField   | Book title (≥ 2 chars).             |  
| `author`            | ForeignKey  | Links to `Author` (on_delete=CASCADE). |  
| `publication_year`  | IntegerField| Year (≤ current year).              |  

---

## 🌐 Endpoints  
### **Authors**  
| Endpoint                 | Method | Description                          |  
|--------------------------|--------|--------------------------------------|  
| `/api/authors/`          | GET    | List all authors (paginated).        |  
| `/api/authors/`          | POST   | Create a new author.                 |  
| `/api/authors/<id>/`     | GET    | Get author details + their books.    |  
| `/api/authors/<id>/`     | PUT    | Update an author.                    |  
| `/api/authors/<id>/`     | DELETE | Delete an author (and their books).  |  

### **Books**  
| Endpoint                 | Method | Description                          |  
|--------------------------|--------|--------------------------------------|  
| `/api/books/`            | GET    | List all books (paginated/filtered). |  
| `/api/books/`            | POST   | Create a new book.                   |  
| `/api/books/<id>/`       | GET    | Get book details.                    |  
| `/api/books/<id>/`       | PUT    | Update a book.                       |  
| `/api/books/<id>/`       | DELETE | Delete a book.                       |  

---

## 🔍 Filtering & Search  
### **Authors**  
- `GET /api/authors/?search=<name>`  
  - Case-insensitive partial match on `name`.  

### **Books**  
- `GET /api/books/?author=<name>`  
  - Filter by author name (partial match).  
- `GET /api/books/?publication_year=<year>`  
  - Exact year.  
- `GET /api/books/?publication_year__gte=<year>`  
  - Books published after `<year>`.  

