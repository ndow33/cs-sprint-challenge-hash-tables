def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # create a dictionary
    d = {}
    # loop through the list
    for value in a:        
        # check to see if the value is positive
        if value > 0:
            # if the value is not in the dictionary
            if value not in d:
                # add it to the dictionary
                d[value] = 1  
    # create an empty list to store the answers
    result = []
    # loop through the inverse of the list
    a = [-1*(value) for value in a]
    for value in a:
        if value in d:
            result.append(value)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))