from tkinter import *
import random
from PIL import Image, ImageTk

root=Tk()
root.configure(background="#403F6F")



you_sum=0
comp_sum=0
def start(i=0):
    global liste1,w3
    liste1 = ["rock", "paper", "scissors"]
    b4.grid_remove()




    w3.config(text="Choice one:")
    w3.grid(row=1, column=1)

    if i < len(liste1):  # Listenin sınırını kontrol et
        w3.config(text=liste1[i])  # i. elemanı yazdır
        root.after(1000, lambda: start(i + 1))  # 1 saniye sonra tekrar çağır
    else:
        w3.config(text="Choice one") # Döngü bittiğinde label'ı temizle


        b1 = Button(root, text='Rock',command=lambda:buttons("rock"))
        b2 = Button(root, text='Paper',command=lambda:buttons("paper"))
        b3 = Button(root, text='Scissors',command=lambda:buttons("scissors"))

        b1.grid(row=2, column=0)
        b2.grid(row=2, column=1)
        b3.grid(row=2, column=2)

def buttons(your_choice):

    buttons_disabled()
    computer()


    w4.config(text="Your choice:"+your_choice)
    w5.config(text="Computer's choice:" + computer_cho)



    if your_choice=="rock" :
        if computer_cho=="rock":
            printer("Draw")
        elif computer_cho=="paper":
            printer("Computer won")
        else :
            printer("You won")
    elif your_choice=="paper" :
        if computer_cho=="rock":
            printer("You won")
        elif computer_cho=="paper":
            printer("Draw")
        else :
            printer("Computer won")
    else:
        if computer_cho=="rock":
            printer("Computer won")
        elif computer_cho=="paper":
            printer("You won")
        else :
            printer("Draw")




def printer(value):
    global you_sum,comp_sum,b5
    you = 0
    comp = 0

    w3.config(text=value)

    if value == "You won":
        you+=1
        you_sum+=you

    elif value== "Computer won":
        comp+=1
        comp_sum+=comp
    else:
        you+=1
        comp+=1
        you_sum+=you
        comp_sum+=comp
    w1.config(text="Score:"+str(you_sum)+"/"+str(comp_sum))

    if you_sum==3:
        winner("You")
    elif comp_sum==3:
        winner("Computer")
    elif you_sum==3 and comp_sum==3:
        winner("Both team")
    else:
        b5.config(text="Try again",command=start, state=NORMAL)






def computer():

    global computer_cho
    computer_cho =random.choice(liste1)



def winner(team):
    global you_sum,comp_sum
    w3.config(text="{} won the game.".format(team))
    you_sum=0
    comp_sum=0
    b5.config(text='Play Again', command=lambda:[change_button(),change_label(),start()])  # Yeni oyun başlatmak için buton


def change_label():
    w1.config(text="Score:0/0")
def change_button():
    b5.config(text="Try again",command=start)


def buttons_disabled():
    b1 = Button(root, text='Rock', state=DISABLED)
    b2 = Button(root, text='Paper', state=DISABLED)
    b3 = Button(root, text='Scissors', state=DISABLED)

    b1.grid(row=2, column=0)
    b2.grid(row=2, column=1)
    b3.grid(row=2, column=2)





w1 = Label(root, text='Score: 0/0')
w2 = Label(root, text='You/Computer')
w3 = Label(root, text="")
w4 = Label(root, text='Your Choice:')
w5 = Label(root, text="Computer's Choice:")

buttons_disabled()
b4 = Button(root, text='Start', command= start )
b5 = Button(root, text='Try again',state=DISABLED)
b5.grid(row=1, column=2)


w1.grid(row=0, column=0)
w2.grid(row=0, column=2)
w3.grid(row=1, column=1)
w4.grid(row=3, column=0)
w5.grid(row=3, column=2)


b4.grid(row=1, column=1)




root.mainloop()