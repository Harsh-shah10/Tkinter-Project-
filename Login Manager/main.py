from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def handle_login():
    email = email_input.get()
    pwd = password_input.get()

    if email=='harsh@gmail.com' and pwd=='1234':
        messagebox.showinfo('Welcome User')
    elif email==' ' or pwd==' ':
        messagebox.showerror('Fields Empty !!')
    else:
        messagebox.showerror('Invalid Login Details')

# create an obj of the Tk class of tkinter pkg
tk_obj = Tk()


# Code to add widgets will go here...

# to modify the title of the app
tk_obj.title('Login Application')

# to modify the logo/icon of the app
    #tk_obj.iconbitmap(r"image/favicon.ico")

# to modify the size of the windows
tk_obj.minsize(350,450)
tk_obj.maxsize(400,400)
'''
we can also pass custom size : to create a window of
particular size

tk_obj.geometry(350x500)

'''

# setting the abckground color of the twinker app
tk_obj.configure(background='#BFBDC1')
img = Image.open('image/Tesla_logo.png')
resized_img = img.resize((75,75))



# resizing the image [logo] and adding it to the background
img = ImageTk.PhotoImage(resized_img)

img_label = Label(tk_obj,image=img)
img_label.pack(pady=(10,10))

# adding the label for the logo below it
text_label = Label(tk_obj,text='Tesla',fg='white',bg='#BFBDC1')
text_label.pack()
text_label.config(font=('verdana',14))



# adding email label for the input fields
email_label = Label(tk_obj,text='Enter Email',fg='white',bg='#BFBDC1')
email_label.pack(pady=(20,5))
email_label.config(font=('Arial',12))

# adding email input box
email_input = Entry(tk_obj,width=35)
email_input.pack(ipady=3,pady=(1,11))



# adding password label for the input fields
password_label = Label(tk_obj,text='Enter Password',fg='white',bg='#BFBDC1')
password_label.pack(pady=(20,5))
password_label.config(font=('Arial',12))

# adding password input box
password_input = Entry(tk_obj,width=35)
password_input.pack(ipady=3,pady=(1,11))


# Adding a login button
login_btn = Button(tk_obj,text='Login',fg='white',bg='#DEB841',width=12,height=1,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('Arial',12))


tk_obj.mainloop()

