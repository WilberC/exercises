from solution1 import is_valid_ip as s1
from solution2 import is_valid_ip as s2


def test_solution():
    assert all(solution_test(s) for s in [s1, s2])


def solution_test(solution):
    assert solution('12.255.56.1') is True
    assert solution('12.255.56.1') is True
    assert solution('') is False
    assert solution('abc.def.ghi.jkl') is False
    assert solution('123.456.789.0') is False
    assert solution('12.34.56') is False
    assert solution('12.34.56 .1') is False
    assert solution('12.34.56.-1') is False
    assert solution('123.045.067.089') is False
    assert solution('127.1.1.0') is True
    assert solution('0.0.0.0') is True
    assert solution('0.34.82.53') is True
    assert solution('192.168.1.300') is False
    return True
