from makensolver.solver import Solver


class TestSolver:
    def test_solve(self) -> None:
        """正しく解を探索し、順番も整理されていること"""
        available_numbers = [1, 2, 3]
        target = 3  # 1 2 3で8となるのは2つ

        solver = Solver()
        results = solver.solve(available_numbers, target)

        assert isinstance(results, list)
        assert len(results) == 2

        # 1つ目
        res = results[0]
        assert res.answer == 3
        assert str(res) == "(2 - 1) * 3"

        # 2つ目
        res = results[1]
        assert res.answer == 3
        assert str(res) == "3 / (2 - 1)"

    def test_solve_with_require_one_result(self) -> None:
        """1つの解を返すこと"""
        available_numbers = [1, 2, 3]
        target = 3  # 1 2 3で8となるのは2つ

        solver = Solver(require_one_result=True)
        results = solver.solve(available_numbers, target)

        assert isinstance(results, list)
        assert len(results) == 1

        # 1つ目
        res = results[0]
        assert res.answer == 3
        assert str(res) == "(2 - 1) * 3"
