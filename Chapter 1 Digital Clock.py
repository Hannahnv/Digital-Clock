#Digital Clock

from tkinter import Label,Tk
from time import strftime # Importing strftime function to retrieve system's time
# Creating Tkinter window
root=Tk()
root.title('Digital Clock')
root.configure(background='purple') #Background of the clock

#Styling the label widget
label=Label(root, font = ('franklin gothic', 40, 'bold'),
            background='purple',
            foreground='pink')

def time(): 
    current_time=strftime('%H:%M:%S %p\n %d/%m/%Y')
    label.configure(text=current_time)
    label.after(100, time) #Updating the clock every 100 milliseconds
    label.pack(anchor='center') # Placing clock at the centre of the tkinter window
    
time()
root.mainloop()
