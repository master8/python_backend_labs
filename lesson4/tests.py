from lesson4.targetfun import gcd
import math


class TestGCD:
    def test_n_zero(self):
        assert gcd(5, 0) == 5

    def test_m_zero(self):
        assert gcd(0, 7) == 7

    def test_both_zero(self):
        assert gcd(0, 0) == 0

    def test_equals_numbers(self):
        assert gcd(8, 8) == 8

    def test_m_is_even_n_is_even(self):
        assert gcd(42, 84) == math.gcd(42, 84)

    def test_m_is_even_n_is_odd(self):
        assert gcd(42, 81) == math.gcd(42, 81)

    def test_m_is_odd_n_is_even(self):
        assert gcd(15, 108) == math.gcd(15, 108)

    def test_m_is_odd_n_is_odd(self):
        assert gcd(317, 73) == math.gcd(317, 73)

