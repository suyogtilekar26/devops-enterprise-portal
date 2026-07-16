# GitHub Actions

## Definition

GitHub Actions is a CI/CD platform that automates build, test, and deployment workflows.

---

## Workflow

Git Push

↓

GitHub Actions

↓

Checkout

↓

Docker Build

↓

Docker Push

---

## Why use GitHub Actions?

- Automation
- Faster deployments
- Consistent builds
- CI/CD pipelines
- Easy integration with GitHub

---

## Interview

Q. What is GitHub Actions?

Answer:

GitHub Actions is GitHub's built-in CI/CD service used to automate software development workflows such as building, testing, and deploying applications.

---

## Common Trigger

on:
  push:
    branches:
      - main