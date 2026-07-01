# Student Success Platform (SSP) - System Architecture

## Overview

The Student Success Platform (SSP) is a centralized web and mobile application that enables students, faculty, placement officers, and administrators to manage academic, administrative, and placement-related activities through a secure, scalable, and role-based platform.

---

## High-Level Architecture

```mermaid
flowchart TB

%% ===========================
%% Users
%% ===========================

subgraph Users
    Student[Student]
    Faculty[Faculty]
    Placement[Placement Officer]
    Admin[Administrator]
end

%% ===========================
%% Client Layer
%% ===========================

subgraph Client_Applications
    React[React Web Application]
    Mobile[Student Mobile Application]
end

%% ===========================
%% API Layer
%% ===========================

subgraph API
    FastAPI[FastAPI REST API]
end

%% ===========================
%% Business Layer
%% ===========================

subgraph Business_Services

    Auth[Authentication Service]

    StudentService[Student Service]

    FacultyService[Faculty Service]

    AcademicService[Academic Service]

    CertificateService[Certificate Service]

    PlacementService[Placement Service]

    NotificationService[Notification Service]

    ETLService[ETL Service]

    ReportService[Reporting Service]

end

%% ===========================
%% Data Layer
%% ===========================

subgraph Data_Layer

    ORM[SQLAlchemy ORM]

end

%% ===========================
%% Database
%% ===========================

subgraph Database

    PostgreSQL[(PostgreSQL Database)]

end

%% ===========================
%% External Services
%% ===========================

subgraph External_Services

    Excel[Excel / CSV Files]

    Email[Email Service]

    Push[Push Notification Service]

    Storage[Certificate File Storage]

end

%% ===========================
%% Connections
%% ===========================

Student --> React
Faculty --> React
Placement --> React
Admin --> React

Student --> Mobile

React --> FastAPI
Mobile --> FastAPI

FastAPI --> Auth
FastAPI --> StudentService
FastAPI --> FacultyService
FastAPI --> AcademicService
FastAPI --> CertificateService
FastAPI --> PlacementService
FastAPI --> NotificationService
FastAPI --> ETLService
FastAPI --> ReportService

Auth --> ORM
StudentService --> ORM
FacultyService --> ORM
AcademicService --> ORM
CertificateService --> ORM
PlacementService --> ORM
NotificationService --> ORM
ETLService --> ORM
ReportService --> ORM

ORM --> PostgreSQL

Excel --> ETLService

NotificationService --> Email
NotificationService --> Push

CertificateService --> Storage
```

---

## Architecture Layers

### 1. Users

- Student
- Faculty
- Placement Officer
- Administrator

---

### 2. Client Applications

- React Web Application
- Student Mobile Application

---

### 3. API Layer

- FastAPI REST API

---

### 4. Business Services

- Authentication Service
- Student Service
- Faculty Service
- Academic Service
- Certificate Service
- Placement Service
- Notification Service
- ETL Service
- Reporting Service

---

### 5. Data Layer

- SQLAlchemy ORM

---

### 6. Database

- PostgreSQL

---

### 7. External Services

- Excel / CSV Import
- Email Notifications
- Push Notifications
- Certificate Storage

---

## Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | React + Vite + Tailwind CSS |
| Mobile | React Native |
| Backend | FastAPI |
| ORM | SQLAlchemy |
| Database | PostgreSQL |
| Authentication | JWT |
| ETL | Pandas + OpenPyXL |
| Notifications | Email + Push |
| Reports | PDF / Excel |
| Version Control | Git & GitHub |

---

## Data Flow

1. User logs in through the web or mobile application.
2. The request is sent to the FastAPI backend.
3. Authentication and authorization are performed.
4. The appropriate business service processes the request.
5. SQLAlchemy communicates with PostgreSQL.
6. The response is returned to the client.
7. External services are used when required for notifications, file storage, and ETL imports.

---

## Future Enhancements

- Docker Deployment
- Nginx Reverse Proxy
- Redis Cache
- Background Jobs
- AI Prediction Engine
- Chatbot Assistant
- Parent Portal
- Multi-College Support