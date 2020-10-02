def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    d = dict()
    if length >= 2:
        # store each index in the dictionary by its weight
        for i in range(0,len(weights)):
            d[weights[i]] = i
    
        # loop through the weights again
        for i in range(0,len(weights)):
            # find the difference between the weight and the limit
            dif = limit-weights[i]
            # if the dif is in our dictionary
            if dif in d:
                # return the indices
                return (d[dif], i)
    return None