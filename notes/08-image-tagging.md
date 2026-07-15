# Docker Image Tagging

## Definition

A Docker tag is a version label assigned to an image.

---

## Syntax

docker tag <source-image>:<tag> <target-image>:<tag>

Example

docker tag devops-enterprise-portal:v1 devops-enterprise-portal:latest

---

## Best Practices

- Use version tags.
- Avoid latest in production.
- Keep tags immutable.
- Support rollbacks.

---

## Interview

Q. What is a Docker tag?

Answer:

A Docker tag identifies a specific version of a Docker image.

---

Q. Why avoid latest?

Answer:

Because latest changes over time and results in unpredictable deployments.

======================================================================

## Does docker tag create a new image?

No.

Docker tag creates another reference to the same image.

Example

Image ID

4d1e4b6bc915

      ▲
      │
 ┌────┴────┐
 │         │
v1      latest

Both tags refer to the same image.

No duplicate image is created.