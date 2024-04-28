from collections import deque
from dataclasses import dataclass
from typing import Deque

from .errors import CalculateFailedError
from .operator.interface import BinaryOperator, Number, Operator, UnaryOperator

FormulaElement = int | Operator


@dataclass
class Formula:
    """
    逆ポーランド記法で計算式を保持するクラス
    """

    values: tuple[FormulaElement, ...]

    def __post_init__(self) -> None:
        self.__length = len(self.values)
        try:
            self.__calc_answer_and_str_formula()
        except ZeroDivisionError as e:
            raise CalculateFailedError(str(e))

    def __str__(self) -> str:
        return self.__str_answer

    def __calc_answer_and_str_formula(self) -> None:
        """
        数式の答えを計算する
        str型は逆ポーランド記法の数式を中置記法の数式に変換する
        """
        str_number_queue: Deque[str] = deque(maxlen=self.__length)
        number_queue: Deque[Number] = deque(maxlen=self.__length)

        for element in self.values:
            if isinstance(element, int):
                str_number_queue.append(str(element))
                number_queue.append(element)

            elif isinstance(element, BinaryOperator):
                if len(number_queue) < 2:
                    raise CalculateFailedError(
                        "Two number is required before 'Binary' operator."
                    )

                # 2つ前 演算子 1つ前 の順
                str_y = str_number_queue.pop()
                str_x = str_number_queue.pop()
                y = number_queue.pop()
                x = number_queue.pop()

                # 必要に応じて括弧をつける
                (bracket_x, bracket_y) = element.add_bracket(str_x, str_y)

                # 計算する
                new_x = element(x, y)

                str_number_queue.append(f"{bracket_x} {str(element)} {bracket_y}")
                number_queue.append(new_x)

            elif isinstance(element, UnaryOperator):
                if len(number_queue) < 1:
                    raise CalculateFailedError(
                        "One number is required before 'Unary' operator."
                    )

                str_x = str_number_queue.pop()
                x = number_queue.pop()

                bracket_x = element.add_bracket(str_x)
                new_x = element(x)

                str_number_queue.append(f"{bracket_x} {str(element)}")
                number_queue.append(new_x)

            else:
                raise CalculateFailedError(f"{type(element)} is not unknown type.")

        # 最終的に1つの数値に定まること
        if len(str_number_queue) != 1 or len(number_queue) != 1:
            raise CalculateFailedError("operator is short.")

        self.__str_answer = str_number_queue[0]
        self.__answer = number_queue[0]

    @property
    def answer(self) -> float:
        return self.__answer
