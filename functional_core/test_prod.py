def is_triangle(a, b, c):
    # triangle inequality theorem: any two sides must be greater than the third
    if (a + b) < c:
        return False
    if (b + c) < a:
        return False
    if (a + c) < b:
        return False
    else:
        return True


def is_isosceles_triangle(a, b, c):
    # where a, b, c are side lengths
    if a == b and a != c:
        return True
    if a == c and a != b:
        return True
    if b == c and a != b:
        return True
    else:
        return False


def is_scalene_triangle(a, b, c):
    # No side lengths are equal
    if a == b or a == c or b == c:
        return False
    else:
        return True


def is_equilateral_triangle(a, b, c):
    if a == b == c:
        return True
    else:
        return False


def determine_actions(length1, length2, length3):
    if is_triangle(length1, length2, length3) is False:
        yield "NOT-TRIANGLE"
    else:
        if is_equilateral_triangle(length1, length2, length3):
            yield "EQUILATERAL"
        if is_scalene_triangle(length1, length2, length3):
            yield "SCALENE"
        if is_isosceles_triangle(length1, length2, length3):
            yield "ISOSCELES"


def test_isosceles_triangle():
    length1 = 2
    length2 = 2
    length3 = 1

    actions = determine_actions(length1, length2, length3)

    assert list(actions) == ["ISOSCELES"]


def test_scalene_triangle():
    length1 = 1
    length2 = 3
    length3 = 2

    actions = determine_actions(length1, length2, length3)

    assert list(actions) == ["SCALENE"]


def test_equilateral_triangle():
    length1 = 1
    length2 = 1
    length3 = 1

    actions = determine_actions(length1, length2, length3)

    assert list(actions) == ["EQUILATERAL"]


def test_is_not_a_triangle():
    length1 = 1
    length2 = 2
    length3 = 4

    actions = determine_actions(length1, length2, length3)

    assert list(actions) == ["NOT-TRIANGLE"]


def test_is_triangle():
    length1 = 1
    length2 = 2
    length3 = 3

    actions = determine_actions(length1, length2, length3)

    assert "NOT-TRIANGLE" not in list(actions)

