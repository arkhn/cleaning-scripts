def clean_osiris_ALLCODES(raw_input):
    if raw_input is None:
        return None
    return (
        raw_input.replace("UMLS:", "")
        .replace("RECIST:", "")
        .replace("HL7:", "")
        .replace("UMLS:", "")
        .replace("LOINC:", "")
        .replace("ATC:", "")
        .replace("MedDRA:", "")
    )
