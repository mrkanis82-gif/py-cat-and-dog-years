from app.main import get_human_age


def test_should_return_0_for_cat_14_dog_14() -> None:
    result = get_human_age(14, 14)
    assert result == [0, 0]


def test_should_return_1_for_cat_15_dog_15() -> None:
    result = get_human_age(15, 15)
    assert result == [1, 1]


def test_should_return_2_for_cat_24_dog_24() -> None:
    result = get_human_age(24, 24)
    assert result == [2, 2]


def test_should_return_3_cat_2dog_for_cat_28_dog_28() -> None:
    result = get_human_age(28, 28)
    assert result == [3, 2]


def test_should_return_3_cat_2dog_for_cat_100_dog_100() -> None:
    result = get_human_age(100, 100)
    assert result == [21, 17]
