# Multi-Stage Docker Build

## Definition

A Multi-Stage Build uses multiple FROM instructions in a Dockerfile.

Each stage has a specific purpose.

---

## Builder Stage

Compiles or prepares the application.

---

## Runtime Stage

Contains only the files required to run the application.

---

## Benefits

- Smaller images
- Better security
- Reduced attack surface
- Faster deployments
- Cleaner runtime environment

---

## Interview

Q. What is a Multi-Stage Build?

Answer:

A Multi-Stage Build separates the build environment from the runtime environment, resulting in a smaller and more secure Docker image.

---

## Best Practices

Use Multi-Stage Builds for:

- Java
- Go
- .NET
- React
- Angular
- Node.js applications

Python projects may also benefit depending on dependency complexity.