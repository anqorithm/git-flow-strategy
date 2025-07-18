# GitFlow Strategy

## 1. Introduction

This project uses the **GitFlow** branching model to manage features, bugfixes, releases, and hotfixes for a simple calculator class. This document explains the workflow, branch types, and best practices for contributing and maintaining code quality.

---

## 2. Branching Model Overview

- **main**: Production-ready code.
- **dev**: Latest development changes.
- **feature/**: New features (e.g., `feature/add-method`).
- **bugfix/**: Non-production bug fixes (e.g., `bugfix/handle-negative-input`).
- **release/**: Release preparation (e.g., `release/v1.0.0`).
- **hotfix/**: Urgent production fixes (e.g., `hotfix/divide-by-zero`).

---

## 3. GitFlow Example Diagram

```mermaid
gitGraph
    commit
    branch dev
    checkout dev
    commit

    %% First release: add & subtract
    branch feature/add-method
    checkout feature/add-method
    commit
    checkout dev
    merge feature/add-method

    branch feature/subtract-method
    checkout feature/subtract-method
    commit
    checkout dev
    merge feature/subtract-method

    branch release/v1.0.0
    checkout release/v1.0.0
    commit id: "Release prep v1.0.0"

    checkout main
    commit id: "Tag: v1.0.0"
    merge release/v1.0.0

    checkout dev
    merge release/v1.0.0

    %% Second release: multiply & divide
    branch feature/multiply-method
    checkout feature/multiply-method
    commit
    checkout dev
    merge feature/multiply-method

    branch feature/divide-method
    checkout feature/divide-method
    commit
    checkout dev
    merge feature/divide-method

    branch release/v1.1.0
    checkout release/v1.1.0
    commit id: "Release prep v1.1.0"

    checkout main
    merge release/v1.1.0
    commit id: "Tag: v1.1.0"

    checkout dev
    merge release/v1.1.0

    %% Hotfix after v1.1.0
    branch hotfix/divide-by-zero
    checkout hotfix/divide-by-zero
    commit id: "Fix: divide-by-zero"

    checkout main
    merge hotfix/divide-by-zero
    commit id: "Tag: v1.1.1"

    checkout dev
    merge hotfix/divide-by-zero

    %% Bugfix example
    checkout dev
    branch bugfix/handle-negative-input
    checkout bugfix/handle-negative-input
    commit id: "Fix: handle negative input"
    checkout dev
    merge bugfix/handle-negative-input
```

---

## 4. Branch Usage Summary

| Branch Type   | Purpose                                 | Created From | Merged Into      | Example Name                  |
|---------------|-----------------------------------------|--------------|------------------|-------------------------------|
| main          | Production releases                     | release/hotfix | —                | main                          |
| dev       | Latest development                      | feature/bugfix/release | —         | dev                       |
| feature/      | New features                            | dev      | dev          | feature/add-method            |
| bugfix/       | Non-production bug fixes                | dev      | dev          | bugfix/handle-negative-input  |
| release/      | Release preparation                     | dev      | main, dev    | release/v1.0.0                |
| hotfix/       | Urgent production bug fixes             | main         | main, dev    | hotfix/divide-by-zero         |

---

## 6. How to Run Tests

```bash
$ uv venv
$ source .venv/bin/activate
$ uv sync
$ pytest tests/test_calculator.py -v
```

---

## 8. All Bug Handling Scenarios in GitFlow

| # | Scenario                                | Branch to Create                | Base Branch      | Merge Back Into        | Notes                                                      |
| - | --------------------------------------- | ------------------------------- | ---------------- | ---------------------- | ---------------------------------------------------------- |
| 1 | Bug in feature/* (in-progress feature)   | Fix directly in `feature/*`     | `feature/*`      | `dev` (via PR)         | Not merged yet, so fix inline                              |
| 2 | Bug in dev (pre-production bug)          | `bugfix/*`                      | `dev`            | `dev` (via PR)         | Used during development/testing                            |
| 3 | Bug in release/* (during regression)     | `bugfix/release-*` (if critical) | `release/*`      | `release/*` (then main, dev) | Critical: branch+fix; Non-critical: register for next sprint |
| 4 | Bug in main (production bug)             | `hotfix/*`                      | `main`           | `main`, `dev` (via PR) | Urgent fixes, patch tagged (e.g., v1.1.1)                  |

**Note:**
- For critical bugs found during release regression, create a `bugfix/release-*` branch from the release branch, fix, and merge back into the release branch. After release, merge the release branch into both `main` and `dev`.
- For non-critical bugs, register the issue for the next sprint and do not fix in the release branch.

## 9. GitFlow Graph

![GitFlow Graph](assets/gitflow-graph.png)