from tkinter import *
import pandas as pd

BLACK = "#0F0F0F"
GREY = "#232D3F"
BLUE = "#0ef"
FONT = "Arial"





# Loading data from csv files

df_rank_salary = pd.read_csv("salary.csv")
df_age_percentage = pd.read_csv("rokyvsprocenta.csv")

# List of military ranks
hodnost = df_rank_salary["Hodnost"]
hodnost_list = hodnost.to_list()
hodnost = [i.replace('\xa0', '') for i in hodnost]

# Liat of service age 

age = df_age_percentage["Roky"]
age = age.to_list()
print(age)






window = Tk()
window.title("Renta AČR")
window.geometry("700x500")
window.configure(bg=BLACK, padx=20, pady=20, )
window.resizable(False, False)
window.iconbitmap("soldier_icon.ico")

header = Label(text="Renta AČR Kalkulačka",pady=10, bg=BLACK, fg=BLUE, font=(FONT, 24, "bold"))
header.grid(row=0, column=1)

rank_label = Label(text="Hodnost", bg=BLACK, fg=BLUE, font=(FONT, 16) )
rank_label.grid(row=1, column=0)

age_label = Label(text="Délka služby", bg=BLACK, fg=BLUE, font=(FONT, 16) )
age_label.grid(row=1, column=1)

extra_money_label = Label(text="Výkonnostní příspěvek", bg=BLACK, fg=BLUE, font=(FONT, 16) )
extra_money_label.grid(row=1, column=2)

# Create a Dropdown menu widget with the list of military ranks
rank_dropdown_menu = OptionMenu( window , StringVar(value="Vojín") , *hodnost) 
rank_dropdown_menu.configure(bg=BLUE, fg=GREY, width=12, activebackground=BLACK, activeforeground=BLUE, font=(FONT, 16))
rank_dropdown_menu.grid(row=2, column=0)

# Create a Dropdown menu widget with the list of service age
age_dropdown_menu = OptionMenu( window , StringVar(value="15") , *age) 
age_dropdown_menu.configure(bg=BLUE, fg=GREY, width=12, activebackground=BLACK, activeforeground=BLUE, font=(FONT, 16))
age_dropdown_menu.grid(row=2, column=1)



window.mainloop()