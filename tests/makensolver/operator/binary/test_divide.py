import pytest
from makensolver.operator.binary.divide import Divide


class TestDivide:
    def test_str(self) -> None:
        assert str(Divide()) == "/"

    @pytest.mark.parametrize(["x", "y", "expected_result"], [(1, 1, 1)])
    def test_call(self, x: float, y: float, expected_result: float) -> None:
        operator = Divide()
        assert operator(x, y) == expected_result

    @pytest.mark.parametrize(
        ["x", "y", "expected_x", "expected_y"],
        [
            ("1", "1", "1", "1"),
            ("1 + 1", "1 + 1", "(1 + 1)", "(1 + 1)"),
            ("1 + 1", "1 * 1", "(1 + 1)", "(1 * 1)"),
            ("1 + 1", "1 / 1", "(1 + 1)", "(1 / 1)"),
        ],
    )
    def test_add_bracket(
        self, x: str, y: str, expected_x: str, expected_y: str
    ) -> None:
        operator = Divide()
        bracket_x, bracket_y = operator.add_bracket(x, y)
        assert bracket_x == expected_x
        assert bracket_y == expected_y
