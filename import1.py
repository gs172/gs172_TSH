def import_data(txt):
    """This function reads in a txt file and selects
    every 4th line and returns them as name, age, gender and TSH"""
    name = []
    age = []
    gender = []
    TSH = []
    data = open(txt, 'r')
    data = [line[:-1] for line in data]
    for idx, val in enumerate(data):
        if idx % 4 == 0:
            name.append(val)
        elif idx % 4 == 1:
            age.append(val)
        elif idx % 4 == 2:
            gender.append(val)
        else:
            TSH.append(val)
    name.remove('END')
    age = [int(val) for val in age]
    TSH = TSH.split(',')
    TSH.remove('TSH')
    return name, age, gender, TSH


def test_patient(TSH):
    """This function gets rid of TSH string and performs
    TSH value testing to determine the diagnosis"""
    TSH = [float(val) for val in TSH]
    for line in TSH:
        if any(line < 1.0 for line in TSH):
            diagnosis = "Hyperthyroidism"
            break
        elif any(line > 4.0 for line in TSH):
            diagnosis = "Hypothyroidism"
            break
        elif any(line <= 4.0 and line >= 1.0 for line in TSH):
            diagnosis = "Normal Thyroid Function"
    return diagnosis


def create_patient(name, age, gender, TSH):
    """This function creates a patient file for one
    patient using the 4 returned inputs. This will be passed
    into the json file for each patient"""
    name = name.split(' ')
    Anne = {
        'First Name': name[0],
        'Last Name': name[1],
        'Age': age,
        'Gender': gender,
        'Diagnosis': test_patient(TSH),
        'TSH': TSH
    }
    return Anne


def create_multiple_patients(name, age, gender, TSH):
    """This function accounts for the previous function by
    appending the other patients info as an array of patients"""
    patient = []
    for name, age, gender, TSH in zip(name, age, gender, TSH):
        patient.append(create_patient(name, age, gender, TSH))
    return patient


def save_patient(patient):
    """This function creates and writes a json file for each
    patient, then closes the file"""
    out_file = open(patient['First Name'] + '-' +
                    patient['Last Name'] + '.json', 'w')
    import json
    json.dump(patient, out_file)
    out_file.close()
    return


def runcode():
    """This function runs the functions by reading the txtfile
    and saving the patient json files"""
    name, age, gender, TSH = import_data('test_data.txt')
    patient = create_multiple_patients(name, age, gender, TSH)
    for x in patient:
        save_patient(x)


if __name__ == "__main__":
    runcode()
