from .formula import Formula


class Solver:
    """
    解析結果を探索するクラス
    """

    def __init__(self, require_one_result: bool = False) -> None:
        """
        コンストラクタ

        Parameters
        ----------
        require_one_result: bool
            解析結果が1つだけ欲しいかどうか
            Trueの場合は1つ見つけた段階で探索を終了する
        """
        self.__require_one_result = require_one_result

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
        result: list[Formula] = []

        return result
