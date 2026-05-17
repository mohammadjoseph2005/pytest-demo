"""
A robust calculator class with history and  error handing.
"""
from typing import List, Tuple, Union

Number = Union[int, float]


class Calculator:
    """A simple calculator with memory of operations."""

    def __init__(self) -> None:
        self._history: list[Tuple[str, Number, Number, Number]] = []

    def _validate_numbers(self, *args: Number) -> None:
        """
        Raise TypeError if any argument is not a number."""
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Expected number, got {type(arg).__name__}: {arg}")

    def add(self, a: Number, b: Number) -> Number:
        self._validate_numbers(a, b)
        result = a + b
        self._history.append(("add", a, b, result))
        return result

    def subtract(self, a: Number, b: Number) -> Number:
        self._validate_numbers(a, b)
        result = a - b
        self._history.append(("subtract", a, b, result))
        return result

    def multiply(self, a: Number, b: Number) -> Number:
        self._validate_numbers(a, b)
        result = a * b
        self._history.append(("multiply", a, b, result))
        return result

    def divide(self, a: Number, b: Number) -> float:
        self._validate_numbers(a, b)
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        result = a / b
        self._history.append(("divide", a, b, result))
        return result

    def power(self, base: Number, exp: Number) -> Number:
        self._validate_numbers(base, exp)
        result = base**exp
        self._history.append(("power", base, exp, result))
        return result

    def clear_history(self) -> None:
        self._history.clear()

    @property
    def history(self) -> List[Tuple[str, Number, Number, Number]]:
        """Return a copy of the history to prevent external modification."""
        return self._history.copy()

    def last_result(self) -> Union[Number, None]:
        """Return the result of the last operation, or None if no  history"""
        if self._history:
            return self._history[-1][3]
        return None
