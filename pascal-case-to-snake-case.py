def to_underscore(string):
    if isinstance(string, int):
        return str(string)
    
    result = string[0].lower()
    
    for c in string[1:]:
        if c.isupper():
            result += '_' + c.lower()
        else:
            result += c
    
    return result
