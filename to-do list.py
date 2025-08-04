import customtkinter 
from tkinter import filedialog
from PIL import Image, ImageTk
import time

# window config
window = customtkinter.CTk()
window.title("To-Do List")
window.geometry("400x400")

topframe = customtkinter.CTkFrame(window,width=400,height=40,fg_color="black")
topframe.place(x=0,y=0)

clock = customtkinter.CTkLabel(window, font=("Helvetica", 20))
clock.place(x=150,y=7)

def update_clock():
    current_time = time.strftime("%H:%M:%S") 
    clock.configure(text=current_time)
    window.after(1000, update_clock) 

update_clock()

# heading
heading = customtkinter.CTkLabel(window, text="To-Do-List", font=("Helvetica", 15),fg_color="black")
heading.place(x=10, y=7)
y = 50
def addentry():
    global y 
    if 50 + y > 400:
        taskaddbtn.destroy()

    entry1 = customtkinter.CTkEntry(window,height=20)
    entry1.place(x=9,y=y)
    
    def clear_entry():
        entry1.delete(0, customtkinter.END) 

    donebtn = customtkinter.CTkButton(
        window,
        text="Done",
        width=30,
        height=20,
        font=("Helvetica", 10),
        command=clear_entry  
    )
    donebtn.place(x=160, y=y)
    y = y + 30
    taskaddbtn.place(x=9,y=y)    
 
taskaddbtn = customtkinter.CTkButton(window,text="ADD",font=("Helvetica",12),width=15,command=addentry)
taskaddbtn.place(x=9,y=50)



# background image setup
backgorund_image = None
backgroundimageinsert = customtkinter.CTkLabel(window, text="")  
backgroundimageinsert.place(x=0, y=0)

# function to change background image
def openfile():
    global backgorund_image
    openfilemanager = filedialog.askopenfilename()
    readfile = Image.open(openfilemanager)
    readfile = readfile.resize((500, 500))  
    backgorund_image = ImageTk.PhotoImage(readfile)

    backgroundimageinsert.configure(image=backgorund_image) 
    backgroundimageinsert.lower() 


changebackgroundimagebutton = customtkinter.CTkButton(
    window,
    text="Change background",
    width=15,
    height=20,
    font=("Helvetica", 10),
    command=openfile
)
changebackgroundimagebutton.place(x=290, y=11)




window.mainloop()
