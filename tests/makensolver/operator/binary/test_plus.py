import pytest
from makensolver.operator.binary.plus import Plus


class TestPlus:
    def test_str(self) -> None:
        assert str(Plus()) == "+"

    @pytest.mark.parametrize(["x", "y", "expected_result"], [(1, 1, 2)])
    def test_call(self, x: float, y: float, expected_result: float) -> None:
        operator = Plus()
        assert operator(x, y) == expected_result

    @pytest.mark.parametrize(
        ["x", "y", "expected_x", "expected_y"],
        [
            ("1", "1", "1", "1"),
            ("1 + 1", "1 + 1", "1 + 1", "1 + 1"),
        ],
    )
    def test_add_bracket(
        self, x: str, y: str, expected_x: str, expected_y: str
    ) -> None:
        operator = Plus()
        bracket_x, bracket_y = operator.add_bracket(x, y)
        assert bracket_x == expected_x
        assert bracket_y == expected_y
