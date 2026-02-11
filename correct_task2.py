# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

import re

PATTERN = re.compile( r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

def count_valid_emails(emails):
    
    if not isinstance(emails, (list, tuple)):
        return 0

    count = 0

    for email in emails:
        if not isinstance(email, str):
            continue

        email = email.strip()
        if PATTERN.match(email):
            count += 1

    return count