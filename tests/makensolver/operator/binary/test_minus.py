import pytest
from makensolver.operator.binary.minus import Minus


class TestMinus:
    def test_str(self) -> None:
        assert str(Minus()) == "-"

    @pytest.mark.parametrize(["x", "y", "expected_result"], [(1, 1, 0)])
    def test_call(self, x: float, y: float, expected_result: float) -> None:
        operator = Minus()
        assert operator(x, y) == expected_result

    @pytest.mark.parametrize(
        ["x", "y", "expected_x", "expected_y"],
        [
            ("1", "1", "1", "1"),
            ("1 + 1", "1 + 1", "1 + 1", "(1 + 1)"),
        ],
    )
    def test_add_bracket(
        self, x: str, y: str, expected_x: str, expected_y: str
    ) -> None:
        operator = Minus()
        bracket_x, bracket_y = operator.add_bracket(x, y)
        assert bracket_x == expected_x
        assert bracket_y == expected_y
