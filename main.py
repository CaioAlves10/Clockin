import tkinter
from tkinter import messagebox
import customtkinter
import tkinter.font
from PIL import Image
from doctest import master
import mysql.connector

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")


def connect():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='clockin_db'
        )
        if conn.is_connected():
            print('Conexão bem-sucedida ao banco de dados.')
            return conn
    except mysql.connector.Error as e:
        print(f'Erro ao conectar no banco de dados: {e}')
        messagebox.showerror('Erro', 'Erro ao conectar no banco de dados.')


def close_connection(conn):
    if conn.is_connected():
        conn.close()
        print('Conexão ao banco de dados fechada.')


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

        self.password = customtkinter.CTkEntry(master=self.frame, width=330, height=40, placeholder_text="Sua senha",
                                               show="*")
        self.password.place(x=35, y=130)

        self.cadastro_button = customtkinter.CTkButton(master=self.frame, width=100, height=40, text='CADASTRAR',
                                                       corner_radius=6,
                                                       font=font_button, fg_color='#FAA115', hover_color='#FBA827',
                                                       command=troca)
        self.cadastro_button.place(x=150, y=190)

        self.login_link = customtkinter.CTkButton(self, text='LOGAR', text_color='#3F5B80',
                                                  fg_color='transparent', bg_color='#D2DDF9', hover=False,
                                                  font=font_link, command=self.open_telaLogin)
        self.login_link.place(relx=0.5, rely=0.74, anchor=tkinter.CENTER)

        self.creator = customtkinter.CTkLabel(self, text='Criado por Caio Carvalho', text_color='#7D7987',
                                              bg_color='#D2DDF9', font=font_creator)
        self.creator.place(relx=0.5, rely=0.96, anchor=tkinter.CENTER)

    def open_telaLogin(self):
        self.destroy()  # Fecha janela atual
        self.tela_login.deiconify()  # Exibe janela anterior


class TelaLogin(customtkinter.CTk):
    def logar(self):
        login = self.login.get()
        password = self.password.get()

        conn = connect()
        if conn:
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE login = %s AND senha = %s"
            cursor.execute(query, (login, password))
            user = cursor.fetchone()
            cursor.close()
            close_connection(conn)

            if user:
                messagebox.showinfo('Sucesso', 'Login bem-sucedido.')
            else:
                messagebox.showwarning('Aviso', 'Credenciais inválidas.')

    def open_telaCadastro(self):
        self.withdraw()  # fecha janela atual
        tela_cadastro = TelaCadastro(self, self)
        tela_cadastro.mainloop()  # abre nova janela

    def open_batidaPonto(self):
        self.withdraw()  # fecha janela atual
        tela_batida_ponto = TelaBatidaPonto(self, self)
        tela_batida_ponto.mainloop()  # abre nova janela

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.login = None
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
        self.image_logo = customtkinter.CTkLabel(self, image=logo, text="",
                                                 fg_color='#D2DDF9')  # display image with a CTkLabel
        self.image_logo.place(relx=0.5, rely=0.16, anchor=tkinter.CENTER)

        self.image_text_logo = customtkinter.CTkLabel(self, image=text_logo, text="",
                                                      fg_color='#D2DDF9')  # display image with a CTkLabel
        self.image_text_logo.place(relx=0.5, rely=0.27, anchor=tkinter.CENTER)

        frame = customtkinter.CTkFrame(master=master, width=400, height=255, corner_radius=15, fg_color='#F2F2F2',
                                       bg_color='#D2DDF9')
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        title = customtkinter.CTkLabel(master=frame, text='Logar:', text_color='#7D7987', font=font_title)
        title.place(x=35, y=30)

        self.login = customtkinter.CTkEntry(master=frame, width=330, height=40, placeholder_text="Seu login")
        self.login.place(x=35, y=70)

        self.password = customtkinter.CTkEntry(master=frame, width=330, height=40, placeholder_text="Sua senha",
                                               show="*")
        self.password.place(x=35, y=130)

        login_button = customtkinter.CTkButton(master=frame, width=100, height=40, text='LOGIN', corner_radius=6,
                                               font=font_button, fg_color='#FAA115', hover_color='#FBA827',
                                               command=self.open_batidaPonto)
        login_button.place(x=150, y=190)

        self.cadastro_link = customtkinter.CTkButton(self, text='CADASTRE-SE', text_color='#3F5B80',
                                                     fg_color='transparent', bg_color='#D2DDF9', hover=False,
                                                     font=font_link, command=self.open_telaCadastro)
        self.cadastro_link.place(relx=0.5, rely=0.74, anchor=tkinter.CENTER)

        self.toplevel_window = None

        self.creator = customtkinter.CTkLabel(self, text='Criado por Caio Carvalho', text_color='#7D7987',
                                              bg_color='#D2DDF9', font=font_creator)
        self.creator.place(relx=0.5, rely=0.96, anchor=tkinter.CENTER)


class TelaBatidaPonto(customtkinter.CTkToplevel):
    def __init__(self, tela_login, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event = None
        self.height = None
        self.width = None
        self.tela_login = tela_login
        self.geometry("900x800")
        self.title("Clockin - Batida de Ponto")
        self.config(bg='#F9F9F9')

        # Declarations

        # Creation of elements
        self.frame1 = customtkinter.CTkFrame(self, width=900, height=135, bg_color='#D2DDF9')
        self.frame1.place(x=35, y=30)

        self.title1 = customtkinter.CTkLabel(master=self.frame1, text='Logar:', text_color='#000')
        self.title1.place(x=35, y=30)


# Functions
def clique():
    print("Login realizado")


def troca():
    print("Cadastro pronto")


app = TelaLogin()
app.mainloop()
