from tkinter import * # her şeyi import ediyor

window = Tk()
window.title("tkinter ex")
window.minsize(width=600,height=600)
window.config(padx=20,pady=20) # boşluk bırakır

my_label = Label(text="My Label")
#my_label.config(bg="black")
my_label.config(fg="black")
my_label.config(padx=50,pady=50)
my_label.pack()

def button():
    print("clicked")
    print(my_text.get("1.0",END)) # bizden index ister entry gibi boş kalmaz
    #1.0 1.satırdan almaya başla demek 2 yapsak 2.satırdan 1.3 yazsak 1.satır 3.karakterden başlar

my_button = Button(text="my button",command=button)
my_button.pack()
my_button.config(padx=20,pady=20)

my_entry = Entry(width=20)
my_entry.focus() # ilk buradan başlar
my_entry.pack()

my_text = Text(width=30, height=10) # uzun yazı
my_text.pack()

#scale

def scale_selected(value):
    #print(my_scale.get()) #böyle yaparsak çöker
    print(value) # böyle yapılması gerekir
my_scale = Scale(from_=0,to=50,command=scale_selected) #buradan buraya git
my_scale.pack()

#spinbox
def spinboxx():
    print(my_spinbox.get()) # burada buton gibi
my_spinbox = Spinbox(from_=0,to=50,command=spinboxx)
my_spinbox.pack()

#checkbutton
def checkbutton_selected():
    print(check_state.get())

check_state = IntVar() # check edildi mi edilmedi mi için kullanılır
my_checkbutton = Checkbutton(text="check",variable=check_state,command=checkbutton_selected)
my_checkbutton.pack()

# radio button

def radio_selected():
    print(radio_checked_state.get())

radio_checked_state = IntVar()

my_radio_button = Radiobutton(text="1.option",value=10,variable=radio_checked_state,command=radio_selected)
my_radio_button2 = Radiobutton(text="2.option",value=20,variable=radio_checked_state,command=radio_selected)
my_radio_button.pack()
my_radio_button2.pack()

#listbox

# listedekileri eklemek

def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
name_list = ["Baris","Abc","asddsaf","Dasfasg"]
for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])

my_listbox.bind("<<ListboxSelect>>",listbox_selected) # fonksiyon bu şekilde bağlanır command olarak değil
my_listbox.pack()


window.mainloop()