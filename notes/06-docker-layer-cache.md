# Docker Layer Caching

## Definition

Docker builds images in layers.

Each Dockerfile instruction creates a new layer.

If a layer has not changed, Docker reuses it during the next build.

---

## Benefits

- Faster builds
- Reduced network usage
- Faster CI/CD pipelines
- Lower build cost

---

## Example

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

Reason:

Dependencies are cached.

Application code changes do not reinstall dependencies.

---

## Interview

Q. What is Docker Layer Caching?

Answer:

Docker Layer Caching allows Docker to reuse unchanged image layers during builds, improving build performance.