import re

from makensolver.operator.interface import BinaryOperator, Number

from .minus import Minus
from .plus import Plus


class Multiply(BinaryOperator):
    def __str__(self) -> str:
        """
        str型で表示する際の記号
        """
        return "*"

    def __call__(self, x: Number, y: Number) -> Number:
        """
        演算子を用いて計算する(x 演算子 yの関係)

        Parameters
        ----------
        x: Number
            演算に使用する数値(前側)
        y: Number
            演算に使用する数値(後側)

        Returns
        -------
        : Number
        """
        return x * y

    def add_bracket(self, x: str, y: str) -> tuple[str, str]:
        """
        中置記法で表現する際に括弧が必要か計算に使用する前後の値から判断し、
        必要に応じて括弧を付与して返す

        Parameters
        ----------
        x: str
            演算に使用する数値(前側)
        y: str
            演算に使用する数値(後側)

        Returns
        -------
        bracket_x: str
            演算に使用する数値(前側), 括弧つき
        bracket_y: str
            演算に使用する数値(後側), 括弧つき

        Notes
        -----
        - 値に「+」もしくは「-」があるとその値には括弧が必要
        """
        # 前後の数値が数字だけならそのまま返す
        if x.isdigit() and y.isdigit():
            return (x, y)

        # 既に括弧の付いている演算は1つの数字(0)に置き換えて考える
        # 例: x = '1 + (2 - 1)' →  replace_x = '1 + 0'
        replaced_x = re.sub(r"\(.+\)", "0", x)
        replaced_y = re.sub(r"\(.+\)", "0", y)

        # 「+」もしくは「-」がある場合は括弧をつける
        target_symbols = [str(Plus()), str(Minus())]
        bracket_x = f"({x})" if self.__has_symbol(replaced_x, target_symbols) else x
        bracket_y = f"({y})" if self.__has_symbol(replaced_y, target_symbols) else y

        return (bracket_x, bracket_y)

    def __has_symbol(self, x: str, symbols: list[str]) -> bool:
        """
        対象の数値(x)に確認したい演算子が含んでいるかどうかを返す

        Parameters
        ----------
        x: str
        symbols: list[str]
            確認したい演算子のリスト

        Returns
        -------
        : bool
        """
        return any(symbol in x for symbol in symbols)
