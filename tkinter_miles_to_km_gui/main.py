from tkinter import *


def calculate():
    input_text = input_field.get()
    miles_to_km = int(input_text) * 1.60934

    output_label.config(text=miles_to_km)


# Window
window = Tk()
window.title("Miles to Km Converter GUI")
window.minsize(width=500, height=300)
window.config(padx=60, pady=80)

# Input field
input_field = Entry(width=30)
input_field.grid(column=1, row=0)

# Output Label
output_label = Label(text="0", font=("Arial", 12, "bold"))
output_label.grid(column=1, row=1)

# Calculate Button
calc_button = Button(text="Calculate", command=calculate)

# Label - Miles
miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

# Label - Is equal to
equals_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equals_label.grid(column=0, row=1)

# Label - Km
km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

window.mainloop()
