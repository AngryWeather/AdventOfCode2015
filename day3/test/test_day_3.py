import src.day_3 as day_3


def test_find_houses_2_is_3():
    result = day_3.find_houses(["^", "v"])
    assert result == 3


def test_find_houses_4_is_3():
    result = day_3.find_houses(["^", ">", "v", "<"])
    assert result == 3


def test_find_houses_10_is_11():
    result = day_3.find_houses(
        ["^", "v", "^", "v", "^", "v", "^", "v", "^", "v",])
    assert result == 11
