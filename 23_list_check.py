def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    list_items = [item for item in lst if type(item) == list]
    return len(list_items) == len(lst)
        