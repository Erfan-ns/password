import string
from random import choices


def create_password(length=20, upper=False, lower=False, digit=False, pun=False):
    pool = ''
    if upper:
        pool += string.ascii_uppercase

    if lower:
        pool += string.ascii_lowercase

    if digit:
        pool += string.digits

    if pun:
        pool += string.punctuation

    if pool == '':
        pool = string.ascii_letters

    return "".join(choices(pool, k=length))


print(create_password(upper=True, lower=True, digit=True, pun=True))
print(create_password(upper=False, lower=False, digit=False, pun=False))
