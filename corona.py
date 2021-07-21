#Python 3
#Tkinter
#Covid
from tkinter import *
from covid import *
covid = Covid()
def search(e):
    try:
        info = covid.get_status_by_country_name(entry.get())
    except ValueError:
        pass
    else:
        con1.config(text=info['confirmed'])
        die1.config(text=info['deaths'])
        act1.config(text=info['active'])
pencere = Tk()
pencere.title('Covid-19 statistics')
pencere.resizable(0, 0)
entry = Entry(pencere, font=('Calibri (Body)', 16), justify="center")
con = Label(pencere, text="Confirmed: ", font=('Calibri (Body)', 16))
con1 = Label(pencere, text="", font=('Calibri (Body)', 16))
die = Label(pencere, text="Deaths: ", font=('Calibri (Body)', 16))
die1 = Label(pencere, text="", font=('Calibri (Body)', 16))
act = Label(pencere, text="Active: ", font=('Calibri (Body)', 16))
act1 = Label(pencere, text="", font=('Calibri (Body)', 16))
#location
entry.grid(row=0, column=0, columnspan=2)
con.grid(row=1, column=0)
con1.grid(row=1, column=1)
die.grid(row=2, column=0)
die1.grid(row=2, column=1)
act.grid(row=3, column=0)
act1.grid(row=3, column=1)
pencere.update()
width = pencere.winfo_screenwidth()//2 - pencere.winfo_width()//2
height = pencere.winfo_screenheight()//2 - pencere.winfo_height()//2
pencere.geometry(f'{pencere.winfo_width()}x{pencere.winfo_height()}+{width}+{height}')
#binding
entry.bind('<Return>', search)
pencere.mainloop()
