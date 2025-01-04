
---

# 🎥 YT-MANAGER  

A Python app for managing YouTube videos with three storage options: **Text File**, **SQLite**, and **MongoDB**.  
📋 Supports adding, listing, updating, and deleting videos.  
✨ Features a modular design with a consistent user experience across backends.  
💡 Ideal for learning Python, CRUD operations, and database management.  

---

## 📖 **YouTube Manager Application**  

A Python-based application to manage YouTube videos with three storage backends:  

- 🗂️ **Text File Storage**: Simple and lightweight storage for small-scale use cases.  
- 🛠️ **SQLite Database**: Structured and relational data storage for medium-scale applications.  
- 🌐 **MongoDB**: Flexible and scalable NoSQL database for larger, distributed applications.  

This repository demonstrates how to implement CRUD (Create, Read, Update, Delete) operations using different storage solutions while maintaining a consistent user experience across all implementations.  

---

## 🚀 **Features**  

- ➕ Add new YouTube videos.  
- 📝 List all stored videos.  
- ✏️ Update video details.  
- 🗑️ Delete unwanted videos.  
- 🔄 Modular design for seamless backend switching.  
- 📚 Beginner-friendly, well-documented codebase.  

---

## 🛠️ **Setup Instructions**  

### 1️⃣ Clone the Repository  

```bash
git clone https://github.com/your_username/youtube_manager.git
cd youtube_manager
```

### 2️⃣ Install Dependencies  

Use `pip` to install the required packages:  

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure MongoDB  

- Duplicate `.env.example` and rename it to `.env`.  
- Replace placeholder values with your MongoDB URI and database name:  

```env
MONGODB_URI=your_mongodb_uri
DB_NAME=your_database_name
```

---

## 💻 **Usage**  

Run any of the scripts based on your preferred storage method:  

### 📂 Text File Storage  

```bash
python youtube_manager_app.py
```

### 🛠️ SQLite Storage  

```bash
python youtube_manager_app_db.py
```

### 🌐 MongoDB Storage  

```bash
python youtube_manager_app_mongodb.py
```

Follow the on-screen prompts to manage your YouTube video collection.  

---

## 📝 **License**  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

---

🎉 **Start managing your YouTube videos like a pro today!** 🎉  

---
