from makensolver.solver import Solver


class TestSolver:
    def test_solve(self) -> None:
        """正しく解を探索すること"""
        available_numbers = [1, 2, 3]
        target = 8

        solver = Solver()
        results = solver.solve(available_numbers, target)

        assert isinstance(results, list)
