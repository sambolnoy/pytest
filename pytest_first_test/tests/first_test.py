import pytest
from app.calculator import С


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctily(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

