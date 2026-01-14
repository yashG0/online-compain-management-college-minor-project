# Online Complaint Management System (OCMS)

A secure, role-based web application designed to manage and track complaints within an institution such as a **college, municipality, or organization**.  
The system ensures **accountability, transparency, and traceability** throughout the complaint resolution lifecycle.

---

## 📌 Project Overview

The **Online Complaint Management System (OCMS)** allows users to submit grievances online and track their resolution status in real time.  
Authorities can manage, assign, and resolve complaints through a structured workflow backed by authentication and role-based access control.

This project is developed as a **College Minor Project**, focusing on real-world backend design and clean system architecture.

---

## 🎯 Objectives

- Provide a centralized platform for lodging complaints  
- Enable users to track complaint status securely  
- Ensure accountability through role-based access  
- Maintain a complete audit trail of complaint actions  
- Simulate real grievance-handling workflows used in institutions  

---

## 🧑‍💼 User Roles

### 1. User (Complainant)
- Register and log in securely  
- Submit new complaints  
- View and track personal complaints  
- Add follow-up messages (optional)  

### 2. Admin (Authority)
- View all submitted complaints  
- Assign complaints to departments or officers  
- Update complaint status  
- Monitor resolution progress  

### 3. Officer (Optional / Advanced)
- View assigned complaints  
- Update progress and resolution notes  

---

## 🔄 Complaint Lifecycle

Each complaint follows a controlled and auditable lifecycle:

```
OPEN → IN_PROGRESS → RESOLVED
          ↓
       REJECTED
```

- All status changes are recorded  
- Users cannot directly modify complaint status  
- Only authorized roles can perform transitions  

---

## 🛠 Technology Stack

### Backend
- FastAPI (Python)  
- RESTful API architecture  
- JWT-based authentication  
- Role-based authorization  
- SQLite / PostgreSQL database  

### Frontend
- HTML5  
- CSS3  
- Vanilla JavaScript  
- Fetch API for backend communication  

---

## 🔐 Authentication & Security

- Secure password hashing using bcrypt  
- JWT (JSON Web Token) authentication  
- Token-based session handling  
- Role-based access control (RBAC)  
- Prevention of unauthorized data access  

---

## 🗃 Database Design (Core Tables)

- **Users**
  - Stores user credentials and roles  

- **Complaints**
  - Stores complaint details, status, and assignment  

- **Complaint History**
  - Tracks all actions and status changes for audit purposes  

---

## 📂 Project Structure

```
online-complaint-management/
│
├── backend/        # FastAPI backend
├── frontend/       # Vanilla JS frontend
├── docs/           # Documentation & diagrams
├── .gitignore
└── README.md
```

---

## 📈 Key Features

- Secure user authentication  
- Role-based dashboards  
- Complaint status tracking  
- Administrative complaint management  
- Scalable and modular backend design  

---

## 🚀 Future Enhancements

- File attachment support for complaints  
- Complaint category-wise SLA tracking  
- Email notifications  
- Analytics dashboard for administrators  
- Deployment using Docker  

---

## 📄 Academic Relevance

This project demonstrates:
- Backend API design using modern Python frameworks  
- Authentication and authorization concepts  
- Real-world workflow modeling  
- Clean project structuring and documentation  

It is suitable for **college evaluation, viva discussions, and portfolio demonstration**.

---

## 📝 License

This project is developed for educational purposes as part of a college minor project.
