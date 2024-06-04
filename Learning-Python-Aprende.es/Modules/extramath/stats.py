def mean(*values: int | float) -> float:
    """Calculate mean of values"""
    return sum(values) / len(values)
