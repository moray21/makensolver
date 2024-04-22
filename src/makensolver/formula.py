from dataclasses import dataclass

from .operator.interface import Operator


@dataclass
class Formula:
    """
    逆ポーランド記法で計算式を保持するクラス
    """

    values: tuple[int | Operator, ...]

    def __str__(self) -> str:
        """
        逆ポーランド記法の数式を中置記法の数式に変換する

        Returns
        ----------
        : str
            中置記法で表現された数式(str型)
        """
        return ""
