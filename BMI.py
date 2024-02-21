import tkinter
from tkinter import *
from PIL import ImageTk, Image

path = r'C:\Users\tuzun\Desktop\Remove-bg.ai_1708437756203.png'
window = Tk()
window.title("BMI Calculater")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)  # boşluk bırakır

#resmin orjinalliğini koruyarak boyutlandırma
original_image = Image.open(path)
resized_image = original_image.resize((130, 130))

img = ImageTk.PhotoImage(resized_image)

image_label = Label(window, image=img) #picture added
image_label.pack()

my_label = tkinter.Label(text="BMI Calculator",font=("Arial",18),fg='saddle brown')
my_label.config(pady=13)
my_label.pack()

my_label1 = Label(text="Kilonuzu Girin")
my_label1.config(fg="black")
my_label1.pack()

# kilo entry
my_entry = Entry(width=30)
my_entry.focus()  # ilk buradan başlar
my_entry.pack()

my_label2 = Label(text="Boyunuzu Girin")
my_label2.config(fg="black")
my_label2.config(padx=10, pady=10)
my_label2.pack()

# boy entry
my_entry2 = Entry(width=30)
my_entry2.pack()

result_label = Label()
result_label.pack()
# Sonuç etiketini depolamak için
# Kullanıcı her butona bastığında eski sonucu silip yeni sonucu ekrana yazdırmak istiyorsak,
# her seferinde yeni bir etiket oluşturmak yerine aynı etiketi güncelleyebiliriz.
# Bu şekilde yaparız güncellemeyi


def button():
    global result_label

    text = my_entry.get()
    text1 = my_entry2.get()

    if text.isdigit() and text1.isdigit():
        boy_cm = int(text1)
        kilo_kg = int(text)
        boy_metre = boy_cm / 100
        vki = kilo_kg / (boy_metre ** 2)

        if vki > 25:
            result_text = "Endeks: {:.1f} Fazla Kilo".format(vki)
        elif vki < 18.5:
            result_text = "Endeks: {:.1f} Zayıf".format(vki)
        else:
            result_text = "Endeks: {:.1f} Normal Kilo".format(vki)

        result_label.config(text=result_text)
        result_label.config(padx=10,pady=10)
    else:
        result_label.config(text="Geçerli bir sayı giriniz.")

my_button = Button(text="Hesapla", command=button)
my_button.config(padx=1, pady=1)
my_button.pack(padx=(10, 0), pady=(10, 0))

#koordinat
image_label.update()

print(image_label.winfo_x(),image_label.winfo_y())

window.mainloop()
