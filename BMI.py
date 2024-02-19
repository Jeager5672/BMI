from tkinter import *

window = Tk()
window.title("BMI Calculater")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)  # boşluk bırakır

my_label = Label(text="Vücut Kitle Endeksi", font=("Arial", 20, "italic"))
my_label.config(fg="black")
my_label.config(padx=10, pady=10)
my_label.pack()

my_label1 = Label(text="Kilonuzu Girin")
my_label1.config(fg="black")
my_label1.config(padx=10, pady=10)
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
my_entry2.focus()  # ilk buradan başlar
my_entry2.pack()

result_label = None  # Sonuç etiketini depolamak için
# Kullanıcı her butona bastığında eski sonucu silip yeni sonucu ekrana yazdırmak istiyorsak,
# her seferinde yeni bir etiket oluşturmak yerine aynı etiketi güncelleyebiliriz.
# Bu şekilde yaparız güncellemeyi


def button():
    global result_label

    text = my_entry.get()
    text1 = my_entry2.get()

    if text.isdigit() and text1.isdigit():
        if int(text1) < 100 or int(text) < 10:
            if result_label:  # Eğer sonuç etiketi zaten varsa sil
                result_label.destroy()
            result_label = Label(text="Boyunuz 100cm'den, kilonuz 10kg'dan az olamaz !")
            result_label.pack()
        else:
            boy_cm = int(text1)
            kilo_kg = int(text)
            boy_metre = boy_cm / 100
            vki = kilo_kg / (boy_metre ** 2)

            if result_label:  # Eğer sonuç etiketi zaten varsa sil
                result_label.destroy()

            if vki > 25:
                result_label = Label(text="Endeks: {:.1f} Fazla Kilo".format(vki))
            elif vki < 18.5:
                result_label = Label(text="Endeks: {:.1f} Zayıf".format(vki))
            elif 18.5 <= vki < 25:
                result_label = Label(text="Endeks: {:.1f} Normal Kilo".format(vki))

            result_label.pack()
    else:
        result_label = Label(text="Geçerli bir sayı giriniz.")
        result_label.pack()


my_button = Button(text="Hesapla", command=button)
my_button.config(padx=1, pady=1)
my_button.pack(padx=(10, 0), pady=(10, 0))

window.mainloop()
