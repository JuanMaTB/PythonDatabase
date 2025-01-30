# 🏫 Driving School Management System

## 📖 Project Description
This project is a **Driving School Management System** designed to **register and manage students, instructors, classes, payments, and invoices**. The system provides a **console-based interactive menu** that allows users to perform various actions, such as:
- Registering students and instructors 👨‍🎓👩‍🏫  
- Scheduling driving lessons 🚘  
- Managing advance payments and generating invoices 💰  
- Storing and retrieving data with **JSON persistence** 📝  

The project is written in **Python** and follows a **modular structure**, ensuring flexibility and ease of maintenance.

---

## ⚙ **Features**
✔ **Console Interactive Menu**: Users can navigate through an easy-to-use menu.  
✔ **Student & Instructor Management**: Add, modify, and display student and instructor records.  
✔ **Class Scheduling**: Keep track of student lessons and assigned instructors.  
✔ **Payments & Invoices**: Manage advance payments and automatically generate invoices.  
✔ **Data Persistence with JSON**: Data is saved in `.json` files to ensure persistence between sessions.  

---

## 📂 **Project Structure**
📂 driving_school_management/ 
│── 📄 main.py # Main entry point that starts the interactive menu 
│── 📄 menu.py # Interactive console menu for user interactions 
│── 📄 registro.py # Core classes (Student, Instructor, Classes, Payments, etc.) 
│── 📄 gestor_datos.py # Handles data persistence (JSON storage) │── 📄 alumnos.json # Stores registered students 
                                                                  │── 📄 profesores.json # Stores registered instructors 
                                                                  │── 📄 clases.json # Stores scheduled classes 
                                                                  │── 📄 facturas.json # Stores generated invoices 
                                                                  │── 📄 anticipos.json # Stores advance payments

---

## 🚀 **How to Run the Project**
1. **Clone the repository**  
   ```bash
   git clone https://github.com/YOUR-USERNAME/driving-school-management.git
   cd driving-school-management
   python main.py

🛠 Technologies Used
Python 🐍
JSON for Data Persistence 📂
Pandas (optional, for future Excel support) 📊
🏗 How the Data Persistence Works
The system saves and loads data automatically using JSON files. This ensures that:

Student, instructor, class, and payment records persist between sessions.
The system can retrieve data when restarted.
Data can be manually edited using any text editor.
Example of stored alumnos.json:

json
Copiar
Editar
[
    {
        "num_registro": "2025/001",
        "nombre": "Juan",
        "primer_apellido": "Pérez",
        "segundo_apellido": "López",
        "dni": "12345678A",
        "fecha_nacimiento": "15-03-1995",
        "fecha_registro": "20-01-2025",
        "permiso_opta": "B"
    }
]
🔥 Future Improvements
While this system already supports JSON-based persistence, several enhancements can be made, including: ✅ Data Validation: Improve input validation to prevent incorrect entries (e.g., invalid dates, negative values).
✅ Excel & Database Support: Extend persistence to support Excel (with Pandas) or SQLite.
✅ GUI Integration: Convert the console-based system into a graphical application using Tkinter or Flask.


