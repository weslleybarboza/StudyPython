import tkinter

windown = tkinter.Tk()
windown.title("Mile to KM Converter")
windown.minsize(width=500, height=300)
windown.configure(
    padx=100,
    pady=100,
    background="white"
)

#Entry_Miles
input_miles = tkinter.Entry()
input_miles.config(
    width=10
)
input_miles.grid(row=0, column=1)

#Label Miles
label_miles = tkinter.Label()
label_miles.config(
                text="Miles",
                font=("Arial", 12, "normal"),
                background="white"
                )
label_miles.grid(row=0, column=2)


#Label_equeal
Label_equeal = tkinter.Label()
Label_equeal.config(
                text="is equal to",
                font=("Arial", 12, "normal"),
                background="white"
                )
Label_equeal.grid(row=1, column=0)

#Label_result
Label_result = tkinter.Label()
Label_result.config(
                text="0",
                font=("Arial", 12, "normal"),
                background="white"
                )
Label_result.grid(row=1, column=1)

#Label_km
Label_km = tkinter.Label()
Label_km.config(
                text="Km",
                font=("Arial", 12, "normal"),
                background="white"
                )
Label_km.grid(row=1, column=2)

#Button_calculate
def button_click():
    mile_inputed = input_miles.get()
    mile_factor = 1.609344
    km = float(mile_inputed) * mile_factor
    new_value = km
    Label_result.config(text=new_value)


botton_calculate = tkinter.Button()
botton_calculate.config(
    text="Calculate",
    command=button_click,
)
botton_calculate.grid(row=2, column=1)

windown.mainloop()