def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    i = 0
    min_even = 0 

    while i < len(data):
        if data[i] % 2 == 0: 
            if min_even == 0 or data[i] < min_even:
                min_even = data[i]
        i += 1

    return min_even
