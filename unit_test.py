import pytest


@pytest.mark.parametrize("first,last,age,gender,expected,a", [
    ("Anne", "Boynton", "45", "Female", "Normal Thyroid Function",
        [3.5, 3.6, 1.8, 2.8, 1.9, 3.4, 3, 3.6, 3, 4]),
    ("Kamal", "Solaiman", "31", "Male", "Hyperthyroidism",
        [2.7, 1.4, 2.5, 3.1, 0.4, 1.8, 3.1, 3, 3.8, 0.9, 2.3]),
    ("Kyaw", "Win", "54", "Male", "Normal Thyroid Function",
        [2.5, 1.1, 1.3, 2.7, 1.9, 2.6, 3.5, 1, 1.4]),
    ("Larissa", "Webb", "46", "Female", "Hypothyroidism",
        [6.3, 6.7, 6.3, 7.6, 2.1, 6.9, 7.1, 4.1, 7.2, 3.5, 2.9]),
    ("Livia", "Villarroel", "62", "Female", "Hyperthyroidism",
        [2.8, 2.5, 0.7, 3.8, 2.7, 0.2, 2.9, 1.5, 0.8, 2.4, 2]),
    ("Catherine", "Su", "44", "Female", "Normal Thyroid Function",
        [2.4, 2.4, 3.5, 1.1, 3, 3.9, 2, 3.7, 2.1, 3.9]),
    ("Francisco", "Valle", "35", "Male", "Hypothyroidism",
        [2.7, 5.2, 4.5, 3.3, 5.8, 2.4, 5.3, 4.2, 2.5, 5.2, 4]),
    ("Julian", "Thomson", "64", "Male", "Hyperthyroidism",
        [0.6, 3.5, 0.2, 3.7, 1.1, 0.2, 3.5, 2.2, 1, 0.6, 3.5]),
    ("Monte", "Swarup", "51", "Male", "Hypothyroidism",
        [3.1, 4.5, 3.5, 3.6, 5.6, 4.8, 4.3, 5.7, 4.2, 2.4, 5.5]),
    ("Jeffrey", "Bond", "77", "Male", "Hyperthyroidism",
        [2, 2.6, 2.4, 2.2, 1, 1.4, 0.2, 0.5, 2, 2.3, 0.2]),
    ])
def test_TSH(first, last, age, gender, expected, a):
    from patient_class import test_patient
    result = test_patient(first, last, age, gender, expected, a)
    assert result == expected
