# Initialize some sample data
l0 = []
l1 = [[]]
l2 = [1, 2, 3, 4]
l3 = [1, 2, 3, [4]]
l4 = [[[1, 2], 3]]
l5 = [[1, [2, [3]]], 4, 5, [[6]]]


def flatten(l):
    """
    Take a list of variable dimension and flatten it to a list of one dimension
    :param l: List to flatten
    :return: List of flattened atomic objects
    """

    # The new list we'll construct
    flat_list = []

    # We're done when our input list, which we will treat like a stack, is empty
    while len(l) != 0:
        # Examine the top-most element of the stack
        elem = l.pop()

        # If it's a list, we strip 1 degree of dimensionality and push the
        # sub-elements back onto the stack for further massaging
        if isinstance(elem, list):
            for sub_elem in elem:
                l.append(sub_elem)
        else:
            # We've found an atomic piece of data, add it to our flat list
            flat_list.append(elem)

    return flat_list

assert flatten(l0) == []
assert flatten(l1) == []
assert flatten(l2) == [4, 3, 2, 1]
assert flatten(l3) == [4, 3, 2, 1]
assert flatten(l4) == [3, 2, 1]
assert flatten(l5) == [6, 5, 4, 3, 2, 1]



