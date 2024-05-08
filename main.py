from tkinter import *
import random

pscore = 0
cscore = 0

RSP = {1: {"photo": "rock.png", "color": 'deep sky blue'},
       2: {"photo": "paper.png", "color": 'yellow'},
       3: {"photo": "scissors.png", "color": "red"}
       }


def trigger(a):
    global cscore, pscore
    b = random.randint(1, 3)
    image = PhotoImage(file=RSP[b]["photo"])
    choice_card.config(image=image, bg=RSP[b]["color"], borderwidth=20)
    choice_card.image = image
    if a == 1 and b != 1:
        if b == 2:
            cscore += 1
        elif b == 3:
            pscore += 1
    elif a == 2 and b != 2:
        if b == 1:
            pscore += 1
        elif b == 3:
            cscore += 1
    elif a == 3 and b != 3:
        if b == 2:
            pscore += 1
        elif b == 1:
            cscore += 1
    score.config(text=f"Your Score : {pscore}\t\t\tCPU Score : {cscore}")


def reset():
    global pscore, cscore
    pscore=cscore=0
    score.config(text=f"Your Score : {pscore}\t\t\tCPU Score : {cscore}")

screen = Tk()
screen.title("Rock-Paper_Scissors")
screen.geometry("1280x1000")

#images
rock = PhotoImage(file='rock.png')
paper = PhotoImage(file='paper.png')
scissors = PhotoImage(file='scissors.png')
userimg = PhotoImage(file='user.png')
cpuimg = PhotoImage(file='robot.png')
resetimg= PhotoImage(file='reset.png')
# label
score = Label(text=f"Your Score : {pscore}\t\t\tCPU Score : {cscore}", height=2, width=48,
              font=('Helvetica', 25, 'bold'), bg='spring green', borderwidth=20, border=20)
score.grid(column=1, row=1, columnspan=5)

user = Label(image=userimg)
user.grid(column=0, row=0)

cpu = Label(image=cpuimg)
cpu.grid(column=0, row=2)

# Buttons
rock_button = Button(height=300, width=280, borderwidth=20, text="Rock", bg='deep sky blue', command=lambda: trigger(1))
rock_button.config(image=rock)
rock_button.grid(column=1, row=0)

paper_button = Button(height=300, width=280, borderwidth=20, text="Paper", bg='yellow', command=lambda: trigger(2))
paper_button.config(image=paper)
paper_button.grid(column=2, row=0)

scissors_button = Button(height=300, width=280, borderwidth=20, text="Scissors", bg='red', command=lambda: trigger(3))
scissors_button.config(image=scissors)
scissors_button.grid(column=3, row=0)

reset=Button(height=100, width=250, image=resetimg, borderwidth=20, command=reset)
reset.grid(column=0, row=1)
# cpu_label
choice_card = Label(text="Random")
image = PhotoImage(file='allrps.png')
choice_card['image'] = image
choice_card.grid(column=1, row=2, rowspan=2, columnspan=3)

screen.mainloop()
