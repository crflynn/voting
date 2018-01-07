"""Utility functions."""


def normalize(values):
    """Normalize a list of values."""
    total = sum(values)
    return [1.0 * value / total for value in values]
