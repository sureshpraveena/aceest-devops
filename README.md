# ACEest DevOps Project

## 🚀 Project Overview

This project demonstrates a complete DevOps pipeline for a Flask-based fitness application. It covers version control, automated testing, containerization, and CI/CD implementation using GitHub Actions and Jenkins.

---

## 🧱 Tech Stack

* Python (Flask)
* Pytest
* Docker
* GitHub Actions
* Jenkins

---

## 📂 Project Structure

```
app/
tests/
Dockerfile
requirements.txt
.github/workflows/
```

---

## ⚙️ Local Setup

```bash
git clone https://github.com/kspraveena92/aceest-devops.git
cd aceest-devops
pip install -r requirements.txt
python -m app.main
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## 🐳 Docker Setup

### Build Image

```bash
docker build -t aceest-devops .
```

### Run Container

```bash
docker run -p 5000:5000 aceest-devops
```

---

## 📦 Docker Hub

Image available at:

```bash
docker pull <your-username>/aceest-devops:latest
```

---

## 🔄 CI/CD Pipeline

### GitHub Actions

* Triggered on every push
* Runs tests
* Builds Docker image

### Jenkins

* Pulls code from GitHub
* Installs dependencies
* Runs tests
* Builds Docker image

---

## 🎯 Key Features

* Automated testing using Pytest
* Containerized application using Docker
* CI/CD pipeline with GitHub Actions and Jenkins
* Production-ready deployment workflow

---

## 📌 Conclusion

This project demonstrates a complete DevOps lifecycle from development to deployment using industry-standard tools.
