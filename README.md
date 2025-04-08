# 📚 BookStore Project

Welcome to the **BookStore API**! This project is a simple yet functional API built to manage authors and books. It supports CRUD operations (Create, Read, Update, Delete) for both entities, making it an excellent starting point for learning Django and Django Rest Framework (DRF).

---

## 1. Analysis Phase

### 📝 Project Description
This project involves creating a simple API for a bookstore. The API allows users to manage authors and books by performing basic **CRUD operations**:
- **Create**: Add new authors or books.
- **Read**: Retrieve details of authors or books.
- **Update**: Modify existing authors or books.
- **Delete**: Remove authors or books.

### 🗄️ Models
- **Author**: Represents an individual author.
- **Book**: Represents a book, linked to an author (one author can have multiple books).

### 📋 Requirements
1. **Author**: Full CRUD support.
2. **Book**: Full CRUD support.
3. **Relationships**:
   - Each book must be associated with **exactly one author**.
   - An author can have **zero or more books**.
4. **Fields**:
   - **Author**: 
     - `name` (string)
   - **Book**: 
     - `title` (string)
     - `author` (foreign key to Author)
     - `publication_year` (integer)
5. **API Behavior**:
   - Basic data validation (e.g., required fields must not be empty).
6. **General Instructions**:
   - No authentication or authorization required (can be added later).
   - Use **JSON** for all requests and responses.
   - Author names do not need to be unique; uniqueness is handled by IDs.

---

## 2. Design Phase

### 🖼️ Bookstore Diagram
Here’s a visual representation of the relationship between the Author and Book models:  
![Bookstore Diagram](images/bookstore_diagram.png)  
*(Replace with your actual diagram image path.)*

### 🗄️ Models
- **Author**:
  - `id`: Primary key (auto-generated)
  - `name`: CharField (max_length=255)
- **Book**:
  - `id`: Primary key (auto-generated)
  - `title`: CharField (max_length=255)
  - `publication_year`: IntegerField
  - `author`: ForeignKey to Author (on_delete=CASCADE)

### 🌐 Endpoints Map
The API provides the following endpoints for managing authors and books:

| Endpoint                | HTTP Methods       | Description                           |
|-------------------------|--------------------|---------------------------------------|
| `/api/authors/`         | GET, POST          | List all authors or create a new one  |
| `/api/authors/<int:pk>/`| GET, PUT, DELETE   | Retrieve, update, or delete an author |
| `/api/books/`           | GET, POST          | List all books or create a new one    |
| `/api/books/<int:pk>/`  | GET, PUT, DELETE   | Retrieve, update, or delete a book    |

---
🤝 Contributing
Contributions are welcome! Fork the repository and submit a pull request. For significant changes, please open an issue first to discuss your ideas.

---
📄 License
This project is licensed under the MIT License. See the  file for details.

---
### Notes:
- **Emojis**: I’ve used Unicode emojis (e.g., 📚, 🛠️) as icons. They work well in most Markdown renderers (like GitHub). If you prefer image-based icons, you can replace them with links to images (e.g., `![icon](path/to/icon.png)`).
- **Customization**: Replace `your-username` in the clone URL with your actual GitHub username or repository URL.
- **Diagram**: The `images/bookstore_diagram.png` placeholder assumes you’ll create and upload a diagram. If you don’t have one yet, you can remove that line or create a simple diagram (e.g., using tools like Draw.io).

Let me know if you need help with anything else, like generating a diagram or tweaking the README further!
