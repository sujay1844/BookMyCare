from loader import load, Datatype
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['bookmycare']
doctors_collection = db['doctors']
patients_collection = db['patients']

def get_doc_data(doctor_name:str) -> dict:

    query = {'name': doctor_name}

    results = doctors_collection.find(query)
    results_list = list(results)

    if len(results_list) == 0:
        raise ValueError("Doctor not found")
    else:
        return results_list[0]

def get_patient_data(ph_no:str) -> dict:

    query = {'ph_no': ph_no}

    results = patients_collection.find(query)
    results_list = list(results)

    if len(results_list) == 0:
        raise ValueError("Phone number not found")
    else:
        return results_list[0]

def get_all_doctors() -> list:
    results = doctors_collection.find({})
    results_list = list(results)
    new_results_list = []
    for result in results_list:
        if '_id' in result: del result['_id']
        result['timeslots'] = list(result['timeslots'].keys())
        new_results_list.append(result)
    return new_results_list


def update_patient(data:dict) -> None:
    
    query = {'ph_no': data['ph_no']}
    update = {
        '$push': {'appointments': [data['doctor'], data['timeslot']]}
    }

    result = patients_collection.update_one(query, update)
    print("modified", result.modified_count)
    if result.modified_count != 1:
        raise Exception("Patient data not updated")

def update_doctor(data:dict) -> None:
    query = {'name': data['doctor']}
    update = {
        '$push': {
            f"timeslots.{data['timeslot']}": data['ph_no']
        }
    }
    result = doctors_collection.update_one(query, update)
    if result.modified_count != 1:
        raise Exception("Doctor data not updated")

def add_doctor(doctor):
    doctors_collection.insert_one(doctor)

def add_patient(patient):
    patients_collection.insert_one(patient)

def _import_from_json():
    doctors_data = load('doctors.json', Datatype.DICT)
    for _, doctor in doctors_data.items():
        print(doctor)
        doctors_collection.insert_one(doctor)

    patients_data = load('patients.json', Datatype.DICT)
    for _, patient in patients_data.items():
        print(patient)
        patients_collection.insert_one(patient)

# print(get_doc_data("John Doe")['timeslots'])
# print(get_patient_data("9384738282")['appointments'])
