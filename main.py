import tkinter
import customtkinter
import tkinter.font
from PIL import Image
from doctest import master

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

class TelaCadastro(customtkinter.CTkToplevel):
    def __init__(self, tela_login, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tela_login = tela_login
        self.geometry("900x800")
        self.title("Clockin - Cadastro")
        self.config(bg='#D2DDF9')

        # Declarations
        font_title = customtkinter.CTkFont(family='', size=20, weight='bold')
        font_button = customtkinter.CTkFont(family='', size=14, weight='bold')
        font_link = customtkinter.CTkFont(family='inter', size=13, weight='bold', underline=True)
        font_creator = customtkinter.CTkFont(family='inter', size=15)

        logo = customtkinter.CTkImage(light_image=Image.open("images/logo-clockin.png"),
                                      dark_image=Image.open("images/logo-clockin.png"),
                                      size=(110, 110))

        text_logo = customtkinter.CTkImage(light_image=Image.open("images/text-clockin.png"),
                                           dark_image=Image.open("images/text-clockin.png"),
                                           size=(130, 30))

        # Creation of elements
        self.image_logo = customtkinter.CTkLabel(self, image=logo, text="",
                                                 fg_color='#D2DDF9')  # display image with a CTkLabel
        self.image_logo.place(relx=0.5, rely=0.16, anchor=tkinter.CENTER)

        self.image_text_logo = customtkinter.CTkLabel(self, image=text_logo, text="",
                                                      fg_color='#D2DDF9')  # display image with a CTkLabel
        self.image_text_logo.place(relx=0.5, rely=0.27, anchor=tkinter.CENTER)

        self.frame = customtkinter.CTkFrame(self, width=400, height=255, corner_radius=15, fg_color='#F2F2F2',
                                       bg_color='#D2DDF9')
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.title = customtkinter.CTkLabel(master=self.frame, text='Cadastrar:', text_color='#7D7987', font=font_title)
        self.title.place(x=35, y=30)

        self.login = customtkinter.CTkEntry(master=self.frame, width=330, height=40, placeholder_text="Seu login")
        self.login.place(x=35, y=70)

        self.password = customtkinter.CTkEntry(master=self.frame, width=330, height=40, placeholder_text="Sua senha", show="*")
        self.password.place(x=35, y=130)

        self.cadastro_button = customtkinter.CTkButton(master=self.frame, width=100, height=40, text='CADASTRAR', corner_radius=6,
                                               font=font_button, fg_color='#FAA115', hover_color='#FBA827',
                                               command=troca)
        self.cadastro_button.place(x=150, y=190)

        self.login_link = customtkinter.CTkButton(self, text='LOGAR', text_color='#3F5B80',
                                                       fg_color='transparent', bg_color='#D2DDF9', hover=False,
                                                       font=font_link, command=self.open_telaLogin)
        self.login_link.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        self.creator = customtkinter.CTkLabel(self, text='Criado por Caio Carvalho', text_color='#7D7987',
                                              bg_color='#D2DDF9', font=font_creator)
        self.creator.place(relx=0.5, rely=0.96, anchor=tkinter.CENTER)

    def open_telaLogin(self):
        self.destroy()  # Fecha janela atual
        self.tela_login.deiconify() # Exibe janela anterior

class TelaLogin(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("900x800")
        self.title("Clockin - Login")
        self.config(bg='#D2DDF9')

        # Declarations
        font_title = customtkinter.CTkFont(family='', size=20, weight='bold')
        font_button = customtkinter.CTkFont(family='', size=15, weight='bold')
        font_link = customtkinter.CTkFont(family='inter', size=13, weight='bold', underline=True)
        font_creator = customtkinter.CTkFont(family='inter', size=15)

        logo = customtkinter.CTkImage(light_image=Image.open("images/logo-clockin.png"),
                                      dark_image=Image.open("images/logo-clockin.png"),
                                      size=(110, 110))

        text_logo = customtkinter.CTkImage(light_image=Image.open("images/text-clockin.png"),
                                           dark_image=Image.open("images/text-clockin.png"),
                                           size=(130, 30))

        # Creation of elements
        self.image_logo = customtkinter.CTkLabel(self, image=logo, text="", fg_color='#D2DDF9')  # display image with a CTkLabel
        self.image_logo.place(relx=0.5, rely=0.16, anchor=tkinter.CENTER)

        self.image_text_logo = customtkinter.CTkLabel(self, image=text_logo, text="", fg_color='#D2DDF9')  # display image with a CTkLabel
        self.image_text_logo.place(relx=0.5, rely=0.27, anchor=tkinter.CENTER)

        frame = customtkinter.CTkFrame(master=master, width=400, height=255, corner_radius=15, fg_color='#F2F2F2', bg_color='#D2DDF9')
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        title = customtkinter.CTkLabel(master=frame, text='Logar:', text_color='#7D7987', font=font_title)
        title.place(x=35, y=30)

        login = customtkinter.CTkEntry(master=frame, width=330, height=40, placeholder_text="Seu login")
        login.place(x=35, y=70)

        password = customtkinter.CTkEntry(master=frame, width=330, height=40, placeholder_text="Sua senha", show="*")
        password.place(x=35, y=130)

        login_button = customtkinter.CTkButton(master=frame, width=100, height=40, text='LOGIN', corner_radius=6, font=font_button, fg_color='#FAA115', hover_color='#FBA827',
                                               command=clique)
        login_button.place(x=150, y=190)

        self.cadastro_link = customtkinter.CTkButton(self, text='CADASTRE-SE', text_color='#3F5B80', fg_color='transparent', bg_color='#D2DDF9', hover=False,
                                                       font=font_link, command=self.open_telaCadastro)
        self.cadastro_link.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        self.toplevel_window = None

        self.creator = customtkinter.CTkLabel(self, text='Criado por Caio Carvalho', text_color='#7D7987', bg_color='#D2DDF9', font=font_creator)
        self.creator.place(relx=0.5, rely=0.96, anchor=tkinter.CENTER)

    def open_telaCadastro(self):
        self.withdraw() # fecha janela atual
        tela_cadastro = TelaCadastro(self, self)
        tela_cadastro.mainloop() # abre nova janela

# Functions
def clique():
    print("Login realizado")


def troca():
    print("Cadastro pronto")

app = TelaLogin()
app.mainloop()
