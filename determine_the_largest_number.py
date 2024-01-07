# Assignment #4 - Find and print the biggest number using only if-else statement
# Ask 3 user to input numbers
# locate the largest number among the 3

#pseudocode

import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import pyttsx3

def find_largest_number():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        num3 = float(entry_num3.get())

        largest_number = max(num1, num2, num3)

        result_label.config(text=f"Largest Number: {largest_number}")

        # Speak the result
        engine.say(f"The largest number is {largest_number}")
        engine.runAndWait()
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Find Largest Number")

# Set a background image
background_image = PhotoImage(file=r"c:\Users\RLF\OneDrive - Real LIFE Foundation, Inc\Pictures\Screenshots\color 2.png")
background_label = tk.Label(image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create and place widgets
label_num1 = ttk.Label(root, text="Enter Number 1:")
label_num1.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_num1 = ttk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = ttk.Label(root, text="Enter Number 2:")
label_num2.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_num2 = ttk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

label_num3 = ttk.Label(root, text="Enter Number 3:")
label_num3.grid(row=2, column=0, padx=10, pady=10, sticky="e")

entry_num3 = ttk.Entry(root)
entry_num3.grid(row=2, column=1, padx=10, pady=10)

find_button = ttk.Button(root, text="Find Largest Number", command=find_largest_number)
find_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Text-to-speech engine
engine = pyttsx3.init()

# Run the main loop
root.mainloop()
