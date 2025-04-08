# 📚 BookStore API (Version 1)

Welcome to the enhanced **BookStore API**! This version adds filtering, pagination, nested relationships, and API documentation.  

---

## 1. Analysis Phase (Version 1 Updates)

### 📝 Project Description (Updates)
Extends **Version 0** with:
- **Filtering/Search**: Find authors/books by name or year.
- **Pagination**: Split large datasets into pages.
- **Nested Relationships**: Fetch authors with their books in responses.
- **Validation**: Stricter rules for titles and publication years.
- **Documentation**: Interactive Swagger/OpenAPI docs.

### 🗄️ Models (No Changes)
Same as Version 0:
- **Author**: `id`, `name`
- **Book**: `id`, `title`, `author` (ForeignKey), `publication_year`

### 📋 New Requirements
1. **Search & Filtering**  
   - Books:  
     - Filter by `author__name` (partial match, case-insensitive).  
     - Filter by `publication_year` (exact or range, e.g., `year__gte=2000`).  
   - Authors:  
     - Search by `name` (partial match, case-insensitive).  

2. **Pagination**  
   - All list endpoints (`/api/authors/`, `/api/books/`) return **10 items per page**.  

3. **Enhanced Validation**  
   - `publication_year` cannot exceed the current year.  
   - `title` must be ≥ 2 characters.  

4. **Nested Relationships**  
   - Author details endpoint (`/api/authors/<id>/`) includes a list of their books.  

5. **API Documentation**  
   - Add Swagger/OpenAPI docs at `/swagger/`.  

6. **Error Handling**  
   - Return consistent error formats (e.g., `404 Not Found` for invalid IDs).  

---

## 2. Design Phase (Version 1 Updates)

### 🖼️ Relationships Diagram  
Same as Version 0:  
![Bookstore Diagram](images/bookstore_diagram.png)  

### 🌐 Updated Endpoints  
#### Authors  
| Endpoint                | New Query Params       | Response Changes                     |  
|-------------------------|------------------------|--------------------------------------|  
| `/api/authors/`         | `?search=<name>`       | Paginated results                    |  
| `/api/authors/<id>/`    | None                   | Includes nested `books` list         |  

#### Books  
| Endpoint                | New Query Params                | Response Changes      |  
|-------------------------|---------------------------------|-----------------------|  
| `/api/books/`           | `?author=<name>&year=<year>`    | Paginated results     |  

### 📄 Response Examples  
**Author Details (with nested books):**  
```json
{
  "id": 1,
  "name": "J.K. Rowling",
  "books": [
    {"id": 1, "title": "Harry Potter 1", "publication_year": 1997},
    {"id": 2, "title": "Harry Potter 2", "publication_year": 1998}
  ]
}
```

## 🔍 Filtering Logic

### **Authors**
| Query Param       | Example                   | Description                              |
|-------------------|---------------------------|------------------------------------------|
| `?search=<name>`  | `?search=rowling`         | Case-insensitive partial name match.     |

### **Books**
| Query Param                     | Example                          | Description                              |
|----------------------------------|----------------------------------|------------------------------------------|
| `?author=<name>`                | `?author=rowling`               | Books by authors with "rowling" in name.|
| `?publication_year=<year>`      | `?publication_year=2000`        | Books published in exact year.           |
| `?publication_year__gte=<year>` | `?publication_year__gte=2000`   | Books published in/after 2000.           |
| `?publication_year__lte=<year>` | `?publication_year__lte=2000`   | Books published in/before 2000.          |

---

## 📖 Pagination

- **Default**: 10 items per page.
- **Customize**: Add `?page_size=<number>` (e.g., `?page_size=5`).
- **Response Format**:
  ```json
  {
    "count": 45,
    "next": "http://localhost:8000/api/books/?page=2",
    "previous": null,
    "results": [
      // Paginated data here
    ]
  }
