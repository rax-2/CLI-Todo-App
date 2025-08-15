


# 📝 MongoDB CLI Todo App

A simple **Command-Line Todo Application** built with **Python** and **PyMongo** that stores your tasks in a MongoDB database.  
Supports **adding, editing, deleting, setting statuses, and clearing completed tasks**.

---

## 📌 Features
- **Add New Todo** with title and due date.
- **List All Todos** with index, status, and deadline.
- **Edit Todos** (title or deadline).
- **Delete Single Todo** by selecting index.
- **Update Status** (Completed ✅, In Progress 🟡, Blocked ❌).
- **Clear Todos** by deleting completed or blocked tasks.
- **Quit Anytime** with `q`.

---

## 🛠 Requirements
- Python 3.8+
- MongoDB instance (local or cloud)
- `pymongo`
- `python-dotenv`

Install dependencies:
```bash
pip install pymongo python-dotenv
````

---

## ⚙️ Setup

1. Clone this repository:

```bash
git clone https://github.com/rax-2/todo-mongo-cli.git
cd todo-mongo-cli
```

2. Create a `.env` file:

```env
MONGO_URI=mongodb://localhost:27017/
DB_NAME=todoDB
DB_COLLECTION=todos
```

3. Run the app:

```bash
python main.py
```

---

## 🎮 Usage

When the app starts, it will:

* Display all stored todos
* Ask you for an action:

  * `a` → Add new todo
  * `d` → Delete a todo
  * `e` → Edit a todo
  * `s` → Set status
  * `c` → Clear completed/blocked todos
  * `q` → Quit the app

Example:

```
[1] Buy groceries               | Status: Pending     | Time: 2025-08-20
[2] Finish project report       | Status: In Progress | Time: 2025-08-18

Enter ('q' for Quit). ('a' for Add new Todo). ('d' for delete a todo)...
```

---

## 🧠 Status Codes

* ✅ **Completed** → `\033[92mCompleted\033[0m`
* 🟡 **In Progress** → `\033[93mIn Progress\033[0m`
* ❌ **Blocked** → `\033[91mBlocked\033[0m`

---
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![PyMongo](https://img.shields.io/badge/PyMongo-Driver-yellow?logo=mongodb&logoColor=white)
![MongoDB Atlas](https://img.shields.io/badge/MongoDB-Atlas-green?logo=mongodb&logoColor=white) 
![python-dotenv](https://img.shields.io/badge/python--dotenv-Environment%20Variables-orange?logo=python&logoColor=white)

## Authors

- [@Rakesh](https://www.github.com/rax-2)

