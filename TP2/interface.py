import customtkinter
#import tkinter as tk
from Main import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root= customtkinter.CTk()
root.geometry("800x500")


def searchCountry():
    #Main.selectedCountry(entry1.get())
    if selectedCountry(entry1.get()) != 404:
        searchDate()
    else:
        #Acción de valor no válido (mensaje de ERROR)
        #label2.configure(text= "ERROR ERROR ERROR ERROR")
        return

def searchDate():
    label1.configure(text= "Ingrese el año que desea consultar")
    label2.configure(text= selectedCountry(entry1.get()))
    entry1.delete(0, customtkinter.END)
    label2.configure(text= selectedDate(entry1.get()))
    entry1.delete(0, customtkinter.END)
    label2.configure(text= selectedYear(entry1.get()))

frame= customtkinter.CTkFrame(master= root)
frame.pack(pady=20, padx=60, fill="both", expand= True)

label= customtkinter.CTkLabel(master= frame, text="Índice de GINI")
label.pack(pady= 12, padx= 10)

label1= customtkinter.CTkLabel(master= frame, text="Ingrese un país de la siguiente lista: ")
label1.pack(pady= 12, padx= 10)

label2= customtkinter.CTkLabel(master= frame, text= countriesList())
label2.pack(pady= 0, padx= 10)

entry1= customtkinter.CTkEntry(master= frame, placeholder_text= "País")
entry1.pack(pady= 12, padx= 10)

button= customtkinter.CTkButton(master= frame, text= "Buscar", command= searchCountry)
button.pack(pady= 12, padx= 10)

#checkbox= customtkinter.CTkCheckBox(master= frame, text= "El profe es re piola")
#checkbox.pack(pady= 12, padx=10)

root.mainloop()