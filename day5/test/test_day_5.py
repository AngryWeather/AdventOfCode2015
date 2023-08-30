import src.day_5 as day_5


def test_is_string_nice_ugknbfddgicrmopn():
    result = day_5.is_string_nice("ugknbfddgicrmopn")
    assert result == True


def test_is_string_nice_aaa():
    result = day_5.is_string_nice("aaa")
    assert result == True


def test_is_string_nice_jchzalrnumimnmhp():
    result = day_5.is_string_nice("jchzalrnumimnmhp")
    assert result == False


def test_is_string_nice_haegwjzuvuyypxyu():
    result = day_5.is_string_nice("haegwjzuvuyypxyu")
    assert result == False


def test_is_string_nice_dvszwmarrgswjxmb():
    result = day_5.is_string_nice("dvszwmarrgswjxmb")
    assert result == False
