from tkinter import *


# button function to caalulate the miles
def calculate():
    kilometers = round(int(m_input.get()) * 1.609, 2)
    cal_label.config(text=kilometers)


# window initialization
window = Tk()
window.title("Miles to Kilometers converter")
window.minsize(width=350, height=220)
font = ("Ariel", 15, "normal")

# miles label
miles_label = Label(text="Enter miles: ", font=font)
miles_label.place(x=40, y=50)

# input
m_input = Entry(width=10)
m_input.place(x=154, y=57)

# labels
iet_label = Label(text="is equal to ", font=font)
iet_label.place(x=40, y=80)

cal_label = Label(text="0", font=font)
cal_label.place(x=150, y=80)

k_label = Label(text="Kilometers", font=font)
k_label.place(x=230, y=80)

# button
c_button = Button(text="Calculate", command=calculate)
c_button.place(x=150, y=110)

window.mainloop()
