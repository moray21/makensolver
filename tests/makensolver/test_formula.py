import pytest
from makensolver.errors import CalculateFailedError
from makensolver.formula import Formula, FormulaElement
from makensolver.operator import DIVIDE, FACTORIAL, PLUS


class TestFormula:
    def test_init(self) -> None:
        """正しく初期化され、正しく計算できること"""
        formula = Formula((2, 3, PLUS, FACTORIAL))
        assert str(formula) == "(2 + 3) !"
        assert formula.answer == 120

    @pytest.mark.parametrize(
        ["formula"],
        [[(1, PLUS)], [(FACTORIAL,)], [("s",)], [(1, 1, 1, PLUS)], [(1, 0, DIVIDE)]],
    )
    def test_init_with_(self, formula: tuple[FormulaElement, ...]) -> None:
        """計算不可な組み合わせを入力するとエラー"""
        with pytest.raises(CalculateFailedError):
            Formula(formula)
