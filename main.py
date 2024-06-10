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

# List of service age 
age = df_age_percentage["Roky"]
age = age.to_list()

#  Dictionary of military ranks
hodnost_dict = {row.Hodnost: row.Plat for (index, row) in df_rank_salary.iterrows()}
hodnost_dict = {key.replace('\N{NO-BREAK SPACE}', ''): value for key, value in hodnost_dict.items()}

#  Dictionary of service age
age_dict = {row.Roky: row.Procenta for (index, row) in df_age_percentage.iterrows()}


def count():
    selected_rank = value_rank.get()
    selected_age = value_age.get()   
    counted_salary = hodnost_dict.get(selected_rank)
    counted_percentage = age_dict.get(int(selected_age))
    selected_extra_money = extra_money_spinbox.get()
    renta = int(round((counted_salary + (counted_salary * (float(counted_percentage) / 100))) * counted_percentage, 0))
    canvas.delete(rank_label)
    canvas.create_text(200, 100, text=renta, fill= BLUE, font=(FONT, 30, "bold"))
    return renta
    


window = Tk()
window.title("Renta AČR")
window.geometry("700x500")
window.configure(bg=BLACK, padx=20, pady=20, )
window.resizable(False, False)
window.iconbitmap("soldier_icon.ico")


header = Label(text="Renta AČR Kalkulačka",pady=10, bg=BLACK, fg=BLUE, font=(FONT, 24, "bold"))
header.grid(row=0, column=1, columnspan=3)

rank_label = Label(text="Hodnost", bg=BLACK, fg=BLUE, font=(FONT, 16) )
rank_label.grid(row=1, column=0)

age_label = Label(text="Délka služby", bg=BLACK, fg=BLUE, font=(FONT, 16) )
age_label.grid(row=1, column=1)

extra_money_label = Label(text="Výkonnostní příspěvek", bg=BLACK, fg=BLUE, font=(FONT, 16) )
extra_money_label.grid(row=1, column=2)

# Create a Dropdown menu widget with the list of military ranks
value_rank =StringVar(window)
# Set the default value of the variable 
value_rank.set("Vojín") 
rank_dropdown_menu = OptionMenu( window , value_rank , *hodnost) 
rank_dropdown_menu.configure(bg=BLUE, fg=GREY, width=12, activebackground=BLACK, activeforeground=BLUE, font=(FONT, 16), cursor="hand2")
rank_dropdown_menu.grid(row=2, column=0)

# Create a Dropdown menu widget with the list of service age
value_age =StringVar(window)
# Set the default value of the variable 
value_age.set("15") 
age_dropdown_menu = OptionMenu( window , value_age , *age) 
age_dropdown_menu.configure(bg=BLUE, fg=GREY, width=12, activebackground=BLACK, activeforeground=BLUE, font=(FONT, 16), cursor="hand2")
age_dropdown_menu.grid(row=2, column=1)

extra_money_spinbox = Spinbox(window, from_=0, to=20, width=12, font=(FONT, 16), bg=BLUE, fg=BLACK)
extra_money_spinbox.config(state="normal", cursor="hand2", bd=3, justify="center", wrap=True, )
extra_money_spinbox.grid(row=2,column=2)

money_image = PhotoImage(file='money.png')
money_image.img = money_image
resized_img = money_image.subsample(2,2)
canvas = Canvas(window, height=200, width=400, background=BLACK, highlightthickness=0)
canvas.create_image(window.winfo_reqwidth(), window.winfo_reqheight()/2, image=resized_img)
rank_label = canvas.create_text(200, 100, text="0", fill= BLUE, font=(FONT, 30, "bold"))
canvas.grid(row=3, column=0, columnspan=3)


button = Button(text="Spočítat")
button.grid(row=4, column=1, pady=10)
button.configure(font=(FONT, 16), cursor="hand2",bg=BLUE, fg=BLACK, command=count)



window.mainloop()