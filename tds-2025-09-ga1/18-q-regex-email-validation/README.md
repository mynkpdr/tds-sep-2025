# 18. Regex email validation (0.4 Marks)

Objective
---------

Count the number of valid email addresses from a provided list based on a set of simple formatting rules.

The Rules for a Valid Email
---------------------------

The quiz defines a valid email as having:

- Characters before the `@` symbol (local part).

- The local part cannot start or end with a dot (`.`).

- Exactly one `@` symbol.

- A domain part after the `@` with at least one dot.

- Characters after the final dot (the top-level domain).

How to Solve
------------

You can solve this manually or with code.

### Method 1: Manual Inspection

Go through the list of emails provided in the quiz and check each one against the rules.

For example for `test@example.com`, the list is:

- `user@`: **Invalid** (no domain dot)

- `support@techfirm.net`: **Valid**

- `notanemail`: **Invalid** (no `@` symbol)

- `@company.com`: **Invalid** (no local part)

- `user.company.com`: **Invalid** (no `@` symbol)

- `test.email@university.edu`: **Valid**

- `info@startup.io`: **Valid**

- `.user@company.com`: **Invalid** (starts with a dot)

Counting the valid ones gives us a total of **3**.

### Method 2: Using a Regex Pattern

You can use a simple regex pattern to test the emails. Here is a Python script that does this:

```python
import re

# The list of emails from the quiz for test@example.com
emails = [
    "user@", "support@techfirm.net", "notanemail",
    "@company.com", "user.company.com", "test.email@university.edu",
    "info@startup.io", ".user@company.com"
]

# A regex that enforces the rules
# ^           - start of string
# [^.\s]      - does not start with a dot or whitespace
# [^@]* - any characters except @
# [^.\s]      - does not end with a dot or whitespace
# @           - the @ symbol
# [^.\s@]+    - domain part
# \.          - a dot in the domain
# [^.\s@]+    - top-level domain
# $           - end of string
pattern = re.compile(r"^[^\.\s][^@]*[^\.\s]@[^.\s@]+\.[^.\s@]+$")

valid_count = 0
for email in emails:
    if pattern.match(email):
        valid_count += 1
        print(f"'{email}' is VALID")
    else:
        print(f"'{email}' is INVALID")

print(f"\nTotal valid emails: {valid_count}")

```

Running this script will also confirm the answer is **3**.
