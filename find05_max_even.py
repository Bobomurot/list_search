def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i = 0
    max_even = 0 

    while i < len(data):
        if data[i] % 2 == 0: 
            if max_even == 0 or data[i] > max_even:
                max_even = data[i]
        i += 1

    return max_even
