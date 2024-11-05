def parse_to_boolean(value: str) -> bool:
    """
    Convert a string to a boolean.
    Accepts 'true', '1', 't', 'y', 'yes' as True.
    Accepts 'false', '0', 'f', 'n', 'no' as False.
    Case insensitive.
    """
    true_values = {'true', '1', 't', 'y', 'yes'}
    false_values = {'false', '0', 'f', 'n', 'no'}
    
    value = value.lower()
    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError(f"Cannot parse boolean value from '{value}'")