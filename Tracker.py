import tkinter as tk
from tkinter import Text, simpledialog
import os

import time

##User Interface
root = tk.Tk()
canvas = tk.Canvas(root, height=100, width=300)
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
activityNum = "None"

## Manually input of activity code
def button_add():
    input_activity_code = activity_input.get()
    activityNum.config(text="Activity Code: " + input_activity_code)
    
    return None 


activity_inputs ={

}

activity_input = tk.Entry(frame, fg="white", bg = "grey")
activity_input.pack()

new_activity= tk.Button(frame, text = "Add new activity code",  padx=10, pady=5, fg="white", bg = "#263D42", command = button_add)
new_activity.pack()

activityNum = tk.Button(frame, text = "", padx=10, pady=5, fg="white", bg = "#263D42")
activityNum.pack()


## To track the state of each button (possible state is inactive or active)
activity_state_dict = {
    activityNum : "inactive"
}
## To track the cumulative time that has elapsed for each activity code
activity_time_elapsed_dict = {
    activityNum : 0.00
}

## To track the start time of the active activity session
activity_session_start_time_dict = {
    activityNum : 0.00
}

## Toggle Function
def toggle_timer(event):
    if activity_state_dict[activityNum] == "inactive":
        activity_state_dict[activityNum] = "active"
        print(activity_state_dict[activityNum])
        start_timer()
    elif activity_state_dict[activityNum] == "active":
        activity_state_dict[activityNum] = "inactive"
        print(activity_state_dict[activityNum])
        elapsed_timer()
        print(activity_time_elapsed_dict[activityNum])


    
def start_timer():
    startTime = time.time() 
    activity_session_start_time_dict[activityNum] = startTime
def elapsed_timer():
    stopTime = time.time()
    elapsedTime = stopTime - activity_session_start_time_dict[activityNum]
    activity_time_elapsed_dict[activityNum] = round((activity_time_elapsed_dict[activityNum] + elapsedTime), 2)


activityNum.bind('<Button-1>', toggle_timer)




root.mainloop()