def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    i = 0
    min_even = 0 

    while i < len(data):
        if data[i] % 2 == 1: 
            if min_even == 0 or data[i] < min_even:
                min_even = data[i]
        i += 1

    return min_even

