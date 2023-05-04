import os
import string
import random
import win10toast
from time import sleep

import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x310")
app.resizable(False, False)
app.title("Screenshot URL Generator")

if not os.path.exists("out/"):
    os.mkdir("out/")

def generate_url():
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(2))
    result_dig = ''.join(random.choice(string.digits) for i in range(4))
    url = ("https://prnt.sc/"+ result_str + result_dig)
    print(url)
    text_1.insert("0.0", url + "\n")
    with open("Output.txt", "a") as  f:
        f.write(f'{url}\n')

def button_callback_2():
    os.startfile(os.getcwd() + "/out")

def show_value(value):
    rvalue = round(value).__str__()
    check_1.configure(text="Mass Generate (" + rvalue + ")")

frame_1 = customtkinter.CTkFrame(master=app, corner_radius=0)
frame_1.place(relheight=1.0, relwidth=0.5)
label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Screenshot URL Generator")
label_1.pack(pady=10, padx=10)

button_2 = customtkinter.CTkButton(master=frame_1, command=button_callback_2, text="Open Output folder")

check_1 = customtkinter.CTkCheckBox(master=frame_1, text="Mass Generate (10)")

slider_1 = customtkinter.CTkSlider(master=frame_1, from_=1, to=100000, command=show_value)
slider_1.set(10)

def button_callback():
    if check_1.get():
        for x in range(slider_1.get().__int__()):
            generate_url()
    else:
        generate_url()

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Generate")
button_1.pack(pady=10, padx=10, side="bottom")

button_2.pack(pady=0, padx=10, side="bottom")
check_1.pack(pady=10, padx=10, side="bottom")
slider_1.pack(pady=10, padx=10, side="bottom")

info_1 = customtkinter.CTkTextbox(master=frame_1, width=160, height=110)
info_1.pack(pady=0, padx=0)
info_1.insert("0.0", """Welcome to Screenshot
URL Generator. This program randomly generates
LightShot URLs for you to view. Not all will work, 
but most will.""")
info_1.configure(state='disabled')

text_1 = customtkinter.CTkTextbox(master=app, width=180, height=260, corner_radius=0)
text_1.pack(pady=0, padx=10, side="right")


app.mainloop()