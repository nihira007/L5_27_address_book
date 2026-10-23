# Lab 5: Static Code Analysis

## Objective

To improve the code quality, security, and maintainability of the address book program using Pylint, Bandit, and Flake8.

## Tools Used

- **Pylint:** Evaluates code quality, naming conventions, documentation, and programming practices.
- **Bandit:** Identifies common security vulnerabilities in Python code.
- **Flake8:** Checks Python style and formatting according to PEP 8 guidelines.

## Issues Identified and Fixes Applied

| Issue | Tool | Original Line(s) | Description | Fix Applied |
|---|---|---:|---|---|
| Missing module and function docstrings | Pylint | Multiple | Module and functions lacked documentation | Added descriptive docstrings |
| CamelCase function and argument names | Pylint | Multiple | Names did not follow the snake_case naming convention | Renamed functions and arguments to snake_case |
| Broad exception handling | Pylint | 34 | `except Exception` could catch unexpected errors | Replaced with specific `KeyError` handling |
| Inefficient iteration | Pylint | 49 | Used `range(len(names))` to iterate over a list | Replaced with `enumerate()` |
| Unspecified file encoding | Pylint | 54, 66 | File operations did not specify an encoding | Specified UTF-8 for text files |
| Weak MD5 hashing | Bandit | 19 | MD5 was used to generate contact identifiers | Replaced MD5 with SHA-256 |
| Unsafe pickle deserialization | Bandit | 67 | `pickle.load()` can execute malicious code when loading untrusted data | Replaced pickle-based backups with JSON serialization |
| Hardcoded password | Bandit | 6 | A password-like constant was hardcoded in the source | Removed the unused hardcoded credential |
| Formatting violations | Flake8 | 23, 47, 84–85 | Whitespace and line-length rules were violated | Corrected spacing and line formatting |

*Note: Line numbers refer to the original version of `address_book.py` and may differ in the updated version.*

## Before-and-After Analysis Results

| Tool | Before Fixes | After Fixes |
|---|---|---|
| Pylint | 5.47/10 | 9.86/10; one missing-module-docstring warning remained in the last verified report |
| Bandit | 4 findings: 1 high, 1 medium, 2 low | No issues identified |
| Flake8 | 4 violations | No reported violations |

### Interpretation of Results

- **Pylint:** The score increased from 5.47/10 to 9.86/10, indicating improved code quality. The last verified report still contained a missing-module-docstring warning.
- **Bandit:** All four original security findings were resolved, and the final report identified no issues.
- **Flake8:** All four original formatting violations were resolved, and the final report was empty.

## Reflection

### 1. What is static code analysis?

Static code analysis is the process of examining source code without executing the program to identify potential bugs, security vulnerabilities, and coding-standard violations.

### 2. Differentiate Pylint, Bandit, and Flake8.

Pylint evaluates code quality, naming conventions, documentation, and potential programming issues. Bandit identifies common security vulnerabilities in Python code. Flake8 checks coding style and formatting, including whitespace, line length, and PEP 8 compliance.

### 3. How did static analysis improve the address book?

Static analysis identified code-quality issues, inconsistent naming, overly broad exception handling, weak hashing, unsafe deserialization, a hardcoded credential, and formatting violations. Addressing these findings improved the program's readability, maintainability, and security. The backup and restore functionality was also tested, and the restored contacts matched the in-memory address book.

### 4. What are the limitations of static analysis?

Static analysis cannot guarantee that a program is completely free of bugs or vulnerabilities. Some findings require manual review, and runtime testing is necessary to verify program behavior.

### 5. Why is static analysis important in software development?

Static analysis helps developers detect potential problems early, maintain consistent coding standards, improve code readability, and reduce security risks before software is deployed.

## Conclusion

Pylint, Bandit, and Flake8 were used to analyze and improve the address book program. The identified code-quality, security, and formatting issues were addressed. The Pylint score improved from 5.47/10 to 9.86/10, Bandit reported no remaining issues, and Flake8 reported no remaining violations. Runtime testing confirmed that the JSON backup and restore operation preserved the contact data.

The final Pylint report should be regenerated after resolving the remaining module-docstring warning.
