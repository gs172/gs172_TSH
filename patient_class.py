class Patient:

    def __init__(self, first, last, age, gender, diagnosis, TSH):
        self.first = first
        self.last = last
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.TSH = TSH

    def output_patient(self):
        print("First Name: "+str(self.first))
        print("Last Name: "+str(self.last))
        print("Age: "+str(self.age))
        print("Gender: "+str(self.gender))
        print("Diagnosis: "+str(self.diagnosis))
        print("TSH: "+str(self.TSH))


def create_patient(first, last, age, gender, diagnosis, TSH):
    new_patient = Patient(first, last, age, gender, diagnosis, TSH)
    return new_patient


def test_patient(first, last, age, gender, diagnosis, TSH):
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


if __name__ == "__main__":
	p1 = create_patient("Anne", "Boynton", "45", "Female",
																					"Normal Thyroid Function", [3.5, 3.6, 1.8, 2.8, 1.9, 3.4, 3, 3.6, 3, 4])
	p2 = create_patient("Kamal", "Solaiman", "31", "Male",
																					"Hyperthyroidism", [2.7, 1.4, 2.5, 3.1, 0.4, 1.8, 3.1, 3, 3.8, 0.9, 2.3])
	p3 = create_patient("Kyaw", "Win", "54", "Male",
																					"Normal Thyroid Function", [2.5, 1.1, 1.3, 2.7, 1.9, 2.6, 3.5, 1, 1.4])
	p4 = create_patient("Larissa", "Webb", "46", "Female",
																					"Hypothyroidism", [6.3, 6.7, 6.3, 7.6, 2.1, 6.9, 7.1, 4.1, 7.2, 3.5, 2.9])
	p5 = create_patient("Livia", "Villarroel", "62", "Female",
																					"Hyperthyroidism", [2.8, 2.5, 0.7, 3.8, 2.7, 0.2, 2.9, 1.5, 0.8, 2.4, 2])
	p6 = create_patient("Catherine", "Su", "44", "Female",
																					"Normal Thyroid Function", [2.4, 2.4, 3.5, 1.1, 3, 3.9, 2, 3.7, 2.1, 3.9])
	p7 = create_patient("Francisco", "Valle", "35", "Male",
																					"Hypothyroidism", [2.7, 5.2, 4.5, 3.3, 5.8, 2.4, 5.3, 4.2, 2.5, 5.2, 4])
	p8 = create_patient("Julian", "Thomson", "64", "Male",
																					"Hyperthyroidism", [0.6, 3.5, 0.2, 3.7, 1.1, 0.2, 3.5, 2.2, 1, 0.6, 3.5])
	p9 = create_patient("Monte", "Swarup", "51", "Male",
																					"Hypothyroidism", [3.1, 4.5, 3.5, 3.6, 5.6, 4.8, 4.3, 5.7, 4.2, 2.4, 5.5])
	p10 = create_patient("Jeffrey", "Bond", "77", "Male",
																						"Hyperthyroidism", [2, 2.6, 2.4, 2.2, 1, 1.4, 0.2, 0.5, 2, 2.3, 0.2])
	my_patients = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
	for i in range(len(my_patients)):
		my_patients[i].output_patient()


