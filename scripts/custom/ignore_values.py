from scripts import utils


def ignore_values(raw_input):
    """ Ignore values
    """
    if utils.is_empty(raw_input):
        return None

    values = [
        "UMLS:C0439673",  # code unknown
        "C0439673",  # code unknown
        "UMLS:C1272460",  # code not applicable
        "C1272460",  # code not applicable
    ]
    if raw_input in values:
        return None
    else:
        return raw_input
