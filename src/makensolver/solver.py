import itertools

from .errors import CalculateFailedError
from .formula import Formula
from .operator import ARITHMETIC_OPERATORS, OTHER_BINARY, UNARY
from .operator.interface import Operator


class Solver:
    """
    解析結果を探索するクラス
    """

    def __init__(
        self,
        require_one_result: bool = False,
        is_special_rule: bool = False,
    ) -> None:
        """
        コンストラクタ

        Parameters
        ----------
        require_one_result: bool
            解析結果が1つだけ欲しいかどうか
            Trueの場合は1つ見つけた段階で探索を終了する
        is_special_rule: bool = False
            四則演算以外も許可するかどうか
            Trueの場合は、四則演算以外も許可する
        """
        self.__require_one_result = require_one_result
        self.__is_special_rule = is_special_rule

    def solve(self, available_numbers: list[int], target_number: int) -> list[Formula]:
        """
        入力された数値のリストと目標の数値を使って探索する

        Parameters
        ----------
        available_numbers: list[int]
            使用する数値のリスト
        target_number: int
            目標の数値

        Returns
        ----------
        : list[Formula]
        """
        numbers = tuple(available_numbers)
        n_numbers = len(available_numbers)

        # 単項演算子の抽出(今はなし)
        ops: list[Operator] = UNARY * self.__is_special_rule
        unaries = list(
            itertools.chain.from_iterable(
                itertools.combinations_with_replacement(ops, iter)
                for iter in range(n_numbers + 1)
            )
        )

        # 2項演算子の抽出（4足演算だけ）
        ops = ARITHMETIC_OPERATORS + OTHER_BINARY * self.__is_special_rule
        binaries = list(itertools.combinations_with_replacement(ops, n_numbers - 1))

        # 演算子と数値の組み合わせを作成し、条件似合うかどうか判定する
        result: list[Formula] = []
        for ope1 in unaries:
            for ope2 in binaries:
                combination = numbers + tuple(ope1) + tuple(ope2)

                # 数値と演算子の順列
                for candidate in itertools.permutations(combination):
                    try:
                        formula = Formula(candidate)

                        # 答えが合うこと
                        if formula.answer != target_number:
                            continue

                        result.append(formula)
                        if self.__require_one_result and len(result) == 1:
                            return result

                    except CalculateFailedError:
                        continue

        result = self.__organize_results(result)

        return result

    def __organize_results(self, results: list[Formula]) -> list[Formula]:
        """
        探索結果のうち、順序が違うだけのものは削除する

        Notes:
        ------
        - 括弧により符号が逆転するものは除けていない
            - 1 - (1 - 1)と1 - 1 + 1
        """
        set_sorted_results = set()
        organized_results: list[Formula] = []

        for res in results:
            sorted_res = tuple(sorted(list(map(str, res.values))))
            if sorted_res not in set_sorted_results:
                organized_results.append(res)
                set_sorted_results.add(sorted_res)

        return organized_results
