from makensolver.operator.interface import BinaryOperator, Number


class Plus(BinaryOperator):
    def __str__(self) -> str:
        """
        str型で表示する際の記号
        """
        return "+"

    def __call__(self, x: Number, y: Number) -> Number:
        """
        演算子を用いて計算する(x 演算子 yの関係)

        Parameters
        ----------
        x: Number
            演算に使用する数値(前側)
        y: Number
            演算に使用する数値(後側)

        Returns
        -------
        : Number
        """
        return x + y

    def add_bracket(self, x: str, y: str) -> tuple[str, str]:
        """
        中置記法で表現する際に括弧が必要か計算に使用する前後の値から判断し、
        必要に応じて括弧を付与して返す

        Parameters
        ----------
        x: str
            演算に使用する数値(前側)
        y: str
            演算に使用する数値(後側)

        Returns
        -------
        bracket_x: str
            演算に使用する数値(前側), 括弧つき
        bracket_y: str
            演算に使用する数値(後側), 括弧つき

        Notes
        -----
        - 和算の場合、前後の値に依らず括弧は必要ない
        """
        return (x, y)
