def big_function(a, b, c):
    """A big function with complex logic"""
    result = a + b * c

    if result > 100:
        result -= 10
    elif result < 0:
        result += 20

    return result

def test_big_function():
    """Functional tests for big_function"""
    # Test case 1: Positive result
    assert big_function(5, 6, 7) == 47

    # Test case 2: Negative result
    assert big_function(-10, 2, 3) == 26

    # Test case 3: Result greater than 100
    assert big_function(10, 20, 6) == 110

    # Test case 4: Result less than 0
    assert big_function(1, -15, 9) == 5

    # Test case 5: Result equal to 0
    assert big_function(0, 0, 0) == 20

test_big_function()
