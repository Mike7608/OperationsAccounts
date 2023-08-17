import main


def test_load_data():
    data = main.load_data("operations.json")
    assert isinstance(data, list)


def test_not_load_data():
    err_file = main.load_data("operations.json-0")
    assert err_file is None

# def test_get():
#     assert arrs.get([1, 2, 3], 1, "test") == 3
#     assert arrs.get([], 0, "test") == "test"
#
#
# def test_slice():
#     assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
#     assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
