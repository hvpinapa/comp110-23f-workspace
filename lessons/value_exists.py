"""Quiz 2 Programming Practice ~ Value Exists!"""
__author__ = "730403031"

def value_exists(dict1: dict[str, int], vals: int) -> bool:
    """Returns a boolean to determine whether the value exists in the dictionary."""
    exists: bool = False
    for keys in dict1:
        if dict1[keys] == vals:
            exists = True
        
    return exists
