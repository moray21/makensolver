from collections import deque
from dataclasses import dataclass
from typing import Deque

from .errors import CalculateFailedError
from .operator.interface import BinaryOperator, Operator

FormulaElement = int | Operator


@dataclass
class Formula:
    """
    逆ポーランド記法で計算式を保持するクラス
    """

    values: tuple[FormulaElement, ...]

    def __post_init__(self) -> None:
        self.__length = len(self.values)
        self.__str_answer = self.__change_notation_from_reverse_polish_to_infix()
        try:
            self.__answer = float(eval(self.__str_answer))
        except ZeroDivisionError as e:
            raise CalculateFailedError(str(e))

    def __str__(self) -> str:
        return self.__str_answer

    def __change_notation_from_reverse_polish_to_infix(self) -> str:
        """
        逆ポーランド記法の数式を中置記法の数式に変換する

        Returns
        ----------
        : str
            中置記法で表現された数式(str型)
        """
        number_queue: Deque[str] = deque(maxlen=self.__length)
        for element in self.values:
            if isinstance(element, int):
                number_queue.append(str(element))

            elif isinstance(element, BinaryOperator):
                if len(number_queue) < 2:
                    raise CalculateFailedError(
                        "Two number is required before 'Binary' operator."
                    )

                # 2つ前 演算子 1つ前 の順
                y = number_queue.pop()
                x = number_queue.pop()

                # 必要に応じて括弧をつける
                (bracket_x, bracket_y) = element.add_bracket(x, y)

                number_queue.append(f"{bracket_x} {str(element)} {bracket_y}")

            else:
                raise CalculateFailedError(f"{type(element)} is not unknown type.")

        # 最終的に1つの数値に定まること
        if len(number_queue) != 1:
            raise CalculateFailedError("operator is short.")

        return number_queue[0]

    @property
    def answer(self) -> float:
        return self.__answer
