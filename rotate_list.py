# q:hat if the list is empty?
# a:return an empty list

# q: can the list also rotate left?
# a: no, it can only roate to the right.

# q: does this function modify the list in place, or return a new one?
# a: this one create a new list and doesn't alter the original.

# q: can the shift by be an str?
# a: no, it has to be an integer. 

def rotate_list(lst, shift_by):
    if not lst:
        return []

    shift_by = shift_by % len(lst)
    return lst[-shift_by:] + lst[:-shift_by]

# Tests
if __name__ == "__main__":
    assert rotate_list([1, 2, 3, 4, 5], 3) == [3, 4, 5, 1, 2]
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]
    assert rotate_list([1, 2, 3], 4) == [3, 1, 2]
    assert rotate_list([], 3) == []
    assert rotate_list([42], 5) == [42]
    assert rotate_list([1, 2, 3], 3) == [1, 2, 3]

    print("All tests passed!")