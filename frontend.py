from gtts import gTTS
import os
import subprocess
import requests
import time

url = "http://127.0.0.1:5000"

os.system("python frontend_helpers.py & disown")

def speak_in_tts(text:str, lang:str):
    print(text)
    tts = gTTS(text=text, lang=lang)
    filename = 'audio.mp3'
    tts.save(filename)
    subprocess.call(["ffplay", "-nodisp", "-autoexit", "-v", "0", filename], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    os.remove(filename)

def take_input() -> int:
    while True:
        with open('inp.txt', 'r') as file:
            txt = file.read()
            if txt == "":
                time.sleep(0.01)
            else:
                x = int(txt)
                break
    with open('inp.txt', 'w') as file:
        file.write("")
    return x
    # return int(input())

def english():
    lang = 'en'

    headers = {'Content-Type': 'application/json'}

    # response = requests.post(url, json=query, headers=headers)
    response = requests.get(url+"/")

    if response.status_code == 200:
        data = response.json()
    else:
        speak_in_tts(f"Error {response.status_code}: {response.text}", lang)
        exit(1)

    while True:
        speak_in_tts("Enter your phone number", lang)
        ph_no = "".join([str(take_input()) for _ in range(10)])

        ph_no_spread = ", ".join([x for x in ph_no])
        speak_in_tts("The phone number you entered is " + ph_no_spread, lang)
        speak_in_tts("Press 1 to confirm", lang)
        speak_in_tts("Press 2 to retry", lang)
        inp = take_input()
        if inp == 2: continue

        if len(ph_no) != 10:
            speak_in_tts('Invalid phone number', lang)
            continue

        response = requests.post(url+"/validate-ph-no", json={'ph-no': ph_no}, headers=headers)
        if response.status_code != 200:
            speak_in_tts(f"Error {response.status_code}: {response.text}", lang)
            continue

        break

    while True:
        speak_in_tts("Choose doctors by speciality", lang)
        specialities = list(set([doctor['title'] for doctor in data['data']]))
        for idx, speciality in enumerate(specialities):
            speak_in_tts(f"Press {idx+1} for {speciality}", lang)
        inp = take_input()
        if inp > len(specialities):
            continue
        speciality = specialities[inp-1]
        doctors = [doctor for doctor in data['data'] if doctor['title'] == speciality]
        break

    while True:
        idx = 1
        for doctor in doctors:
            speak_in_tts(f"Press {idx} for {doctor['name']}", lang)
            idx += 1
        doctor_num = take_input()
        if doctor_num > len(data['data']):
            speak_in_tts('Invalid doctor number', lang)
            continue
        doctor = doctors[doctor_num-1]
        break

    while True:
        idx = 1
        for timeslot in doctor['timeslots']:
            speak_in_tts(f"Press {idx} for {timeslot}", lang)
            idx += 1
        timeslot_num = take_input()

        if timeslot_num > len(doctor['timeslots']):
            speak_in_tts('Invalid timeslot number', lang)
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
            speak_in_tts(response.text, lang)
        else:
            speak_in_tts(f"Error {response.status_code}: {response.text}", lang)
            continue

        break

def kannada():
    lang = 'kn'

    headers = {'Content-Type': 'application/json'}

    response = requests.get(url+"/")

    if response.status_code == 200:
        data = response.json()
    else:
        speak_in_tts(f"Error {response.status_code}: {response.text}", lang)
        exit(1)

    while True:
        speak_in_tts("ದಯವಿಟ್ಟು ನಿಮ್ಮ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ", lang)
        ph_no = "".join([str(take_input()) for _ in range(10)])

        ph_no_spread = ", ".join([x for x in ph_no])
        speak_in_tts("ನೀವು ನಮೂದಿಸಿದ ಫೋನ್ ಸಂಖ್ಯೆ " + ph_no_spread, lang)
        speak_in_tts("ದೃಢೀಕರಿಸಲು 1 ಒತ್ತಿರಿ", lang)
        speak_in_tts("ಮರುಪ್ರಯತ್ನಿಸಲು 2 ಒತ್ತಿರಿ", lang)
        inp = take_input()
        if inp == 2: continue

        if len(ph_no) != 10:
            speak_in_tts('ಅಮಾನ್ಯವಾದ ಫೋನ್ ಸಂಖ್ಯೆ', lang)
            continue

        response = requests.post(url+"/validate-ph-no", json={'ph-no': ph_no}, headers=headers)
        if response.status_code != 200:
            speak_in_tts(f"Error {response.status_code}: {response.text}", lang)
            continue

        break

    while True:
        speak_in_tts("ವಿಶೇಷತೆಯಿಂದ ವೈದ್ಯರನ್ನು ಆಯ್ಕೆ ಮಾಡಿ", lang)
        specialities = list(set([doctor['title'] for doctor in data['data']]))
        for idx, speciality in enumerate(specialities):
            speak_in_tts(f"{speciality} ಗಾಗಿ {idx+1} ಒತ್ತಿರಿ", lang)
        inp = take_input()
        if inp > len(specialities):
            continue
        speciality = specialities[inp-1]
        doctors = [doctor for doctor in data['data'] if doctor['title'] == speciality]
        break

    while True:
        idx = 1
        for doctor in doctors:
            speak_in_tts(f"{doctor['name']}ಗಾಗಿ {idx} ಒತ್ತಿರಿ", lang)
            idx += 1
        doctor_num = take_input()
        if doctor_num > len(data['data']):
            speak_in_tts('ಅಮಾನ್ಯ ವೈದ್ಯರ ಸಂಖ್ಯೆ', lang)
            continue
        doctor = doctors[doctor_num-1]
        break

    while True:
        idx = 1
        for timeslot in doctor['timeslots']:
            speak_in_tts(f"{timeslot}ಗಾಗಿ {idx} ಒತ್ತಿರಿ", lang)
            idx += 1
        timeslot_num = take_input()

        if timeslot_num > len(doctor['timeslots']):
            speak_in_tts('ಅಮಾನ್ಯವಾದ ಟೈಮ್‌ಸ್ಲಾಟ್ ಸಂಖ್ಯೆ', lang)
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
            speak_in_tts(response.text, lang)
        else:
            speak_in_tts(f"Error {response.status_code}: {response.text}", lang)
            continue

        break

speak_in_tts("Welcome to BookMyCare:-", 'en')
speak_in_tts("Press 1 for English", 'en')
speak_in_tts('ಕನ್ನಡಕ್ಕಾಗಿ 2 ಒತ್ತಿರಿ', 'kn')
if take_input() == 2:
    kannada()
else:
    english()
