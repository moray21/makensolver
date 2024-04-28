import math

from makensolver.errors import CalculateFailedError
from makensolver.operator.interface import Number, UnaryOperator


class Factorial(UnaryOperator):
    def __str__(self) -> str:
        """
        str型で表示する際の記号
        """
        return "!"

    def __call__(self, x: Number) -> int:
        """
        演算子を用いて計算する

        Parameters
        ----------
        x: Number
            演算に使用する数値

        Returns
        -------
        : Number
        """
        if not isinstance(x, int):
            raise CalculateFailedError
        if x < 0:
            raise CalculateFailedError
        try:
            return math.factorial(x)
        except OverflowError as e:
            raise CalculateFailedError(str(e))

    def add_bracket(self, x: str) -> str:
        """
        中置記法で表現する際に括弧が必要か計算に使用する前後の値から判断し、
        必要に応じて括弧を付与して返す

        Parameters
        ----------
        x: str
            演算に使用する数値

        Returns
        -------
        bracket_x: str
            演算に使用する数値(前側), 括弧つき
        """
        if x.isdigit():
            return x

        return f"({x})"
