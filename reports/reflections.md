# Static Code Analysis – Reflections

### 1. What is the purpose of static code analysis?

Static code analysis examines source code without executing the program. It helps identify potential bugs, security vulnerabilities, code-quality issues, and formatting inconsistencies early in development.

### 2. How do Pylint, Bandit, and Flake8 differ?

- **Pylint:** Evaluates code quality, naming conventions, documentation, and potential programming errors.
- **Bandit:** Identifies common security vulnerabilities in Python code.
- **Flake8:** Detects Python style violations, formatting problems, and other linting issues.

### 3. What improvements were made to the address book?

The code was improved by adding docstrings, following snake_case naming conventions, narrowing exception handling, specifying file encodings, replacing MD5 with SHA-256, and replacing unsafe pickle-based backups with JSON serialization and validation. Formatting violations were also corrected.

### 4. Are static analysis tools sufficient to guarantee correct and secure code?

No. Static analysis tools identify many common issues, but they cannot guarantee that a program is completely correct or secure. Runtime errors, logical bugs, and context-dependent vulnerabilities may require testing and manual review.

### 5. Why is static code analysis important in software development?

Static code analysis helps detect problems early, improve readability and maintainability, reduce security risks, and encourage consistent coding standards. It also makes code reviews and future maintenance easier.

## Conclusion

The address book was analysed using Pylint, Bandit, and Flake8. After fixing the identified issues, the Pylint score improved from 5.47/10 to 10.00/10, Bandit reported no remaining issues, and Flake8 reported no formatting violations. This exercise demonstrated how static analysis tools can improve code quality, security, and maintainability.
