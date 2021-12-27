from tkinter import *
from PIL import Image, ImageTk
from random import randint


root = Tk()


#list
choices = ["rock", "paper", "scissors"]


#header
root.title("Jan Ken")
root.configure(background = "black")
root.iconbitmap('icon.ico')


#images
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png"))
player_img = ImageTk.PhotoImage(Image.open("man.png"))
comp_img = ImageTk.PhotoImage(Image.open("comp.png"))


#labels
comp_label = Label(root, image = comp_img, bg = "black")
comp_label.grid(row = 1, column = 0)
player_label = Label(root, image = player_img, bg = "black")
player_label.grid(row = 1, column = 4)


#score board
comp_score = Label(root, text = 0, font= ("comic sans", 20, "bold"), fg = "green", bg = "black")
comp_score.grid(row = 3, column = 0)
player_score = Label(root, text = 0, font= ("comic sans", 20, "bold"), fg = "green", bg = "black")
player_score.grid(row = 3, column = 4)


#indicators
player_ind = Label(root, font = ("comic sans", 20, "bold"), text = "Player", bg = "black", fg = "white")
player_ind.grid(row = 2, column = 4)
comp_ind = Label(root, font = ("comic sans", 20, "bold"), text = "Computer", bg = "black", fg = "white")
comp_ind.grid(row = 2, column = 0)


#functions
def final_msg_update(msg):
    final_msg['text'] = msg


def comp_score_update():
    final = int(comp_score['text'])
    final += 1
    comp_score['text'] = str(final)


def player_score_update():
    final = int(player_score['text'])
    final += 1
    player_score['text'] = str(final)


def winner(player, computer):
    if player == computer:
        final_msg_update("It's a tie!!!")
    elif player == "rock":
        if computer == "paper":
            final_msg_update("You Lose!!!")
            comp_score_update()
        else:
            final_msg_update("You Win!!!")
            player_score_update()
    elif player == "paper":
        if computer == "scissors":
            final_msg_update("You lose!!!!")
            comp_score_update()
        else:
            final_msg_update("You Win!!!")
            player_score_update()
    elif player == "scissors":
        if computer == "rock":
            final_msg_update("You lose!!!")
            comp_score_update()
        else:
            final_msg_update("You Win!!!")
            player_score_update()
    else:
        pass


def exit_game():
    root.destroy()


def final_winner():
    player_sc = int(player_score['text'])
    comp_sc = int(comp_score['text'])

    if player_sc == 5:
        final_msg_update("YOU WON\nTHE GAME")
        rock_btn["state"] = "disable"
        paper_btn["state"] = "disable"
        scissor_btn["state"] = "disable"
        exit = Button(root, text = "EXIT", command= exit_game, width = 10, height = 1, font = ("comic sans", 20, "bold"), bg = "white", fg = "black")
        exit.grid(row =6, column= 2)
    elif comp_sc == 5:
        final_msg_update("YOU LOST\nTHE GAME")
        rock_btn["state"] = "disable"
        paper_btn["state"] = "disable"
        scissor_btn["state"] = "disable"
        exit = Button(root, text = "EXIT", command= exit_game, width = 10, height = 1, font = ("comic sans", 20, "bold"), bg = "white", fg = "black")
        exit.grid(row =6, column= 2)
    else:
        pass


def update_choice(msg):
    comp_choice = choices[randint(0,2)]
    if comp_choice == "rock":
        comp_choice_img = Label(root, image= rock_img, bg = "black")
        comp_choice_img.grid(row = 1, column =1)
    elif comp_choice == "paper":
        comp_choice_img = Label(root, image= paper_img, bg = "black")
        comp_choice_img.grid(row = 1, column =1)
    elif comp_choice == "scissors":
        comp_choice_img = Label(root, image= scissors_img, bg = "black")
        comp_choice_img.grid(row = 1, column =1)

    if msg == "rock":
        player_choice_img = Label(root, image=rock_img, bg = "black")
        player_choice_img.grid(row = 1, column =3)
    elif msg == "paper":
        player_choice_img = Label(root, image=paper_img, bg = "black")
        player_choice_img.grid(row = 1, column =3)
    elif msg == "scissors":
        player_choice_img = Label(root, image=scissors_img, bg = "black")
        player_choice_img.grid(row = 1, column =3)
    
    winner(msg, comp_choice)
    final_winner()


#buttons
rock_btn = Button(root, width = 10, height = 1, text = "Rock", font = ("comic sans", 20, "bold"), bg = "white", fg = "black", command = lambda:update_choice("rock"))
rock_btn.grid(row = 4, column = 1, padx = 5, pady = 10)
paper_btn = Button(root, width = 10, height = 1, text = "Paper", font = ("comic sans", 20, "bold"), bg = "white", fg = "black", command = lambda:update_choice("paper"))
paper_btn.grid(row = 4, column = 2, padx = 5, pady = 10)
scissor_btn = Button(root, width = 10, height = 1, text = "Scissors", font = ("comic sans", 20, "bold"), bg = "white", fg = "black", command = lambda:update_choice("scissors"))
scissor_btn.grid(row = 4, column = 3, padx = 5, pady = 10)


#final message
final_msg = Label(root, font = ("comic sans", 60, "bold"), bg = "black", fg = "yellow")
final_msg.grid(row = 5, column = 2)


root.mainloop()