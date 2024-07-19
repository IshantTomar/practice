from customtkinter import *
import random

app = CTk()
choices = ["Rock", "Paper", "Scissors"]

def rock():
    test = random.choice(choices)
    label_player.configure(text="You: Rock")
    label_comp.configure(text=f"Computer: {test}")
    if test == "Scissors":
        label.configure(text="You Won!", text_color="LightBlue")
    elif test == "Paper":
        label.configure(text="You Lost.", text_color="Red")
    else:
        label.configure(text="Tied!", text_color="Yellow")

def paper():
    test = random.choice(choices)
    label_player.configure(text="You: Paper")
    label_comp.configure(text=f"Computer: {test}")
    if test == "Rock":
        label.configure(text="You Won!", text_color="LightBlue")
    elif test == "Scissors":
        label.configure(text="You Lost.", text_color="Red")
    else:
        label.configure(text="Tied!", text_color="Yellow")

def scissors():
    test = random.choice(choices)
    label_player.configure(text="You: Scissors")
    label_comp.configure(text=f"Computer: {test}")
    if test == "Paper":
        label.configure(text="You Won!", text_color="LightBlue")
    elif test == "Rock":
        label.configure(text="You Lost.", text_color="Red")
    else:
        label.configure(text="Tied!", text_color="Yellow")


rock_button = CTkButton(app, text="Rock", font=("Arial",20), width=150, border_width=2, corner_radius=10, command=rock)
rock_button.grid(row=1,column=0)
paper_button = CTkButton(app, text="Paper", font=("Arial",20), width=150, border_width=2, corner_radius=10, command=paper)
paper_button.grid(row=1,column=1)
scissors_button = CTkButton(app, text="Scissors", font=("Arial",20), width=150, border_width=2, corner_radius=10, command=scissors)
scissors_button.grid(row=1,column=2)
label = CTkLabel(app, text="", font=("Arial",20))
label.grid(row=0,columnspan=3)
label_player = CTkLabel(app, text="You: ", font=("Arial",20))
label_player.grid(row=3,columnspan=3)
label_comp = CTkLabel(app, text="Computer: ", font=("Arial",20))
label_comp.grid(row=4,columnspan=3)

app.mainloop()

