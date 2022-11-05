import re

def is_https(domain):
    if match := re.match(r"^https(?::\/\/)?.+", domain, re.IGNORECASE):
        return True
    else:
        return False