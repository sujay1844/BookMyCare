data = {
	"data": [
		{
			"name": "John Doe",
			"timeslots": [
				"3:00PM",
				"4:00PM",
				"5:00PM"
			],
			"title": "General Physician"
		},
		{
			"name": "Jane Smith",
			"timeslots": [
				"2:00PM",
				"3:00PM",
				"4:00PM"
			],
			"title": "Pediatrician"
		},
		{
			"name": "Robert Johnson",
			"timeslots": [
				"9:00AM",
				"10:00AM",
				"11:00AM"
			],
			"title": "Orthopedic Surgeon"
		}
	]
}

from gtts import gTTS
import os
import subprocess

def speak_in_tts(text:str):
    tts = gTTS(text=text, lang='kn')
    filename = 'audio.mp3'
    tts.save(filename)
    subprocess.call(["ffplay", "-nodisp", "-autoexit", filename])
    os.remove(filename)
    
speak_in_tts("BookMyCare ಗೆ ಸುಸ್ವಾಗತ")
speak_in_tts("ದಯವಿಟ್ಟು ನಿಮ್ಮ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ")
ph_no = input()
if len(ph_no) != 10:
    speak_in_tts('ಅಮಾನ್ಯವಾದ ಫೋನ್ ಸಂಖ್ಯೆ')
    exit()
speak_in_tts("ಲಭ್ಯವಿರುವ ವೈದ್ಯರು:-")
idx = 1
for doctor in data['data']:
    speak_in_tts(f"{doctor['name']} ಗಾಗಿ {idx} ಒತ್ತಿರಿ")
    speak_in_tts(f"{doctor['name']} ಟೈಮ್‌ಸ್ಲಾಟ್‌ಗಳಲ್ಲಿ ಲಭ್ಯವಿದೆ:-")
    speak_in_tts(','.join(doctor['timeslots']))
    idx += 1
speak_in_tts("ವೈದ್ಯರ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ:-")
doctor_num = int(input())
if doctor_num > len(data['data']):
    speak_in_tts('ಅಮಾನ್ಯ ವೈದ್ಯರ ಸಂಖ್ಯೆ')
    exit()
doctor = data['data'][doctor_num-1]
idx = 1
for timeslot in doctor['timeslots']:
    speak_in_tts(f"Press {idx} for {timeslot}")
    idx += 1
speak_in_tts("Enter timeslot number:-")
timeslot_num = int(input())

if timeslot_num > len(doctor['timeslots']):
    speak_in_tts('ಅಮಾನ್ಯವಾದ ಟೈಮ್‌ಸ್ಲಾಟ್ ಸಂಖ್ಯೆ')
    exit()
timeslot = doctor['timeslots'][timeslot_num-1]

output = {
    'ph_no': ph_no,
    'doctor': doctor['name'],
    'timeslot': timeslot
}
print(output)
