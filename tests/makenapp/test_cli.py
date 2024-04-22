import io

import pytest
from makenapp.cli import main


def test_with_empty_input(monkeypatch) -> None:
    """使用可能な数字を指定しないとエラー"""
    argv = ["cli.py"]

    with monkeypatch.context() as m:
        m.setattr("sys.argv", argv)
        with pytest.raises(ValueError):
            main()


def test_result_print(monkeypatch) -> None:
    """結果が正しく表示されること"""
    argv = ["cli.py", "1", "2", "3", "-t", "8"]
    stdout = io.StringIO()

    expected_print = "available_numbers:  [1, 2, 3]\n"
    expected_print += "target:  8\n"
    expected_print += "result: \n"

    # 1,2,3では7はつくれない
    with monkeypatch.context() as m:
        m.setattr("sys.argv", argv)
        m.setattr("sys.stdout", stdout)
        main()

        assert stdout.getvalue() == expected_print
