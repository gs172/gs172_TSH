import pytest


@pytest.mark.parametrize("TSH,expected", [
    ([3.5, 3.6, 1.8, 2.8, 1.9, 3.4, 3, 3.6, 3, 4], "Normal Thyroid Function"),
    ([2.7, 1.4, 2.5, 3.1, 0.4, 1.8, 3.1, 3, 3.8, 0.9, 2.3], "Hyperthyroidism"),
    ([2.5, 1.1, 1.3, 2.7, 1.9, 2.6, 3.5, 1, 1.4], "Normal Thyroid Function"),
    ([6.3, 6.7, 6.3, 7.6, 2.1, 6.9, 7.1, 4.1, 7.2, 3.5], "Hypothyroidism"),
    ([2.8, 2.5, 0.7, 3.8, 2.7, 0.2, 2.9, 1.5, 0.8, 2.4, 2], "Hyperthyroidism"),
    ([2.4, 2.4, 3.5, 1.1, 3.9, 2, 3.7, 2.1, 3.9], "Normal Thyroid Function"),
    ([2.7, 5.2, 4.5, 3.3, 5.8, 2.4, 5.3, 4.2, 2.5, 5.2, 4], "Hypothyroidism"),
    ([0.6, 3.5, 0.2, 3.7, 1.1, 0.2, 3.5, 2.2, 1, 0.6, 3.5], "Hyperthyroidism"),
    ([3.1, 4.5, 3.5, 3.6, 5.6, 4.8, 4, 5.7, 4.2, 2.4, 5.5], "Hypothyroidism"),
    ([2, 2.6, 2.4, 2.2, 1, 1.4, 0.2, 0.5, 2, 2.3, 0.2], "Hyperthyroidism"),
    ])
def test_tachy(TSH, expected):
    """This is a unit test function that imports
    test_patient and separately tests 10 cases of
    TSH values"""
    from import1 import test_patient
    result = test_patient(TSH)
    assert result == expected
