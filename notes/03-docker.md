# Docker Notes

# Application Verification Before Docker

## Golden Rule

If the application does not run locally, Docker will not fix it.

Always verify the application before creating a Docker image.

---

## Verification Steps

1. Verify project structure.

2. Verify requirements.txt.

3. Verify Python version.

4. Install dependencies.

5. Run the application.

6. Verify the application in the browser.

---

# Python Package Manager (pip)

## Definition

pip is the official package manager for Python.

It installs Python libraries and dependencies.

---

## Commands

Check Version

```bash
pip3 --version
```

Install Package

```bash
pip install flask
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Python Virtual Environment (venv)

## Definition

A virtual environment is an isolated Python environment for a specific project.

---

## Why do we use it?

- Avoid dependency conflicts.
- Protect system Python.
- Each project has its own packages.

---

## Commands

Create

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

Deactivate

```bash
deactivate
```

Install Packages

```bash
pip install -r requirements.txt
```

---

# Application Verification

Run

```bash
python app.py
```

Expected

```text
Running on http://127.0.0.1:5000
```

Meaning

Application is successfully running.

---

# Development Server Warning

Flask uses a Development Server.

It is suitable for development only.

Production deployments typically use Gunicorn or another WSGI server.

---

# Important Points

127.0.0.1

Localhost.

---

0.0.0.0

Application listens on all network interfaces.

---

5000

Application Port.

---

404 favicon.ico

Normal.

Browser requests favicon automatically.

---

# Production Workflow

Developer

↓

Verify Application

↓

Install Dependencies

↓

Run Locally

↓

Verify Port

↓

Create Dockerfile

↓

Build Docker Image

↓

Run Container

---

# Interview Questions

## Q. Why do you verify the application before creating a Docker image?

Running the application locally confirms that the application, dependencies, and startup process work correctly before containerization.

---

## Q. What is pip?

pip is Python's package manager used to install and manage Python packages.

---

## Q. What is a virtual environment?

A virtual environment isolates project dependencies from the system Python installation.

---

## Q. Why don't we use venv inside Docker?

A Docker container is already an isolated environment, so creating another virtual environment inside the container is unnecessary.

---

# Best Practices

✔ Verify locally before Dockerizing.

✔ Use requirements.txt.

✔ Use venv only for local development.

✔ Use Docker for deployment.

✔ Never debug Docker before verifying the application.
touch