# Git Notes

## Definition

Git is a distributed version control system used to track changes in source code.

---

## Why Git?

- Version Control
- Collaboration
- Branching
- Rollback
- History Tracking

---

## Git Workflow

Working Directory
        │
        ▼
Staging Area
        │
        ▼
Local Repository
        │
        ▼
Remote Repository (GitHub)

---

## Commands Learned

git init
Initializes a Git repository.

git status
Shows repository status.

---

## Git Status Meanings

Untracked Files
Files that Git is not tracking.

Tracked Files
Files already tracked by Git.

---

## Production Best Practices

✔ Always run git status before committing.

✔ Never commit passwords or secrets.

✔ Use .gitignore.

✔ Commit small logical changes.

---

## Interview Questions

Q. What is Git?

Q. What is a repository?

Q. What are untracked files?

Q. Why do we use git status?

---

## Common Mistakes

❌ Forgetting .gitignore

❌ Committing secrets

❌ Large commits

❌ Not checking git status

---

## Golden Rule

Never Assume.
Always Verify.



## Git File Lifecycle

New File
        │
        ▼
Untracked
        │
git add
        ▼
Staged
        │
git commit
        ▼
Tracked
        │
Modify
        ▼
Modified

===============================================================
## Git Staging Area

Purpose

The staging area allows us to choose which files will be included in the next commit.

Command

git add <file>

Example

git add README.md

Interview

Q. What is the purpose of the staging area?

Answer:
It allows selective commits by preparing specific files before creating a commit.
================================================================================
## Git Identity

### Configure User

```bash
git config --global user.name "Suyog Tilekar"
git config --global user.email "suyogtilekar26@gmail.com"
```

### Verify

```bash
git config --global --list
```

### Why?

Git records the author name and email with every commit. This helps track who made each change and is visible in the commit history.