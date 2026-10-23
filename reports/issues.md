# Static Code Analysis – Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Missing module docstring | Pylint – Code Quality | 1 | The module lacked a description of its purpose. | Added a module-level docstring. |
| Missing function docstrings | Pylint – Code Quality | Multiple | Functions lacked documentation describing their purpose. | Added docstrings to the functions. |
| CamelCase naming | Pylint – Code Quality | Multiple | Function names and parameters did not follow the snake_case convention. | Renamed functions and parameters using snake_case. |
| Broad exception handling | Pylint – Code Quality | 34 | Catching `Exception` could hide unexpected errors. | Replaced it with `except KeyError`. |
| Inefficient loop | Pylint – Code Quality | 49 | Used `range(len(names))` to iterate over contacts. | Replaced it with `enumerate()`. |
| Missing file encoding | Pylint – Code Quality | 54, 66 | File operations did not specify an encoding. | Added `encoding="utf-8"`. |
| Weak MD5 hashing | Bandit – B324 | 19 | MD5 was used to generate contact identifiers. | Replaced MD5 with SHA-256. |
| Unsafe pickle deserialization | Bandit – B301 | 67 | `pickle.load()` can execute malicious code when loading an untrusted backup. | Replaced pickle backups with JSON and added validation. |
| Hardcoded password | Bandit – B105 | 6 | A password-like value was hardcoded in the source code. | Removed the unused password constant. |
| Missing whitespace around operator | Flake8 – E225 | 23 | Missing whitespace around an assignment operator. | Added the required spaces. |
| Too many blank lines | Flake8 – E303 | 47 | Excess blank lines appeared between functions. | Removed unnecessary blank lines. |
| Missing whitespace after comma | Flake8 – E231 | 84 | A comma was not followed by a space. | Added the required space. |
| Line too long | Flake8 – E501 | 85 | A line exceeded the configured maximum line length. | Split the statement across multiple lines. |

**Note:** Line numbers refer to the original version of `address_book.py`. They may differ in the corrected version.

## Final Analysis Results

| Tool | Before Fixes | After Fixes |
|---|---|---|
| Pylint | 5.47/10 | 10.00/10 |
| Bandit | 4 findings: 1 high, 1 medium, 2 low | No issues identified |
| Flake8 | 4 formatting violations | No violations reported |
