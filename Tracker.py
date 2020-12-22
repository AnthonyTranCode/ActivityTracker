import tkinter as tk
from tkinter import Text, simpledialog
import os
import time

##User Interface
root = tk.Tk()
canvas = tk.Canvas(root, height=200, width=300)
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


def button_add():
    input_activity_code = activity_input.get()
    newButton = tk.Button(frame, text = input_activity_code, padx=10, pady=5, fg="white", bg = "#263D42")
    newButton.bind('<Button-1>', lambda event : toggle_timer(event, input_activity_code))
    newButton.pack()
    
    ## initialize dictionary for initial values
    activity_state_dict[input_activity_code] = "inactive"
    activity_session_start_time_dict[input_activity_code] = 0.00
    activity_time_elapsed_dict[input_activity_code] = 0.00
    return None 


## Manual input of activity code
activity_input = tk.Entry(frame, fg="white", bg = "grey")
activity_input.pack()

new_activity= tk.Button(frame, text = "Add new activity code",  padx=10, pady=5, fg="white", bg = "#263D42", command = button_add)
new_activity.pack()


## To track the state of each button (possible state is inactive or active)
activity_state_dict = {}

## To track the start time of the active activity session
activity_session_start_time_dict = {}

## To track the cumulative time that has elapsed for each activity code
activity_time_elapsed_dict = {}


## Toggle function for each button
def toggle_timer(event, activity_code):
    if activity_state_dict[activity_code] == "inactive":
        activity_state_dict[activity_code] = "active"
        print(activity_state_dict[activity_code])
        start_timer(activity_code)
    elif activity_state_dict[activity_code] == "active":
        activity_state_dict[activity_code] = "inactive"
        print(activity_state_dict[activity_code])
        elapsed_timer(activity_code)
        print(activity_time_elapsed_dict[activity_code])


## To initiate the timer for each activity code    
def start_timer(activity_code):
    startTime = time.time() 
    activity_session_start_time_dict[activity_code] = startTime
def elapsed_timer(activity_code):
    stopTime = time.time()
    elapsedTime = stopTime - activity_session_start_time_dict[activity_code]
    activity_time_elapsed_dict[activity_code] = round((activity_time_elapsed_dict[activity_code] + elapsedTime), 2)


root.mainloop()