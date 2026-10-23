# Lab 5: Static Code Analysis

## Objective

To improve the code quality, security, and maintainability of the address book program using Pylint, Bandit, and Flake8.

## Tools Used

- **Pylint:** Evaluates code quality, naming conventions, documentation, and programming practices.
- **Bandit:** Identifies common security vulnerabilities in Python code.
- **Flake8:** Checks Python style and formatting according to PEP 8 guidelines.

## Issues Identified and Fixes Applied

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Missing module docstring | Code Quality (Pylint) | 1 | The Python file did not contain a module-level docstring describing its purpose. | Added a module docstring explaining the address book's functionality. |
| Missing function docstrings | Code Quality (Pylint) | Multiple | Functions lacked docstrings describing their purpose. | Added descriptive docstrings to the functions. |
| CamelCase naming | Code Quality (Pylint) | Multiple | Function names and arguments did not follow Python's recommended snake_case naming convention. | Renamed functions and parameters using snake_case. |
| Broad exception handling | Code Quality (Pylint) | 34 | A broad `except Exception` could hide unexpected errors. | Replaced it with `except KeyError` to handle a missing contact specifically. |
| Inefficient loop using `range(len())` | Code Quality (Pylint) | 49 | The loop used indices to access elements instead of iterating directly. | Replaced it with `enumerate()` to access the index and contact name together. |
| Missing file encoding | Code Quality (Pylint) | 54, 66 | Files were opened without explicitly specifying an encoding. | Added `encoding="utf-8"` to file operations. |
| Weak MD5 hashing | Security (Bandit – B324) | 19 | MD5 was used to generate contact IDs even though it is considered a weak hash algorithm. | Replaced MD5 with SHA-256 and retained a shortened hexadecimal identifier. |
| Unsafe pickle deserialization | Security (Bandit – B301) | 67 | `pickle.load()` can execute malicious code when loading an untrusted backup file. | Replaced pickle-based backups with JSON serialization and added basic validation when restoring data. |
| Hardcoded password | Security (Bandit – B105) | 6 | A password-like value was hardcoded directly into the source code. | Removed the unused hardcoded password constant. |
| Missing whitespace around operator | Formatting (Flake8 – E225) | 23 | An assignment statement did not have the required whitespace around the assignment operator. | Added the required spaces. |
| Too many blank lines | Formatting (Flake8 – E303) | 47 | Excess blank lines appeared between functions. | Removed unnecessary blank lines. |
| Missing whitespace after comma | Formatting (Flake8 – E231) | 84 | A comma was not followed by the expected space. | Added a space after the comma. |
| Line too long | Formatting (Flake8 – E501) | 85 | A line exceeded the configured maximum line length. | Split the statement across multiple lines for readability. |

## Summary of Results

| Tool | Before Fixes | After Fixes |
|---|---|---|
| Pylint | 5.47/10 | 10.00/10 (last recorded result; rerun after the module docstring correction) |
| Bandit | 4 findings: 1 high, 1 medium, 2 low | No issues identified |
| Flake8 | 4 formatting violations | No violations reported |

**Note:** Line numbers refer to the original version of `address_book.py` and may differ in the corrected version.

## Reflection

### 1. What is the purpose of static code analysis?

Static code analysis examines source code without executing the program. It helps identify potential bugs, security vulnerabilities, code-quality problems, and formatting inconsistencies.

### 2. How do Pylint, Bandit, and Flake8 differ?

- **Pylint:** Checks code quality, naming conventions, documentation, and potential programming issues.
- **Bandit:** Identifies common security risks in Python code.
- **Flake8:** Detects style violations and formatting issues, including those defined by Python's PEP 8 conventions.

### 3. What improvements were made?

The code was improved by adding documentation, following naming conventions, narrowing exception handling, improving file encoding, replacing MD5 with SHA-256, replacing unsafe pickle backups with JSON, and fixing formatting violations.

### 4. Are static analysis tools sufficient to guarantee that code is correct and secure?

No. Static analysis tools can identify many common issues, but they may miss runtime errors, logic bugs, and vulnerabilities that depend on execution context. Testing and manual review are also necessary.

### 5. Why is static code analysis important?

It helps developers identify issues early, improve readability and maintainability, reduce security risks, and follow consistent coding standards.

## Conclusion

Static code analysis was performed using Pylint, Bandit, and Flake8. The identified code-quality, security, and formatting issues were addressed. The Pylint score improved from 5.47/10 to 10.00/10, Bandit reported no remaining issues, and Flake8 reported no formatting violations.

