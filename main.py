import tkinter
import customtkinter
from PIL import Image
from doctest import master

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

telaLogin = customtkinter.CTk()
telaLogin.title("Clockin - Login")
telaLogin.config(bg='#D2DDF9')
telaLogin.geometry("900x800")

#Functions
def clique():
    print("Login realizado")


#Declarations
font_title = customtkinter.CTkFont(family='mulish', size=20, weight='bold')

logo = customtkinter.CTkImage(light_image=Image.open("images/logo-clockin.png"),
                                  dark_image=Image.open("images/logo-clockin.png"),
                                  size=(100, 100))

text_logo = customtkinter.CTkImage(light_image=Image.open("images/text-clockin.png"),
                                  dark_image=Image.open("images/text-clockin.png"),
                                  size=(130, 30))

#Creation of elements
image_logo = customtkinter.CTkLabel(telaLogin, image=logo, text="", fg_color='#D2DDF9')  # display image with a CTkLabel
image_logo.pack(padx=10, pady=10)

image_text_logo = customtkinter.CTkLabel(telaLogin, image=text_logo, text="", fg_color='#D2DDF9')  # display image with a CTkLabel
image_text_logo.pack(padx=10, pady=10)

frame = customtkinter.CTkFrame(master=master, width=320, height=360, corner_radius=15, fg_color='#F2F2F2', bg_color='#D2DDF9')
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

title = customtkinter.CTkLabel(master=frame, text='Logar:', text_color='#7D7987', font=font_title)
title.place(x=50, y=45)

email = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Seu e-mail")
email.place(x=50, y=110)

senha = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Sua senha", show="*")
senha.place(x=50, y=165)

botao_login = customtkinter.CTkButton(master=frame, width=220, text='Login', corner_radius=6, command=clique)
botao_login.place(x=50, y=240)

telaLogin.mainloop()