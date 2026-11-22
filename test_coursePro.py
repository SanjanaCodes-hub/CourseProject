from coursePro import calculate_grade, calculate_average


def test_grade_s():
    assert calculate_grade(95) == "S"



def test_grade_a():
    assert calculate_grade(85) == "A"


def test_grade_b():
    assert calculate_grade(70) == "B"


def test_grade_c():
    assert calculate_grade(55) == "C"


def test_grade_d():
    assert calculate_grade(45) == "D"


def test_grade_f():
    assert calculate_grade(30) == "F"


def test_average():
    assert calculate_average(80, 90, 70) == 80


def test_invalid_marks():
    assert calculate_grade(110) == "Invalid Marks"
    assert calculate_grade(-5) == "Invalid Marks"