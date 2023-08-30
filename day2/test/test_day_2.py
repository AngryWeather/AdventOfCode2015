import src.day_2 as day_2


def test_calculate_surface_area_equals_52():
    result = day_2.calculate_surface_area({"w": 2, "l": 3, "h": 4})
    assert result == 52


def test_calculate_surface_area_equals_42():
    result = day_2.calculate_surface_area({"w": 1, "l": 1, "h": 10})
    assert result == 42


def test_find_area_of_smallest_side_2_3_4():
    result = day_2.find_area_of_smallest_side({"w": 2, "l": 3, "h": 4})
    assert result == 6


def test_find_area_of_smallest_side_1_1_10():
    result = day_2.find_area_of_smallest_side({"w": 1, "l": 1, "h": 10})
    assert result == 1


def test_find_total_52_and_6_is_58():
    result = day_2.find_total({"w": 2, "l": 3, "h": 4})
    assert result == 58


def test_find_total_42_and_1_is_43():
    result = day_2.find_total({"w": 1, "l": 1, "h": 10})
    assert result == 43


def test_find_total_for_all_presents_1():
    result = day_2.find_total_for_all_presents([{"w": 2, "l": 3, "h": 4}])
    assert result == 58


def test_find_total_for_all_presents_2():
    result = day_2.find_total_for_all_presents(
        [{"w": 2, "l": 3, "h": 4}, {"w": 1, "l": 1, "h": 10}])
    assert result == 58 + 43


def test_find_ribbon_for_present_10():
    result = day_2.find_ribbon_for_present({"w": 2, "l": 3, "h": 4})
    assert result == 10


def test_find_ribbon_for_present_4():
    result = day_2.find_ribbon_for_present({"w": 1, "l": 1, "h": 10})
    assert result == 4


def test_find_ribbon_for_bow_24():
    result = day_2.find_ribbon_for_bow({"w": 2, "l": 3, "h": 4})
    assert result == 24


def test_find_total_feet_of_ribbon_34():
    result = day_2.find_total_feet_of_ribbon({"w": 2, "l": 3, "h": 4})
    assert result == 34


def test_find_total_feet_of_ribbon_14():
    result = day_2.find_total_feet_of_ribbon({"w": 1, "l": 1, "h": 10})
    assert result == 14


def test_find_ribbon_for_bow_10():
    result = day_2.find_ribbon_for_bow({"w": 1, "l": 1, "h": 10})
    assert result == 10
