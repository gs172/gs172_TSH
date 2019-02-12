def test_patient(TSH):
    TSH = [float(i) for i in TSH]
    if any(line < 1.0 for line in TSH):
        diagnosis = "Hyperthyroidism"
        return diagnosis
    elif any(line > 4.0 for line in TSH):
        diagnosis = "Hypothyroidism"
        return diagnosis
    elif any(line <= 4.0 and line >= 1.0 for line in TSH):
        diagnosis = "Normal Thyroid Function"
        return diagnosis
