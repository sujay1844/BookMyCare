from book import book_appointment
from db_helpers import get_all_doctors, get_patient_data, get_doc_data, add_doctor, add_patient
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/book", methods=["POST"])
def book():
    data = request.get_json()
    try:
        book_appointment(data)
    except Exception as err:
        return str(err), 400
    return "Appointment was booked succesfully", 200

@app.route("/", methods=["GET"])
def get_doctors():
    return jsonify({"data": get_all_doctors()})

@app.route("/validate-ph-no", methods=["POST"])
def validate_ph_no():
    try:
        data = request.get_json()
        get_patient_data(data['ph-no'])
    except Exception as err:
        return str(err), 400
    return "Phone number is valid", 200

@app.route("/add/patient", methods=["POST"])
def add_patient_endpoint():
    try:
        data = request.get_json()
        add_patient(data)
    except Exception as err:
        return str(err), 400
    return "Patient added", 200

@app.route("/add/doctor", methods=["POST"])
def add_doctor_endpoint():
    try:
        data = request.get_json()
        add_doctor(data)
    except Exception as err:
        return str(err), 400
    return "Doctor added", 200

if __name__ == "__main__":
    app.run()
