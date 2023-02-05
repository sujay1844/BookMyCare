from tkinter import Tk, Frame, Button, Label, StringVar, Entry, CENTER, messagebox
from db_helpers import get_doc_data, get_patient_data
root = Tk()
root.configure(bg='#333')

welcome_label = Label(
    root,
    text="WELCOME TO BOOK MY CARE",
    bg='#333333', fg="#FF3399",
    font=("Cooper Black", 35)
)
welcome_label.place(anchor=CENTER, relx=.5, rely=.1)

username = StringVar()

page1_centre_frame = Frame(root, bg="#333")
page1_centre_frame.place(anchor=CENTER, relx=.5, rely=.5)

label_user = Label(
    page1_centre_frame,
    text="Username:",
    bg='#333', fg="#FFF",
    font=("Arial", 16),
    padx=10, pady=10
)
label_user.grid(row=0, column=0)

username_box = Entry(
    page1_centre_frame,
    textvariable=username,
    font=('Times', 12,'bold'),
    highlightcolor='green',
    highlightbackground='brown',
    bg='#FFEFE7'
)
username_box.grid(row=0, column=1)

def login(doctor_name:str):
    try:
        doctor = get_doc_data(doctor_name)
    except Exception as err:
        messagebox.showinfo('Error', str(err))
        return

    appointments = {}
    for timeslot in doctor['timeslots']:
        for ph_no in doctor['timeslots'][timeslot]:
            try:
                patient = get_patient_data(ph_no)
                if timeslot not in appointments:
                    appointments[timeslot] = []
                appointments[timeslot].append(patient['name'])
            except Exception as err:
                pass
    text = f"""
    Name: {doctor['name']}
    Title: {doctor['title']}
    Appointments:-
    """
    print(appointments)
    text2 = ""
    for timeslot, patients in appointments.items():
        text2 += f"{timeslot} {', '.join(patients)}\n"
    welcome_label.destroy()
    label_user.destroy()
    username_box.destroy()
    login_button.destroy()
    Label(root, text=text, bg='#333', fg='white', font=(20)).pack()
    Label(root, text=text2, bg='#333', fg='white').pack()
        
login_button = Button(
    page1_centre_frame,
    text="Login",
    command=lambda: login(username.get()),
    bg="#FF3399", fg="#FFFFFF",
    font=("Arial", 16),
    bd='5'
)
login_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
