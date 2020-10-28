def merge_concat_attached(*args):
    """Merging script with a simple concatenation, attached"""
    values = [str(v) for v in args if v is not None]
    separator = ""
    return separator.join(values)
