"""
Core arithmetic and statistical helper functions for honorine-calcutils.
"""

from collections.abc import Sequence

def add(a: float, b: float) -> float:
    """Return the sum of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b

def multiply(a: float, b: float) -> float:
    """Return the product of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.
    """
    return a * b

def average(numbers: Sequence[float]) -> float:
    """Return the arithmetic mean of a sequence of numbers.

    Args:
        numbers: A sequence containing numeric values.

    Returns:
        The arithmetic mean of the values, or 0.0 if the sequence is empty.
    """
    if not numbers:
        return 0.0

    return sum(numbers) / len(numbers)