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
    
speak_in_tts("Welcome to BookMyCare:-")
speak_in_tts("enter your phone number")
ph_no = input()
if len(ph_no) != 10:
    speak_in_tts('Invalid phone number')
    exit()
speak_in_tts("Available doctors:-")
idx = 1
for doctor in data['data']:
    speak_in_tts(f"Press {idx} for {doctor['name']}")
    speak_in_tts(f"{doctor['name']} is available at timeslots:-")
    speak_in_tts(','.join(doctor['timeslots']))
    idx += 1
speak_in_tts("Enter doctor number:-")
doctor_num = int(input())
if doctor_num > len(data['data']):
    speak_in_tts('Invalid doctor number')
    exit()
doctor = data['data'][doctor_num-1]
idx = 1
for timeslot in doctor['timeslots']:
    speak_in_tts(f"Press {idx} for {timeslot}")
    idx += 1
speak_in_tts("Enter timeslot number:-")
timeslot_num = int(input())

if timeslot_num > len(doctor['timeslots']):
    speak_in_tts('Invalid timeslot number')
    exit()
timeslot = doctor['timeslots'][timeslot_num-1]

output = {
    'ph_no': ph_no,
    'doctor': doctor['name'],
    'timeslot': timeslot
}
print(output)
