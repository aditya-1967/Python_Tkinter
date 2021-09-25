from tkinter import *
from PIL import ImageTk, Image

root = Tk()


root.iconbitmap('G:\Projects\GUI\Icons\matrix.ico')

my_img1 = ImageTk.PhotoImage(Image.open("G:\Projects\GUI\Images\picture 1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("G:\Projects\GUI\Images\picture 2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("G:\Projects\GUI\Images\picture 3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("G:\Projects\GUI\Images\picture 4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("G:\Projects\GUI\Images\picture 5.jpg"))


image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_lable = Label(image = my_img1)
my_lable.grid(row = 0, column = 0, columnspan = 3)


def forward(image_number):
    global my_lable
    global button_next
    global button_back
    
    my_lable.grid_forget()
    my_lable = Label(image = image_list[image_number - 1])
    button_next = Button(root, text = ">>", command = lambda: forward(image_number + 1))
    button_back = Button(root, text = "<<", command = lambda: backward(image_number - 1))
    
    if image_number == 5:
        button_next = Button(root, text = ">>", state = DISABLED)
    
    my_lable.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_next.grid(row = 1, column = 2)


def backward(image_number):
    global my_lable
    global button_next
    global button_back
    
    my_lable.grid_forget()

    my_lable = Label(image = image_list[image_number - 1])
    button_next = Button(root, text = ">>", command = lambda: forward(image_number + 1))
    button_back = Button(root, text = "<<", command = lambda: backward(image_number - 1))
    
    if image_number == 1:
        button_back = Button(root, text = "<<", state = DISABLED)
    
    my_lable.grid(row = 0, column = 0, columnspan = 3)
    button_back.grid(row = 1, column = 0)
    button_next.grid(row = 1, column = 2)



button_back = Button(root, text = '<<', command = backward, state = DISABLED)
button_next = Button(root, text = '>>', command = lambda: forward(2))

button_quit = Button(root, text = 'Quit', command = root.quit)

button_back.grid(row = 1, column = 0)
button_quit.grid(row = 1, column = 1)
button_next.grid(row = 1, column = 2)



root.mainloop()