import itertools
import sys
from multiprocessing import Process, Queue

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
        available_numbers: list[int],
        target_number: int,
        timeout: float = 10,
        require_one_result: bool = False,
        is_special_rule: bool = False,
    ) -> None:
        """
        コンストラクタ

        Parameters
        ----------
        available_numbers: list[int]
            使用する数値のリスト
        target_number: int
            目標の数値
        timeout: float
            タイムアウト時間(単位: 秒)
        require_one_result: bool
            解析結果が1つだけ欲しいかどうか
            Trueの場合は1つ見つけた段階で探索を終了する
        is_special_rule: bool = False
            四則演算以外も許可するかどうか
            Trueの場合は、四則演算以外も許可する
        """
        self.__available_numbers = available_numbers
        self.__target_number = target_number
        self.__timeout = timeout
        self.__require_one_result = require_one_result
        self.__is_special_rule = is_special_rule

    def solve(self) -> list[Formula]:
        """
        入力された数値のリストと目標の数値を使って探索する
        """
        queue: Queue = Queue()
        proc = Process(target=self.__exec_solve, args=(queue,), daemon=True)
        proc.start()
        proc.join(self.__timeout)

        # 終了コードでどう終わったか判定
        exitcode = proc.exitcode  # 0: 正常終了
        if exitcode == 1:  # 例外終了
            sys.exit(1)
        elif exitcode is None:  # timeout
            print("WARNING: timeout. solve have not completed yet.")

        results: list[Formula] = [queue.get() for _ in range(queue.qsize())]
        results = self.__organize_results(results)

        return results

    def __exec_solve(self, results: Queue) -> None:
        """
        入力された数値のリストと目標の数値を使って探索する(実際の処理の実装)
        """

        numbers = tuple(self.__available_numbers)
        n_numbers = len(self.__available_numbers)

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
        for ope1 in unaries:
            for ope2 in binaries:
                combination = numbers + tuple(ope1) + tuple(ope2)

                # 数値と演算子の順列
                for candidate in itertools.permutations(combination):
                    try:
                        formula = Formula(candidate)

                        # 答えが合うこと
                        if formula.answer != self.__target_number:
                            continue

                        results.put(formula)
                        if self.__require_one_result and results.qsize() == 1:
                            return

                    except CalculateFailedError:
                        continue

        return

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
