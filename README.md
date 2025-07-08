# 🛒 Storefront E-commerce App

🔧 **Description**

This project is a **full-featured e-commerce platform** built with **Django** providing APIs and backend logic for a modern online store.<br />
✅ Supports **product listing, collections, carts, orders, reviews, and user management** <br />
✅ Integrated with **MySQL** as the database <br />
✅ Uses **Docker and Docker Compose** for containerized deployment <br />
✅ Includes **Jenkins CI/CD pipeline** to test, build, provision infrastructure using **Terraform**, and deploy to AWS EC2

---

## 📂 Project Structure

```
project/
├── core/                     # Core app utilities and configurations
├── likes/                    # Likes feature module
├── locustfiles/              # Load testing scripts with Locust
├── playground/               # Experimental and utility scripts
├── store/                    # Main store app (models, views, serializers, etc.)
│   ├── management/commands   # Custom Django management commands
│   ├── migrations/           # Database migrations
│   ├── signals/              # Signal handlers
│   ├── tests/                # Unit and integration tests
│   ├── admin.py
│   ├── apps.py
│   ├── filters.py
│   ├── models.py             # All store models (Product, Order, Customer, etc.)
│   ├── pagination.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── urls.py
│   ├── validators.py
│   └── views.py
├── storefront/               # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── terraform/                # Terraform files for AWS EC2 provisioning
├── .dockerignore             # Docker ignore rules
├── .gitignore                # Git ignore rules
├── docker-compose.yml        # Compose configuration for multi-container deployment
├── Dockerfile                # Docker build configuration
├── jenkinsfile               # Jenkins CI/CD pipeline
├── manage.py                 # Django management script
├── pytest.ini                # Pytest configuration
├── requirements.txt          # Python dependencies
├── script.sh                 # Deployment script for EC2 server
└── README.md                 # Project documentation
```

---

## 💡 Features

✨ **Product Catalog**: CRUD operations for products, collections, and promotions <br />
✨ **Shopping Cart**: Add, update, and delete cart items with quantity management <br />
✨ **Orders & Payments**: Order creation with payment status tracking <br />
✨ **Customer Management**: Membership levels (Bronze, Silver, Gold) with user profiles <br />
✨ **Reviews**: Submit and retrieve product reviews <br />
✨ **Images & File Uploads**: Supports multiple product images with size validation <br />
✨ **API Filtering, Searching, Ordering**: Built with Django REST Framework filters <br />
✨ **Admin Panel**: Fully configured Django admin for managing all models <br />
✨ **CI/CD Pipeline**: Jenkins pipeline to test, build Docker image, provision AWS EC2 with Terraform, and deploy the application using Docker Compose <br />
✨ **Load Testing Ready**: Locust scripts included for performance testing

---

## 🛠️ Technologies Used

* 🐍 **Python 3.12**
* 🌐 **Django & Django REST Framework**
* 🐬 **MySQL**
* 🐳 **Docker & Docker Compose**
* ☁️ **AWS EC2**
* ⚙️ **Terraform**
* 🔄 **Jenkins**
* 🔥 **Locust** (for load testing)

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/AHMED0130/your-repo.git
cd your-repo
```

### 2️⃣ Build and run with Docker Compose

Ensure Docker and Docker Compose are installed.

```bash
docker-compose up --build
```

* The Django app will be accessible at **[http://localhost:8000](http://localhost:8000)**
* phpMyAdmin will be accessible at **[http://localhost:8080](http://localhost:8080)** with:

  * Username: `root`
  * Password: `12345678`

### 3️⃣ Running Tests

If running locally without Docker:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
pytest
```

---

## ✅ CI/CD Pipeline Overview

✔️ **Test**: Runs application tests <br />
✔️ **Build**: Builds Docker image tagged as `ahmed0130/store:latest` and pushes to Docker Hub <br />
✔️ **Provision**: Uses Terraform to create AWS EC2 instance <br />
✔️ **Deploy**: SSH into EC2, copies `docker-compose.yml` and `script.sh`, and runs deployment script

---

## 📌 Deployment Environment Variables

* `DB_NAME` – Database name (default: store)
* `DB_USER` – Database user (default: root)
* `DB_PASSWORD` – Database password (default: 12345678)
* `DB_HOST` – Database host (default: db)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

### ✨ Author

Ahmed Elshnawy
[LinkedIn](https://www.linkedin.com/in/ahmed-elshnawy-9132ba2a4)


