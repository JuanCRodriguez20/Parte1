from arreglo import min_array


def test_min_array():
    assert min_array({2,3,5,6,8,9,0}) == 0
    assert min_array({2,2,1}) == 1
    assert min_array({3,9,7,6,5,4,2}) == 2