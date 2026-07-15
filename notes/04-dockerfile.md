# Dockerfile

## Definition

A Dockerfile is a text file containing instructions used to build a Docker image.

---

## Why do we use Dockerfile?

- Automates image creation.
- Ensures consistency.
- Eliminates manual installation.
- Enables repeatable deployments.

---

## Workflow

Dockerfile

↓

docker build

↓

Docker Image

↓

docker run

↓

Container

---

## Common Instructions

FROM

WORKDIR

COPY

RUN

EXPOSE

CMD

---

## Interview

Q. What is a Dockerfile?

Answer:

A Dockerfile is a text file containing instructions for building a Docker image.
=========================================================================
# FROM Instruction

## Definition

The FROM instruction specifies the base image for the Docker image.

---

## Syntax

FROM <image>:<tag>

Example

FROM python:3.12-slim

---

## Why do we use FROM?

Every Docker image starts from a base image.

The base image provides:

- Operating System
- Runtime
- Required tools

---

## Why python:3.12-slim?

- Python is already installed.
- pip is already available.
- Smaller image size.
- Faster download.
- Reduced attack surface.

---

## Image Variants

python:3.12

Large image.

python:3.12-slim

Recommended for production.

python:3.12-alpine

Very small but may require additional compatibility work.

---

## Interview

Q. What is the purpose of the FROM instruction?

Answer:

The FROM instruction specifies the base image used to build a Docker image.

---

## Best Practices

✔ Always use a specific version tag.

✔ Avoid latest in production.

✔ Prefer slim images when suitable.
================================================================
# WORKDIR

## Definition

WORKDIR sets the default working directory inside the container.

---

## Syntax

```dockerfile
WORKDIR /app
```

---

## Why do we use WORKDIR?

- Avoid repeatedly writing full paths.
- Improves readability.
- Ensures all commands execute from the correct location.

---

## Example

```dockerfile
FROM python:3.12-slim

WORKDIR /app
```

---

## Interview

Q. What is WORKDIR?

Answer:

WORKDIR sets the default working directory inside the container for all subsequent Dockerfile instructions.

---

## Best Practices

✔ Use an absolute path.

✔ Keep application files inside a dedicated directory such as `/app`.

✔ Avoid relying on the root (`/`) directory.
=====================================================================================
# COPY

## Definition

COPY copies files and directories from the host machine into the Docker image.

---

## Syntax

COPY <source> <destination>

---

## Example

COPY requirements.txt .

COPY . .

---

## Best Practice

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

Reason:

Docker caches dependency installation.

If only application code changes, Docker reuses the cached layer and builds the image faster.

---

## Why --no-cache-dir?

Prevents pip from storing package cache inside the image.

Results in a smaller Docker image.

---

## Interview

Q. What is COPY?

Answer:

COPY transfers files from the build context to the Docker image.

---

Q. Why copy requirements.txt before COPY . . ?

Answer:

To take advantage of Docker layer caching and reduce build time.

=====================================================================
# Docker Image

## What is a Docker Image?

A Docker image is a read-only template that contains the application, runtime, libraries, dependencies, and startup command required to create a container.

---

## Image Build Flow

Application Source

↓

Dockerfile

↓

docker build

↓

Docker Image

↓

docker run

↓

Container

---

## Verify Images

docker images

---

## Interview

Q. What is a Docker Image?

Answer:

A Docker image is a read-only package that contains everything required to run an application as a container.
======================================================================================
# Image vs Container

Docker Image

- Read-only template.
- Blueprint.
- Used to create containers.

Docker Container

- Running instance of an image.
- Executable.
- Can be started and stopped.

---

## docker run

Syntax

docker run -d --name <container-name> -p <host-port>:<container-port> <image>

Example

docker run -d --name devops-portal -p 5000:5000 devops-enterprise-portal:v1

---

## Interview

Q. Difference between Image and Container?

Answer:

An image is a blueprint, while a container is a running instance of that image.
==============================================================================
# First Production Docker Image

## Steps

1. Verify application locally.

2. Create Dockerfile.

3. Build Docker image.

4. Run Docker container.

5. Verify application.

6. Check logs.

---

## Commands

docker build -t devops-enterprise-portal:v1 .

docker run -d \
--name devops-portal \
-p 5000:5000 \
devops-enterprise-portal:v1

docker ps

docker logs devops-portal

---

## Verification

docker ps

Status should be:

Up

docker logs

Should show Flask running on port 5000.

---

## Interview

Q. How do you verify that a container is running correctly?

Answer:

- Check the container status using docker ps.
- Review logs using docker logs.
- Access the application through the exposed port.

=============================================================================================