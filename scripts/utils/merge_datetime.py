def merge_datetime(*args):
    """Merging script with a datetime concatenation"""
    values = [v for v in args if v is not None]
    return "T".join(values)
