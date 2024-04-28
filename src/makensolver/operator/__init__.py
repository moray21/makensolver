from .binary import Divide, Exponentiate, Minus, Multiply, Plus
from .interface import Operator
from .unary import Factorial

# Arithmetic
PLUS = Plus()
MINUS = Minus()
MULTIPLY = Multiply()
DIVIDE = Divide()

EXP = Exponentiate()

FACTORIAL = Factorial()

# 演算子のリスト
UNARY: list[Operator] = [FACTORIAL]
ARITHMETIC_OPERATORS: list[Operator] = [
    PLUS,
    MINUS,
    MULTIPLY,
    DIVIDE,
]
OTHER_BINARY: list[Operator] = [EXP]
