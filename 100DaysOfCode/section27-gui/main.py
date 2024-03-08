import tkinter

windown = tkinter.Tk()
windown.title("My first GUI Program")
windown.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack(side='left')

my_label.config(text="New name of label.")

#Button

def button_click():
    new_value = input.get()
    my_label.config(text=new_value)


my_botton = tkinter.Button()
my_botton.config(
    fg="red", 
    bg="green",
    text="Click me",
    command=button_click,
)
my_botton.pack()

#Entry

input = tkinter.Entry()
input.config(
    width=30
)
input.pack()

windown.mainloop()