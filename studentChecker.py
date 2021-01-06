import tkinter as tk
import pandas as pd
import numpy as np
import sys 
pd.set_option('mode.chained_assignment', None)

sys.stdout = open("TU103_attendance(1%)_Sep_9_checked.txt", "w")
# J:\My Drive\Master SIIT\Grader and TA\TU103\TU103.csv
# C:\Users\ACER\Desktop\TU108.csv
# Sep 9 attendance (1%) 1
# input dataframe

def get_data():
    global d, path, student_id
    p = path.get()
    d = pd.read_csv(str(p))
    message = "Input file completed!"
    tk.Label(window, text=message).grid(row=5, column=0) 
    path.config(state='disabled')
    d["ID"] = np.nan
    student_id = []
    for j in range(2, len(d.index)):
        x = d["Email Address"][j].split("@")
        d["ID"][j] = x[0]
        student_id.append(x[0])

# insert activity
def get_ac():
    global activity
    activity = str(ac.get())
    print("This checking is: "+ activity+"\n_____________________________________")
    message = "This checking is: "+ activity +"\n_____________________________________"
    tk.Label(window, text=message).grid(row=6, column=0) 
    ac.config(state='disabled')
    if activity not in d.columns: 
        d[activity] = np.nan
    
no_std = []
def add_check():
    global no_std 
    std = std_id.get()
    std = str(std)
    if std in student_id:
        index = student_id.index(std)
        print(d["First Name"][index+2] + " " + d["Last Name"][index+2] + " (ID "+str(d["ID"][index+2])+"): Checked")
        d[activity][index+2] = 0.5
        message = d["First Name"][index+2] + " " + d["Last Name"][index+2] + " (ID "+str(d["ID"][index+2])+"): Checked"
    else: 
        print("no "+std+ " id in the class")
        no_std.append(std)
        message = "No this ID "+ std+ " in the class"
    tk.Label(window, text=message).grid(row=7, column=0) 
    std_id.delete(0, tk.END)
    
window = tk.Tk()
window.geometry("500x200")
window.title("Student Checker")


tk.Label(window, text="File path").grid(row=0)
path = tk.Entry(window)
okButton = tk.Button(window, text="OK", command=get_data).grid(row=0, column=2)

tk.Label(window, text="Title of activity").grid(row=1)
ac = tk.Entry(window)
okButton = tk.Button(window, text="OK", command=get_ac).grid(row=1, column=2)

tk.Label(window, text="Student ID").grid(row=2)
std_id = tk.Entry(window)
checkButton = tk.Button(window, text='Check', command=add_check).grid(row=4, columnspan=2, pady=4)

path.grid(row=0, column=1)
ac.grid(row=1, column=1)
std_id.grid(row=2, column=1)

tk.mainloop()
d.to_csv("TU103_update.csv")
print("No these student ID: ", no_std)
sys.stdout.close()