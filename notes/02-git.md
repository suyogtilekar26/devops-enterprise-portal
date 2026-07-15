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
==========================================================
## Git Commit

### Definition

A commit creates a permanent snapshot of the staged changes.

### Syntax

git commit -m "message"

### Example

git commit -m "feat: initial project structure"

### Best Practices

✔ Write meaningful commit messages.

✔ Keep commits small and focused.

✔ Commit only related changes.

### Interview

Q. What is a Git commit?

Answer:

A Git commit creates a permanent snapshot of the staged changes in the local repository.
=============================================
## git branch -M main

### Definition

Renames the current branch to main.

### Syntax

git branch -M main

### Why?

Modern repositories use main as the default branch.

### Interview

Q. Why do most projects use main instead of master?

Answer:
main is the current industry-standard default branch adopted by Git hosting platforms.
=========================================================
## git remote

### Definition

Connects the local repository to a remote repository such as GitHub.

### Commands

git remote add origin <repository-url>

git remote -v

### Interview

Q. What is origin?

Answer:

origin is the default name of the remote GitHub repository.
====================================================================
## SSH Authentication

SSH uses a key pair.

Private Key
- Stored on your local machine.
- Never share it.

Public Key
- Added to GitHub.
- Used to authenticate your machine.

Benefits

- No password required for every push.
- More secure than HTTPS passwords.
- Standard practice in production environments.

=========================================================
## SSH Authentication with GitHub

### Generate SSH Key

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

### View Public Key

```bash
cat ~/.ssh/id_ed25519.pub
```

### Test Connection

```bash
ssh -T git@github.com
```

### Change Remote to SSH

```bash
git remote remove origin
git remote add origin git@github.com:<username>/<repository>.git
```

### Push

```bash
git push -u origin main
```

### Why SSH?

- No password required for every push.
- More secure than HTTPS passwords.
- Standard practice in production environments.

==============================================
| Command                   | Purpose                     |
| ------------------------- | --------------------------- |
| `git init`                | Initialize a Git repository |
| `git status`              | Check repository status     |
| `git add`                 | Stage files                 |
| `git commit`              | Create a snapshot           |
| `git branch -M main`      | Rename branch               |
| `git remote add origin`   | Connect to GitHub           |
| `git push -u origin main` | Push to GitHub              |

===================================================================================
