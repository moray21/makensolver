from makensolver.formula import Formula


class TestFormula:
    def test_str(self) -> None:
        """正しくstr型に変換できること"""
        formula = Formula((1, 2))
        expected_print = ""
        assert str(formula) == expected_print
