
# q: what are the numbers in the list?
# a: the height of a building.

# q: what if the list is empty?
# a: return an empty list.

# q: should we include buildings with the same height as the tallest one we've seen so far?
# a: no. only buildings taller than all previous ones will be visible.

# q: should the order of visible buildings in the result match the input order?
# a: Yeah, return the visible buildings in the order the order of the original list.


# q: What do the negative numbers represent?
# a: buildings that are below ground level, which are ignored.


def skyline(building_list):
    visible = []
    max_height = float('-inf')

    for height in building_list:
        if height >= 0 and height > max_height:
            visible.append(height)
            max_height = height 
    
    return visible

# Tests
if __name__ == "__main__":
    assert skyline([-1, 1, 3, 7, 7, 3]) == [1, 3, 7]
    assert skyline([3, 3, 3, 3]) == [3]  
    assert skyline([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]  
    assert skyline([5, 4, 3, 2, 1]) == [5]  
    assert skyline([10, 7, 8, 5]) == [10]  
    assert skyline([]) == []  

    print("All tests passed!")