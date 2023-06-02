import tkinter
import customtkinter
import tkinter.font
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
font_title = customtkinter.CTkFont(family='', size=20, weight='bold')
font_button = customtkinter.CTkFont(family='', size=15, weight='bold')
font_link = customtkinter.CTkFont(family='inter', size=13, weight='bold', underline=True)
font_creater = customtkinter.CTkFont(family='inter', size=15)

logo = customtkinter.CTkImage(light_image=Image.open("images/logo-clockin.png"),
                                  dark_image=Image.open("images/logo-clockin.png"),
                                  size=(110, 110))

text_logo = customtkinter.CTkImage(light_image=Image.open("images/text-clockin.png"),
                                  dark_image=Image.open("images/text-clockin.png"),
                                  size=(130, 30))

#Creation of elements
image_logo = customtkinter.CTkLabel(telaLogin, image=logo, text="", fg_color='#D2DDF9')  # display image with a CTkLabel
image_logo.place(relx=0.5, rely=0.16, anchor=tkinter.CENTER)

image_text_logo = customtkinter.CTkLabel(telaLogin, image=text_logo, text="", fg_color='#D2DDF9')  # display image with a CTkLabel
image_text_logo.place(relx=0.5, rely=0.27, anchor=tkinter.CENTER)

frame = customtkinter.CTkFrame(master=master, width=400, height=255, corner_radius=15, fg_color='#F2F2F2', bg_color='#D2DDF9')
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

title = customtkinter.CTkLabel(master=frame, text='Logar:', text_color='#7D7987', font=font_title)
title.place(x=35, y=30)

login = customtkinter.CTkEntry(master=frame, width=330, height=40, placeholder_text="Seu login")
login.place(x=35, y=70)

senha = customtkinter.CTkEntry(master=frame, width=330, height=40, placeholder_text="Sua senha", show="*")
senha.place(x=35, y=130)

botao_login = customtkinter.CTkButton(master=frame, width=100, height=40, text='LOGIN', corner_radius=6, font=font_button, fg_color='#FAA115', hover_color='#FBA827', command=clique)
botao_login.place(x=150, y=190)

cadastre_se= customtkinter.CTkLabel(telaLogin, text='CADASTRE-SE', text_color='#3F5B80', bg_color='#D2DDF9', font=font_link)
cadastre_se.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

creater= customtkinter.CTkLabel(telaLogin, text='Criado por Caio Carvalho', text_color='#7D7987', bg_color='#D2DDF9', font=font_creater)
creater.place(relx=0.5, rely=0.96, anchor=tkinter.CENTER)

telaLogin.mainloop()


#border_width=1, border_color='#828282'