import io
import sys
from unittest.mock import MagicMock, patch

from makensolver.solver import Solver


class TestSolver:
    def test_solve(self) -> None:
        """正しく解を探索し、順番も整理されていること"""
        available_numbers = [1, 2, 3]
        target = 3  # 1 2 3で8となるのは2つ

        solver = Solver(available_numbers, target)
        results = solver.solve()

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

        solver = Solver(available_numbers, target, require_one_result=True)
        results = solver.solve()

        assert isinstance(results, list)
        assert len(results) == 1

        # 1つ目
        res = results[0]
        assert res.answer == 3
        assert str(res) == "(2 - 1) * 3"

    def test_solve_with_timeout(self) -> None:
        """タイムアウトが機能すること"""
        available_numbers = [1, 2, 3]
        target = 3  # 1 2 3で8となるのは2つ
        timeout = 0.0

        normal_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            solver = Solver(
                available_numbers, target, timeout=timeout, require_one_result=True
            )
            results = solver.solve()

            assert (
                sys.stdout.getvalue()
                == "WARNING: timeout. solve have not completed yet.\n"
            )
            assert isinstance(results, list)
            assert len(results) == 0
        finally:
            sys.stdout = normal_stdout

    def test_solve_with_error(self) -> None:
        """タイムアウトが機能すること"""
        available_numbers = [1, 2, 3]
        target = 3  # 1 2 3で8となるのは2つ

        target = "makensolver.solver.Solver._Solver__exec_solve"
        with patch(target, MagicMock(side_effect=Exception)):
            try:
                solver = Solver(available_numbers, target)
                solver.solve()
            except SystemExit as e:
                assert e.code == 1
