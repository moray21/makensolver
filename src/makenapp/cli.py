import argparse

from makensolver.solver import Solver


def main() -> None:
    """
    入力した数字を並び替え、目標の数字をつくる計算式を探す

    Parameters
    ----------
    available_numbers: list[int]
        使用する数字のリスト
        (例) [1, 2, 3]の3つで目標の数字をつくるということ
    target: int
        作成する数字
    --timeout: float
        タイムアウト時間(単位: 秒)
        タイムアウトするまでに探索された結果を返す
    --require_one_result: bool
        オプション
        結果が1つだけでいい場合はオプションを使用する
        デフォルトは全ての解を再帰的に探索する
    --special
        オプション
        四則演算以外も許可する

    Example
    -------
    $ python main.py 1 1 3 4 -t 10
    available_numbers:  [1, 1, 3, 4]
    target:  10
    result:
        No.1: (1 + 1) * 3 + 4
        No.2: 1 + 3 * (4 - 1)
        No.3: 1 - (1 - 4) * 3

    $ python main.py 1 1 3 4 -t 10 --require_one_result
    available_numbers:  [1, 1, 3, 4]
    target:  10
    result:
        No.1: (1 + 1) * 3 + 4

    $ python main.py 1 1 3 4 -t 23 --special
    available_numbers:  [1, 1, 3, 4]
    target:  23
    WARNING: timeout. solve have not completed yet.
    result:
        No.1: 1 + 1 - 3 + 4 !
        No.2: 1 + 1 - (3 - 4 !)
        No.3: (1 + 3) ! - 1 ^ 4
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("available_numbers", nargs="*", type=int)
    parser.add_argument("-t", "--target", type=int, default=10)
    parser.add_argument("--timeout", default=10, type=float)
    parser.add_argument("--require_one_result", action="store_true")
    parser.add_argument("--special", action="store_true")

    args = parser.parse_args()

    # 入力整理
    if len(args.available_numbers) == 0:
        raise ValueError("the number of available_numbers is required over 1.")
    print("available_numbers: ", args.available_numbers)
    print("target: ", args.target)

    # 解析
    solver = Solver(
        sorted(args.available_numbers),
        args.target,
        timeout=args.timeout,
        require_one_result=args.require_one_result,
        is_special_rule=args.special,
    )
    result = solver.solve()

    # 出力
    print("result: ")
    for i, res in enumerate(result):
        print(f"    No.{i+1}: {str(res)}")


if __name__ == "__main__":
    main()
