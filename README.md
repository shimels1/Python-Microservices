
# Python Microservices with Django, Flask, Docker, MySQL, and RabbitMQ

This project showcases a practical implementation of microservices architecture using Python. It includes two independent services developed with **Django** and **Flask**, communicating through **RabbitMQ** and sharing a **MySQL** database — all containerized using **Docker**.

---

## Overview

The application is structured into two services:

- **Main Service**: Built with Flask, this handles core business logic and interacts with the admin service through RabbitMQ.
- **Admin Service**: Built with Django, this manages administrative functionality, including database operations and internal APIs.

RabbitMQ is used as the messaging backbone to enable asynchronous, decoupled communication between services.

---

## Features

- ⚙️ **Microservice Architecture** – Decoupled services for better scalability and maintainability.
- 🐍 **Django & Flask** – Each service leverages a different Python web framework to suit its responsibilities.
- 🐇 **RabbitMQ** – Enables asynchronous messaging between services.
- 🐬 **MySQL Database** – Centralized relational storage.
- 🐳 **Dockerized Deployment** – All services run in isolated containers for consistent environment setup.
- 🔗 **Service Communication** – Flask and Django services communicate via message queues, promoting decoupling.

---

## Project Structure

```
Python-Microservices/
├── admin/                  # Django-based admin service
│   └── ...
├── main/                   # Flask-based main service
│   └── ...
├── docker-compose.yml      # Compose file to run all services
├── .env                    # Environment variables
├── .gitignore
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- Docker & Docker Compose
- Git

---

### Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/shimels1/Python-Microservices.git
cd Python-Microservices
```

2. **Start the Services**:

```bash
docker-compose up --build
```

Docker Compose will:

- Build and run the **main** (Flask) service
- Build and run the **admin** (Django) service
- Start **MySQL** and **RabbitMQ** containers

---

## Services Overview

| Service      | Tech Stack | URL                      | Description                          |
|--------------|------------|--------------------------|--------------------------------------|
| Main         | Flask      | `http://localhost:5000`  | Handles user-facing functionality    |
| Admin        | Django     | `http://localhost:8000`  | Admin panel and content management   |

---

## Environment Configuration

Make sure to configure your `.env` files (if needed) for sensitive variables like database credentials and RabbitMQ connection strings. Defaults are provided in the `docker-compose.yml`.

---

## License

This project is licensed under the **MIT License**. Feel free to use, modify, and share.
