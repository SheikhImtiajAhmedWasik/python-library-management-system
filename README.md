<div align="center">

# 📚 Library Management System

### 🐍 Console-Based Library Management System using Python OOP

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![OOP](https://img.shields.io/badge/Concept-OOP-success?style=for-the-badge)
![CLI](https://img.shields.io/badge/Application-Console-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Assignment-red?style=for-the-badge)

</div>

---

# 🎯 Objective

Develop a **Console-Based Library Management System** using **Object-Oriented Programming (OOP)** concepts in Python.

This project demonstrates your understanding of:

- Classes & Objects
- Constructors
- Inheritance
- Encapsulation
- Properties
- Class Methods
- Static Methods
- Composition
- Method Overriding
- Project Organization

---

# 🎓 Learning Outcomes

After completing this assignment, students should be able to:

- ✅ Create and use **Classes & Objects**
- 🏗️ Work with constructors (`__init__`)
- 📦 Use instance variables and methods
- 🏛️ Use class variables and class methods
- ⚙️ Create static methods
- 🔒 Apply encapsulation using private attributes
- 🏷️ Use `@property` for getters and setters
- 👨‍👩‍👦 Implement inheritance and method overriding
- 🧩 Apply composition between classes
- 📁 Organize Python projects into multiple files
- 🚀 Push a complete project to GitHub

---

# 📖 Project Description

A library wants to replace its paper-based management system with a simple software application.

The system should allow a librarian to:

- ➕ Add new books
- 👤 Register members
- 📖 Borrow books
- 🔄 Return books
- 📚 View all books
- 👥 View all members
- 🔍 Search books by title
- 🚪 Exit the program

> **Note:** All data remains **in memory**. No database is required.

---

# 🏗️ Project Structure

## 👤 1. Person (Parent Class)

### Attributes

| Attribute | Description |
|-----------|-------------|
| `name` | Person's name |
| `age` | Person's age |

### Methods

```python
display_info()
```

---

## 👥 2. Member (Child of Person)

### Additional Attributes

| Attribute | Description |
|-----------|-------------|
| `member_id` | Unique member ID |
| `borrowed_books` | List of borrowed books |

### Methods

```python
borrow_book()
return_book()
display_info()   # Override
```

---

## 📖 3. Book

### Attributes

| Attribute | Description |
|-----------|-------------|
| `title` | Book title |
| `author` | Author name |
| `isbn` | Unique ISBN |
| `status` | Available / Borrowed |

### Methods

```python
display_book()
```

### Encapsulation

Use encapsulation for book availability.

Create:

- 🔒 Getter
- 🔒 Setter
- 📖 Read-only property (if needed)

---

## 🏛️ 4. Library

### Attributes

| Attribute | Description |
|-----------|-------------|
| `books` | Collection of books |
| `members` | Collection of members |

### Methods

```python
add_book()
register_member()
borrow_book()
return_book()
show_books()
show_members()
search_book()
```

### Composition

A **Library** contains multiple **Books** and **Members**.

---

# 📋 Main Menu

```text
=========================================
LIBRARY MANAGEMENT SYSTEM
=========================================

1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. Show All Books
6. Show All Members
7. Search Book
8. Exit
```

---

# 🚀 Features

## ➕ Add Book

Collect:

- Book Title
- Author
- ISBN

✔️ Save the book into the library.

---

## 👤 Register Member

Collect:

- Member ID
- Name
- Age

✔️ Register a new library member.

---

## 📖 Borrow Book

Allow a member to borrow a book using:

- Member ID
- Book ISBN

---

## 🔄 Return Book

Return a borrowed book using:

- Member ID
- Book ISBN

---

## 📚 Show All Books

Display every book in a readable format.

Example:

```text
ISBN : B101
Title : Python Programming
Author : John Smith
Status : Available
```

---

## 👥 Show All Members

Display all registered members.

Example:

```text
Member ID : M001
Name : Naimur
Age : 23
Borrowed Books : 0
```

---

## 🔍 Search Book

Search a book by **Title**.

### If Found

```text
Book Found!

ISBN : B101
Title : Python Programming
Author : John Smith
Status : Borrowed
```

### Otherwise

```text
Book not found.
```

---

## 🚪 Exit

Safely terminate the application.

```text
Thank you for using Library Management System.
Goodbye!
```

---

# 📋 Sample Workflow

### ➕ Add Book

```text
----- Add New Book -----

Enter Book Title : Python Programming
Enter Author : John Smith
Enter ISBN : B101

Book added successfully!
```

---

### 👤 Register Member

```text
----- Register Member -----

Enter Member ID : M001
Enter Name : Naimur
Enter Age : 23

Member registered successfully!
```

---

### 📖 Borrow Book

```text
------ Borrow Book ------

Enter Member ID : M001
Enter Book ISBN : B101

Book borrowed successfully.
```

---

### 🔄 Return Book

```text
------ Return Book ------

Enter Member ID : M001
Enter Book ISBN : B101

Book returned successfully.
```

---

### 📚 Show Books

```text
------------- BOOK LIST -------------

ISBN : B101
Title : Python Programming
Author : John Smith
Status : Available

-------------------------------------

ISBN : B102
Title : Data Structures
Author : Ahmed Ali
Status : Available
```

---

### 👥 Show Members

```text
----------- MEMBER LIST ------------

Member ID : M001
Name : Naimur
Age : 23
Borrowed Books : 0
```

---

### 🔍 Search Book

```text
------ Search Book ------

Enter Book Title : Python Programming

Book Found!

ISBN : B101
Title : Python Programming
Author : John Smith
Status : Borrowed
```

---

# ⚠️ Validation Rules

The application must enforce the following rules:

- ✅ Book ISBN must be unique.
- ✅ Member ID must be unique.
- ✅ Age must be greater than **0**.
- ✅ Book title cannot be empty.
- ✅ Author name cannot be empty.
- ✅ Prevent borrowing an already borrowed book.
- ✅ A member cannot borrow the same book twice.

---

# ❌ Example Error Cases

| Scenario | Message |
|----------|---------|
| Duplicate ISBN | `Error: ISBN already exists.` |
| Duplicate Member ID | `Error: Member ID already exists.` |
| Invalid Member | `Member not found.` |
| Book Not Found | `Book not found.` |
| Search Not Found | `Book not found.` |
| Invalid Age | `Error: Age must be greater than 0.` |

---

# ⚠️ Exception Handling

Handle the following exceptions using **try-except**.

| Exception | Description |
|-----------|-------------|
| Invalid Menu Choice | User selects an invalid menu option |
| Invalid Age Input | Age is not a number |
| Empty Input | Required input is blank |
| Duplicate ISBN | Book ISBN already exists |
| Duplicate Member ID | Member ID already exists |
| Unexpected Runtime Errors | Prevent application crashes |

> **The application should never crash because of invalid user input.**

---

# 🛠 OOP Concepts Used

| Concept | Applied |
|---------|:--------:|
| Classes & Objects | ✅ |
| Constructors (`__init__`) | ✅ |
| Instance Variables | ✅ |
| Instance Methods | ✅ |
| Class Variables | ✅ |
| Class Methods | ✅ |
| Static Methods | ✅ |
| Encapsulation | ✅ |
| Properties (`@property`) | ✅ |
| Inheritance | ✅ |
| Method Overriding | ✅ |
| Composition | ✅ |

---

<div align="center">

## ⭐ Built with Python & Object-Oriented Programming

A simple console-based Library Management System designed to demonstrate core **Python OOP concepts**.

If you found this project helpful, consider giving it a ⭐ on GitHub!

</div>
