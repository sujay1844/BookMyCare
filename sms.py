from gtts import gTTS
import os
import subprocess
import requests
import time

url = "http://127.0.0.1:5000"

os.system("python frontend_helpers.py & disown")

def english():
    lang = 'en'

    headers = {'Content-Type': 'application/json'}

    # response = requests.post(url, json=query, headers=headers)
    response = requests.get(url+"/")

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error {response.status_code}: {response.text}", lang)
        exit(1)

    while True:
        print("Enter your phone number", lang)
        ph_no = "".join([input() for _ in range(10)])

        ph_no_spread = ", ".join([x for x in ph_no])
        print("The phone number you entered is " + ph_no_spread, lang)
        print("Press 1 to confirm", lang)
        print("Press 2 to retry", lang)
        inp = int(input())
        if inp == 2: continue

        if len(ph_no) != 10:
            print('Invalid phone number', lang)
            continue

        response = requests.post(url+"/validate-ph-no", json={'ph-no': ph_no}, headers=headers)
        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}", lang)
            continue

        break

    while True:
        print("Choose doctors by speciality", lang)
        specialities = list(set([doctor['title'] for doctor in data['data']]))
        for idx, speciality in enumerate(specialities):
            print(f"Press {idx+1} for {speciality}", lang)
        inp = int(input())
        if inp > len(specialities):
            continue
        speciality = specialities[inp-1]
        doctors = [doctor for doctor in data['data'] if doctor['title'] == speciality]
        break

    while True:
        idx = 1
        for doctor in doctors:
            print(f"Press {idx} for {doctor['name']}", lang)
            idx += 1
        doctor_num = int(input())
        if doctor_num > len(data['data']):
            print('Invalid doctor number', lang)
            continue
        doctor = doctors[doctor_num-1]
        break

    while True:
        idx = 1
        for timeslot in doctor['timeslots']:
            print(f"Press {idx} for {timeslot}", lang)
            idx += 1
        timeslot_num = int(input())

        if timeslot_num > len(doctor['timeslots']):
            print('Invalid timeslot number', lang)
            continue
        timeslot = doctor['timeslots'][timeslot_num-1]

        output = {
            'ph_no': ph_no,
            'doctor': doctor['name'],
            'timeslot': timeslot
        }
        print(output)

        query = {
            "ph_no": ph_no,
            "doctor": doctor['name'],
            "timeslot": timeslot
        }
        headers = {'Content-Type': 'application/json'}

        response = requests.post(url+"/book", json=query, headers=headers)

        if response.status_code == 200:
            print(response.text, lang)
        else:
            print(f"Error {response.status_code}: {response.text}", lang)
            continue

        break

def kannada():
    lang = 'kn'

    headers = {'Content-Type': 'application/json'}

    response = requests.get(url+"/")

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error {response.status_code}: {response.text}", lang)
        exit(1)

    while True:
        print("ದಯವಿಟ್ಟು ನಿಮ್ಮ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ", lang)
        ph_no = "".join([input() for _ in range(10)])

        ph_no_spread = ", ".join([x for x in ph_no])
        print("ನೀವು ನಮೂದಿಸಿದ ಫೋನ್ ಸಂಖ್ಯೆ " + ph_no_spread, lang)
        print("ದೃಢೀಕರಿಸಲು 1 ಒತ್ತಿರಿ", lang)
        print("ಮರುಪ್ರಯತ್ನಿಸಲು 2 ಒತ್ತಿರಿ", lang)
        inp = int(input())
        if inp == 2: continue

        if len(ph_no) != 10:
            print('ಅಮಾನ್ಯವಾದ ಫೋನ್ ಸಂಖ್ಯೆ', lang)
            continue

        response = requests.post(url+"/validate-ph-no", json={'ph-no': ph_no}, headers=headers)
        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}", lang)
            continue

        break

    while True:
        print("ವಿಶೇಷತೆಯಿಂದ ವೈದ್ಯರನ್ನು ಆಯ್ಕೆ ಮಾಡಿ", lang)
        specialities = list(set([doctor['title'] for doctor in data['data']]))
        for idx, speciality in enumerate(specialities):
            print(f"{speciality} ಗಾಗಿ {idx+1} ಒತ್ತಿರಿ", lang)
        inp = int(input())
        if inp > len(specialities):
            continue
        speciality = specialities[inp-1]
        doctors = [doctor for doctor in data['data'] if doctor['title'] == speciality]
        break

    while True:
        idx = 1
        for doctor in doctors:
            print(f"{doctor['name']}ಗಾಗಿ {idx} ಒತ್ತಿರಿ", lang)
            idx += 1
        doctor_num = int(input())
        if doctor_num > len(data['data']):
            print('ಅಮಾನ್ಯ ವೈದ್ಯರ ಸಂಖ್ಯೆ', lang)
            continue
        doctor = doctors[doctor_num-1]
        break

    while True:
        idx = 1
        for timeslot in doctor['timeslots']:
            print(f"{timeslot}ಗಾಗಿ {idx} ಒತ್ತಿರಿ", lang)
            idx += 1
        timeslot_num = int(input())

        if timeslot_num > len(doctor['timeslots']):
            print('ಅಮಾನ್ಯವಾದ ಟೈಮ್‌ಸ್ಲಾಟ್ ಸಂಖ್ಯೆ', lang)
            continue
        timeslot = doctor['timeslots'][timeslot_num-1]

        output = {
            'ph_no': ph_no,
            'doctor': doctor['name'],
            'timeslot': timeslot
        }
        print(output)

        query = {
            "ph_no": ph_no,
            "doctor": doctor['name'],
            "timeslot": timeslot
        }
        headers = {'Content-Type': 'application/json'}

        response = requests.post(url+"/book", json=query, headers=headers)

        if response.status_code == 200:
            print(response.text, lang)
        else:
            print(f"Error {response.status_code}: {response.text}", lang)
            continue

        break

print("Welcome to BookMyCare:-", 'en')
print("Press 1 for English", 'en')
print('ಕನ್ನಡಕ್ಕಾಗಿ 2 ಒತ್ತಿರಿ', 'kn')
if int(input()) == 2:
    kannada()
else:
    english()
