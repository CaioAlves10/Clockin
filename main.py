# import tkinter
#
# tela = tkinter.Tk() #cria a tela
# tela.geometry("500x300")
#
# def clique():
#     print("Login realizado")
#
# texto = tkinter.Label(tela, text="Fazer login") #crei o elemento
# texto.pack(padx=10, pady=10) #inseri na tela
#
# botao= tkinter.Button(tela, text="Login", command=clique)
# botao.pack(padx=10, pady=10)
#
# tela.mainloop() #garante que a tela ficarÃ¡ aberta

import tkinter
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

telaLogin = customtkinter.CTk()
telaLogin.geometry("1440x900")

def clique():
    print("Login realizado")

logo = customtkinter.CTkImage(light_image=Image.open("/Clockin/images/logo-clockin.png"),
                                  dark_image=Image.open("/Clockin/images/logo-clockin.png"),
                                  size=(135, 135))

image_label = customtkinter.CTkLabel(telaLogin, image=logo, text="hi")  # display image with a CTkLabel

texto = customtkinter.CTkLabel(telaLogin, text="Fazer login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(telaLogin, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(telaLogin, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(telaLogin, text="Login", command=clique)
botao.pack(padx=10, pady=10)
#botao.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

telaLogin.mainloop()