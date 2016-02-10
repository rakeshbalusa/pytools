def is_ascii(s):
    """Return True if a string consists entirely of ASCII characters."""
    try:
        s.encode('ascii', 'strict')
        return True
    except UnicodeError:
        return False
    
def is_valid_owner_name(name):
    """
    Returns True if the name is valid, ie: good enough to be used as-is.
    """
    if not is_ascii(name):
        return False

    if len(name) > 255:
        return False

    if 'project' in name.lower():
        return False

    parts = name.split()
    if len(parts) <= 1:
        return False

    for part in parts:
        if len(part) < 2:
            return False
        if not part[0].isupper():
            return False
        if all(c.isupper() for c in part):
            return False

    if ' '.join(parts) != name:
        return False

    return True

print is_valid_owner_name('B.Rakesh')
print is_valid_owner_name('Balusa ^Rakesh')
print is_valid_owner_name('Balusa Rakesh')
print is_valid_owner_name('B Rakesh')

print "#########"
import re

value = 'Rakesh BalusaRg'
matchob = re.match(r'([A-Z]{1}[a-z]{1,}\s{0,1}){1,}', value)
if matchob:
    print matchob.group()