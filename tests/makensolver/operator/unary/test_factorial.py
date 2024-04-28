import pytest
from makensolver.operator.unary.factorial import CalculateFailedError, Factorial


class TestPlus:
    def test_str(self) -> None:
        assert str(Factorial()) == "!"

    @pytest.mark.parametrize(["x", "expected_result"], [(3, 6)])
    def test_call(self, x: float, expected_result: float) -> None:
        operator = Factorial()
        assert operator(x) == expected_result

    @pytest.mark.parametrize(
        ["input"],
        [
            [5.0],  # intのみ
            [-5],  # 正のみ
            [pow(10, 36)],  # overflow
        ],
    )
    def test_call_raises(self, input: int | float) -> None:
        with pytest.raises(CalculateFailedError):
            operator = Factorial()
            operator(input)

    @pytest.mark.parametrize(
        ["x", "expected_x"],
        [
            ("1", "1"),
            ("1 + 1", "(1 + 1)"),
        ],
    )
    def test_add_bracket(self, x: str, expected_x: str) -> None:
        operator = Factorial()
        bracket_x = operator.add_bracket(x)
        assert bracket_x == expected_x
