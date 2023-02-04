MAX_NUM = 10

# data = {
#     'ph_no': '9384729384',
#     'doctor': 'John Doe',
#     'timeslot': '5:00PM'
# }

from db_helpers import get_doc_data, get_patient_data, update_doctor, update_patient

def book_appointment(data:dict|None) -> (Exception | None):
    if data is None:
        raise Exception('Invalid data')

    update = [data['doctor'], data['timeslot']]

    patient_data = get_patient_data(data['ph_no'])
    doctor_data = get_doc_data(data['doctor'])

    if data['timeslot'] not in doctor_data['timeslots']:
        raise Exception('Timeslot not found')

    phs = doctor_data['timeslots'][data['timeslot']]
    appointments = patient_data['appointments']

    if len(phs) > MAX_NUM:
        raise Exception('Doctor is not available at given timeslot anymore.')

    if data['ph_no'] in phs or update in appointments:
        raise Exception('Appointment has already been booked')
        
    update_patient(data)
    update_doctor(data)
