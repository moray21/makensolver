from abc import ABC, abstractmethod


class Operator(ABC):
    @abstractmethod
    def __str__(self) -> str:
        """
        str型で表示する際の記号
        """
        ...

    @abstractmethod
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
        """
        ...


class UnaryOperator(Operator):
    @abstractmethod
    def __call__(self, x: float) -> float:
        """
        演算子を用いて計算する

        Parameters
        ----------
        x: float
            演算に使用する数値

        Returns
        -------
        : float
        """
        ...


class BinaryOperator(Operator):
    @abstractmethod
    def __call__(self, x: float, y: float) -> float:
        """
        演算子を用いて計算する(x 演算子 yの関係)

        Parameters
        ----------
        x: float
            演算に使用する数値(前側)
        y: float
            演算に使用する数値(後側)

        Returns
        -------
        : float
        """
        ...
