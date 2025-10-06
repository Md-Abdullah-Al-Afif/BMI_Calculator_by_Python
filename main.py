from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("BMI CALCULATOR")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")

def calculate_bmi():
    try:
        h = float(Height.get())
        w = float(Weight.get())
        m = h / 100  # Convert height into meters
        bmi = round(float(w / m ** 2), 1)
        labl1.config(text=bmi)

        if bmi <= 18.5:
            labl2.config(text="Underweight !")
            labl3.config(text="You are in the Underweight category \n based on your BMI .")
        elif 18.5 < bmi <= 25:
            labl2.config(text="Normal !")
            labl3.config(text="You are in the Normal category \n based on your BMI .")
        elif 25 < bmi <= 30:
            labl2.config(text="Overweight !")
            labl3.config(text="You are in the Overweight category \n based on your BMI .")
        else:
            labl2.config(text="Obese !")
            labl3.config(text="You are in the Obese category \n based on your BMI .")
    except ValueError:
        labl1.config(text="Error !")
        labl2.config(text="Invalid input !")
        labl3.config(text="Please enter valid height and weight.")

# Icon
image_icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False, image_icon)

# Top image
top = PhotoImage(file="Images/top.png")
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(x=-10, y=-10)

# Bottom box
Label(root, width=72, height=18, bg="lightblue").pack(side=BOTTOM)

# Two boxes
box = PhotoImage(file="Images/box.png")
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)

# Scale image
scale = PhotoImage(file="Images/scale.png")
Label(root, image=scale, bg="lightblue").place(x=20, y=310)

# Slider 1 (for height)
current_value = tk.DoubleVar()

def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed_height(_):
    Height.set(get_current_value())
    size = int(float(get_current_value()))
    img = Image.open("Images/man.png")
    resized_image = img.resize((50, 10 + size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.configure(image=photo2)
    secondimage.image = photo2  # Keep a reference to avoid garbage collection
    secondimage.place(x=70, y=550 - size)

style = ttk.Style()
style.configure("TScale", background="white")

slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale",
                   command=slider_changed_height, variable=current_value)
slider.place(x=80, y=250)

# Slider 2 (for weight)
current_value2 = tk.DoubleVar()

def get_current_value2():
    return '{:.2f}'.format(current_value2.get())

def slider_changed_weight(_):
    Weight.set(get_current_value2())

slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale",
                    command=slider_changed_weight, variable=current_value2)
slider2.place(x=300, y=250)

# Entry boxes
Height = StringVar()
Weight = StringVar()

height_label = Label(root, text="Height (in centimeters)", font='arial 8', bg="#fff", fg="#000")
height_label.place(x=45, y=130)

weight_label = Label(root, text="Weight (in KG)", font='arial 8', bg="#fff", fg="#000")
weight_label.place(x=265, y=130)

height = Entry(root, textvariable=Height, width=6, font='arial 40', bg="#fff", fg="#000", bd=0, justify=CENTER)
height.place(x=45, y=150)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width=6, font='arial 40', bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=265, y=150)
Weight.set(get_current_value2())

# Man image
secondimage = Label(root, bg="lightblue")
secondimage.place(x=70, y=530)

# Button
Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white", command=calculate_bmi).place(x=280, y=340)

# Labels for BMI result
labl1 = Label(root, font="arial 30 bold", bg="lightblue", fg="black")
labl1.place(x=145, y=325)

labl2 = Label(root, font="arial 20 bold", bg="lightblue", fg="black")
labl2.place(x=200, y=430)

labl3 = Label(root, font="arial 10", bg="lightblue", fg="black")
labl3.place(x=200, y=500)

root.mainloop()
