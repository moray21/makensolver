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
    --require_one_result: bool
        オプション
        結果が1つだけでいい場合はオプションを使用する
        デフォルトは全ての解を再帰的に探索する

    Example
    -------
    $ python main.py 1 3 3 4 -t 23
        available_numbers:  [1, 3, 3, 4]
        target:  23
        result:
            No.1: (3 + 3) * 4 - 1
            No.2: (3 + 3) * 4 - 1
            No.3: 4 * (3 + 3) - 1
            No.4: 4 * (3 + 3) - 1

    $ python main.py 1 3 3 4 -t 23 --require_one_result
        available_numbers:  [1, 3, 3, 4]
        target:  23
        result:
            No.1: (3 + 3) * 4 - 1
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("available_numbers", nargs="*", type=int)
    parser.add_argument("-t", "--target", type=int, default=10)
    parser.add_argument("--require_one_result", action="store_true")

    args = parser.parse_args()

    # 入力整理
    if len(args.available_numbers) == 0:
        raise ValueError("the number of available_numbers is required over 1.")
    print("available_numbers: ", args.available_numbers)
    print("target: ", args.target)

    # 解析
    solver = Solver(require_one_result=args.require_one_result)
    result = solver.solve(sorted(args.available_numbers), args.target)

    # 出力
    print("result: ")
    for i, res in enumerate(result):
        print(f"    No.{i+1}: {str(res)}")


if __name__ == "__main__":
    main()
