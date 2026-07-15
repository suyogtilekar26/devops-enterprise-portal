# .dockerignore

## Definition

.dockerignore excludes unnecessary files and directories from the Docker build context.

---

## Why do we use it?

- Faster Docker builds
- Smaller build context
- Improved security
- Cleaner Docker images

---

## Example

venv/
__pycache__/
*.pyc
.git
.vscode/
notes/
README.md

---

## Difference

.gitignore

Prevents files from being committed to Git.

.dockerignore

Prevents files from being sent during Docker image builds.

---

## Interview

Q. Why do we use .dockerignore?

Answer:

It excludes unnecessary files from the Docker build context, resulting in faster builds, smaller images, and improved security.

---

## Best Practices

- Exclude virtual environments.
- Exclude Git metadata.
- Exclude IDE configuration.
- Exclude temporary and cache files.