# Lab 5: Static Code Analysis

## Objective
Improve the address book's code quality, security, and maintainability using Pylint, Bandit, and Flake8.

## Tools
- Pylint: Code quality and programming practices.
- Bandit: Common Python security vulnerabilities.
- Flake8: Python style and formatting.

## Issues Identified and Fixes

| Issue | Tool | Fix |
|---|---|---|
| Missing docstrings | Pylint | Added module and function documentation |
| CamelCase names | Pylint | Changed identifiers to snake_case |
| Broad exception handling | Pylint | Caught KeyError specifically |
| range(len(...)) iteration | Pylint | Used enumerate |
| Unspecified file encoding | Pylint | Specified UTF-8 |
| Weak MD5 hash | Bandit | Replaced with SHA-256 |
| Unsafe pickle deserialization | Bandit | Replaced pickle with JSON |
| Hardcoded password | Bandit | Removed unused credential |
| Formatting violations | Flake8 | Corrected spacing and line formatting |

## Before and After Results

| Tool | Before | After |
|---|---|---|
| Pylint | 5.47/10 | 9.86/10 before final docstring fix; verify latest score |
| Bandit | 4 findings | No issues identified |
| Flake8 | 4 violations | No reported violations |

## Reflection

### 1. What is static code analysis?
Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and coding-standard violations.

### 2. Differentiate Pylint, Bandit, and Flake8.
Pylint checks code quality, Bandit checks for common security issues, and Flake8 checks style and formatting.

### 3. How did static analysis improve the address book?
It helped identify naming and documentation issues, overly broad exception handling, weak hashing, unsafe deserialization, and formatting violations. The fixes improved readability and security.

### 4. What are its limitations?
Static analysis cannot guarantee that a program is free of defects. Runtime testing and manual review are still necessary.

### 5. Why is static analysis important?
It helps identify problems early and improves code quality, consistency, security, and maintainability.