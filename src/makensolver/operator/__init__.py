from .binary import Divide, Minus, Multiply, Plus
from .interface import Operator

# Arithmetic
PLUS = Plus()
MINUS = Minus()
MULTIPLY = Multiply()
DIVIDE = Divide()

# 演算子のリスト
ARITHMETIC_OPERATORS: list[Operator] = [
    PLUS,
    MINUS,
    MULTIPLY,
    DIVIDE,
]
