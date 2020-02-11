def merge_concat(*args):
    """Merging script with a simple concatenation"""
    values = [v for v in args if v is not None]
    return " ".join(values)
