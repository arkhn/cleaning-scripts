def merge_concat(*args):
    """Merging script with a simple concatenation, space-between"""
    values = [v for v in args if v is not None]
    separator = " "
    return separator.join(values)
