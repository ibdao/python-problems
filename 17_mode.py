def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    curr_count = 0
    curr_highest = 0

    for num in nums:
        if nums.count(num) > curr_count:
            curr_highest = num
            curr_count = nums.count(num)
    return curr_highest