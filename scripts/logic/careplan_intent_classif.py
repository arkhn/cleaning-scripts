from script.utils import is_empty

def classif_intent(input):
    """Classify careplan intent from validated protocols"""
    if is_empty(input):
        return 'proposal'
    if input==0:
        return 'plan'
    else if input==1:
        return 'order'  