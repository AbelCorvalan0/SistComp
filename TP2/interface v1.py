import customtkinter
#import tkinter as tk
from mainv1 import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root= customtkinter.CTk()
root.geometry("800x500")

##### FUNCTIONS #####
year= 0
# Dentro de la 
def searchCountry():
    #Main.selectedCountry(entry1.get())
    if buscarPais(entry1.get()) != 404:
        #searchDate(entry1.get())
        searchDate()
    else:
        return

def searchDate():
    label1.configure(text= "Ingrese el año que desea consultar")
    label2.configure(text= buscarPais(entry1.get()))
    #entry1.delete(0, customtkinter.END)
    entry2= customtkinter.CTkEntry(master= frame, placeholder_text= "Año")
    entry2.pack(pady= 12, padx= 10)
    button1= customtkinter.CTkButton(master= frame, text= "Buscar", command= viewInd(entry2.get()))
    button1.pack(pady= 12, padx= 10)
    
    def viewInd(year):
    #label2.configure(text= retornoIndice(entry1.get(), '2019'))
    #label3= customtkinter.CTkLabel(master= frame, text= retornoIndice(entry1.get(),  '2020'))
        label3= customtkinter.CTkLabel(master= frame, text= retornoIndice(entry1.get(),  "'" + year + "'"))
        label3.pack(pady= 0, padx= 10)
        return
    return
    
# def viewInd(year):
#     #label2.configure(text= retornoIndice(entry1.get(), '2019'))
#     #label3= customtkinter.CTkLabel(master= frame, text= retornoIndice(entry1.get(),  '2020'))
#     label3= customtkinter.CTkLabel(master= frame, text= retornoIndice(entry1.get(),  "'" + year + "'"))
#     label3.pack(pady= 0, padx= 10)
#     return

##### INTERFACE #####

frame= customtkinter.CTkFrame(master= root)
frame.pack(pady=20, padx=60, fill="both", expand= True)

label= customtkinter.CTkLabel(master= frame, text="Índice de GINI")
label.pack(pady= 12, padx= 10)

label1= customtkinter.CTkLabel(master= frame, text="Ingrese un país de la siguiente lista: ")
label1.pack(pady= 12, padx= 10)

label2= customtkinter.CTkLabel(master= frame, text= listaPaises())
label2.pack(pady= 0, padx= 10)

entry1= customtkinter.CTkEntry(master= frame, placeholder_text= "País")
entry1.pack(pady= 12, padx= 10)

button= customtkinter.CTkButton(master= frame, text= "Buscar", command= searchCountry)
button.pack(pady= 12, padx= 10)

#checkbox= customtkinter.CTkCheckBox(master= frame, text= "El profe es re piola")
#checkbox.pack(pady= 12, padx=10)

root.mainloop()