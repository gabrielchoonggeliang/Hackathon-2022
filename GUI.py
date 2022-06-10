from tkinter import *
from PIL import Image

# LOGO
Logo_file = Image.open("GUI/Test 2/logo.jpg")
Logo_file.save("logo.ico")

# Function
def size(variable):
    if variable == "S":
        print(f"{variable}")
        size_variable = variable
        return size_variable

def enter(name_variable, size_variable):
    print("Name:", name_variable)
    print("\nSize:", size_variable)

# Main Screen
window = Tk()
window.title("Uniform")
window.iconbitmap("logo.ico")
window.geometry("350x250")

# Frame
Title_Frame = Frame(window)
Title_Frame.pack(side=TOP)

Dummy_Frame = Frame(window)
Dummy_Frame.pack(side=TOP)

Name_Frame = Frame(window)
Name_Frame.pack(side=TOP)

Dummy_1_Frame = Frame(window)
Dummy_1_Frame.pack(side=TOP)

Size_Frame = Frame(window)
Size_Frame.pack(side=TOP)

Dummy_2_Frame = Frame(window)
Dummy_2_Frame.pack(side=TOP)

Enter_Frame = Frame(window)
Enter_Frame.pack(side=TOP)

# Label
Title_Label = Label(Title_Frame, text="Uniform", font=("Arial", 20))
Title_Label.pack(side=TOP)

Name_Label = Label(Name_Frame, text="Name:", font=("Arial", 16))
Name_Label.pack(side=LEFT)

Size_Label = Label(Size_Frame, text="Size:", font=("Arial", 16))
Size_Label.pack(side=TOP)

# Dummy Label
Dummy_Label = Label(Dummy_Frame)
Dummy_Label.pack(side=BOTTOM)

Dummy_1_Label = Label(Dummy_1_Frame)
Dummy_1_Label.pack(side=BOTTOM)

Dummy_2_Label = Label(Dummy_2_Frame)
Dummy_2_Label.pack(side=BOTTOM)

# Button
Enter_Button = Button(Enter_Frame, text="Enter", width=10, height=1, font=("Arial", 14), command=lambda: enter(Name.get(), size.get()))
Enter_Button.pack(side=BOTTOM)

# Size Option ttk
XS_Size_Option_ttk = Checkbutton(Size_Frame, text="XS", command=lambda: size("XS"))
XS_Size_Option_ttk.pack(side=LEFT)

S_Size_Option_ttk = Checkbutton(Size_Frame, text="S", command=lambda: size("S"))
S_Size_Option_ttk.pack(side=LEFT)

M_Size_Option_ttk = Checkbutton(Size_Frame, text="M", command=lambda: size("M"))
M_Size_Option_ttk.pack(side=LEFT)

L_Size_Option_ttk = Checkbutton(Size_Frame, text="L", command=lambda: size("L"))
L_Size_Option_ttk.pack(side=LEFT)

XL_Size_Option_ttk = Checkbutton(Size_Frame, text="XL", command=lambda: size("XL"))
XL_Size_Option_ttk.pack(side=LEFT)

XXL_Size_Option_ttk = Checkbutton(Size_Frame, text="2XL", command=lambda: size("2XL"))
XXL_Size_Option_ttk.pack(side=LEFT)

XXXL_Size_Option_ttk = Checkbutton(Size_Frame, text="3XL", command=lambda: size("3XL"))
XXXL_Size_Option_ttk.pack(side=LEFT)

# Entry
Name = StringVar()
Name_Entry = Entry(Name_Frame, textvariable=Name, font=("Arial",14))
Name_Entry.pack(side=LEFT)

window.mainloop()