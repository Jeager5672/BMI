import tkinter

window = tkinter.Tk()
window.title("Deneme")
window.minsize(width=450,height=300)

def button():
    #text = my_entry.get() # ne yazarsak onu bastırır
    #print(text)
    pass

#label

my_label = tkinter.Label(text="this is a label",font=("Arial",30,"italic"))
#my_label.config(bg="Black",fg="white")
#my_label.pack(side="left") # konumlandırma, side left yapmazsak ortalar
#my_label.place(x=0,y=0) # tam olarak nereye koyacağımızı gösterir
my_label.grid(row=4,column=4) # ızgara metodu

#button

my_button = tkinter.Button(text="This is a button",command=button)
#my_button.pack()
my_button.grid(row=1,column=0)

#entry

#my_entry = tkinter.Entry(width=20)
#my_entry.pack()



window.mainloop()