import customtkinter as tk
import tkinter
# Add another python code (in order to functions)
from Main import *

def mostrarGINI():
    window.destroy()
    return

# Open first window
window= tk.CTk()
tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")
window.geometry('800x600')
window.title('Indice de GINI')

# Craft background frame 
frame1= tk.CTkFrame(master= window)
frame1.pack(pady=20, padx=60, fill= "both", expand= True)

# Print message 1 
label1= tk.CTkLabel(master= frame1, text="Ingrese un país de la siguiente lista: ")
label1.pack(pady= 12, padx= 10)

# Print countries list.
label2= tk.CTkLabel(master= frame1, text= listaPaises())
label2.pack(pady= 0, padx= 10)

# Add entry "Country"
entry1= tk.CTkEntry(master= frame1, placeholder_text= "País")
entry1.pack(pady= 0, padx= 10)

# Add button to get into a country.
button1= tk.CTkButton(master= frame1, text= "Buscar", command= mostrarGINI)
button1.pack(pady= 12, padx=10)

# Run
window.mainloop()