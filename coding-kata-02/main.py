def function_one(num_one: int, num_two: int) -> int:
    """
    This function takes two numbers and returns their sum.
    """
    return num_one * num_two

def function_two(num_one, num_two):
    return num_one+num_two

def function_three(num_one: int, num_two: int) -> int:
    """This function generates the sum of two integers.

    Args:
        num_one (int): The first integer to sum.
        num_two (int): The second integer to sum.

    Raises:
        TypeError: If either num_one or num_two is not an integer.

    Returns:
        int: The sum of num_one and num_two.
    """
    if not isinstance(num_one, int):
        raise TypeError("num_one must be an integer")
    if not isinstance(num_two, int):
        raise TypeError("num_two must be an integer")
    return num_one + num_two
    