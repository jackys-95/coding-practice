def without_string(base, remove):
    '''
    Returns base with the substring remove deleted from base, if found
    '''
    import re
    return re.sub(remove, "", base)

print(without_string("Hello there", "llo"))
print(without_string("Hello there", "e"))
print(without_string("Hello there", "x"))