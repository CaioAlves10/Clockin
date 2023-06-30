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


class TelaPrincipal(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('900x700')
        self.title('Clockin')
        self.config(bg='#D2DDF9')

        font_title = customtkinter.CTkFont(family='', size=20, weight='bold')
        font_button = customtkinter.CTkFont(family='', size=15, weight='bold')
        font_creator = customtkinter.CTkFont(family='inter', size=15)

        logo = customtkinter.CTkImage(light_image=Image.open("images/logo-clockin.png"), size=(120, 120))
        text_logo = customtkinter.CTkImage(light_image=Image.open("images/text-clockin.png"), size=(130, 30))

        self.image_logo = customtkinter.CTkLabel(self, image=logo, text="", fg_color='#D2DDF9')
        self.image_logo.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        self.image_text_logo = customtkinter.CTkLabel(self, image=text_logo, text="", fg_color='#D2DDF9')
        self.image_text_logo.place(relx=0.5, rely=0.34, anchor=tkinter.CENTER)

        # self.frame = customtkinter.CTkFrame(master=master, width=400, height=100, corner_radius=15, fg_color='#F2F2F2',
        #                                     bg_color='#D2DDF9')
        # self.frame.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

        # self.title = customtkinter.CTkLabel(master=self.frame, text='Logar:', text_color='#7D7987', font=font_title)
        # self.title.place(x=35, y=30)

        self.login_button = customtkinter.CTkButton(self, width=100, height=40, text='LOGIN',
                                                    corner_radius=6, font=font_button, fg_color='#FAA115',
                                                    hover_color='#FBA827', command=self.open_login)
        self.login_button.place(relx=0.4, rely=0.55, anchor=tkinter.CENTER)

        self.cadastro_button = customtkinter.CTkButton(self, height=40, text='CADASTRAR', corner_radius=6,
                                                       font=font_button, fg_color='#FAA115', hover_color='#FBA827',
                                                       command=self.open_cadastro)
        self.cadastro_button.place(relx=0.6, rely=0.55, anchor=tkinter.CENTER)

        self.creator = customtkinter.CTkLabel(self, text='Criado por Caio Carvalho', text_color='#7D7987',
                                              bg_color='#D2DDF9', font=font_creator)
        self.creator.place(relx=0.5, rely=0.96, anchor=tkinter.CENTER)

    def open_login(self):
        self.withdraw()
        tela_login = TelaLogin()
        tela_login.mainloop()

    def open_cadastro(self):
        self.withdraw()
        tela_cadastro = TelaCadastro(self)
        tela_cadastro.mainloop()


class TelaLogin(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tela_batida_ponto = None
        self.tela_cadastro = None
        self.geometry("900x750")
        self.title("Clockin - Login")
        self.config(bg='#D2DDF9')

        # Declarations
        font_title = customtkinter.CTkFont(family='', size=20, weight='bold')
        font_button = customtkinter.CTkFont(family='', size=15, weight='bold')
        font_link = customtkinter.CTkFont(family='inter', size=13, weight='bold', underline=True)
        font_creator = customtkinter.CTkFont(family='inter', size=15)

        logo = customtkinter.CTkImage(light_image=Image.open("images/logo-clockin.png"), size=(110, 110))
        text_logo = customtkinter.CTkImage(light_image=Image.open("images/text-clockin.png"), size=(130, 30))

        # Creation of elements
        self.image_logo = customtkinter.CTkLabel(self, image=logo, text="",
                                                 fg_color='#D2DDF9')  # display image with a CTkLabel
        self.image_logo.place(relx=0.5, rely=0.16, anchor=tkinter.CENTER)

        self.image_text_logo = customtkinter.CTkLabel(self, image=text_logo, text="",
                                                      fg_color='#D2DDF9')  # display image with a CTkLabel
        self.image_text_logo.place(relx=0.5, rely=0.27, anchor=tkinter.CENTER)

        self.frame = customtkinter.CTkFrame(self, width=400, height=255, corner_radius=15, fg_color='#F2F2F2',
                                            bg_color='#D2DDF9')
        self.frame.place(relx=0.5, rely=0.52, anchor=tkinter.CENTER)

        self.title = customtkinter.CTkLabel(master=self.frame, text='Logar:', text_color='#7D7987', font=font_title)
        self.title.place(x=35, y=30)

        self.login = customtkinter.CTkEntry(master=self.frame, width=330, height=40, placeholder_text="Seu login")
        self.login.place(x=35, y=70)

        self.password = customtkinter.CTkEntry(master=self.frame, width=330, height=40, placeholder_text="Sua senha",
                                               show="*")
        self.password.place(x=35, y=130)

        self.login_button = customtkinter.CTkButton(master=self.frame, width=100, height=40, text='LOGIN',
                                                    corner_radius=6, font=font_button, fg_color='#FAA115',
                                                    hover_color='#FBA827', command=self.open_batida_ponto)
        self.login_button.place(x=150, y=190)

        self.cadastro_link = customtkinter.CTkButton(self, text='CADASTRE-SE', text_color='#3F5B80',
                                                     fg_color='transparent', bg_color='#D2DDF9', hover=False,
                                                     font=font_link, command=self.open_cadastro)
        self.cadastro_link.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

        self.creator = customtkinter.CTkLabel(self, text='Criado por Caio Carvalho', text_color='#7D7987',
                                              bg_color='#D2DDF9', font=font_creator)
        self.creator.place(relx=0.5, rely=0.96, anchor=tkinter.CENTER)

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

    def open_batida_ponto(self):
        self.withdraw()
        self.tela_batida_ponto = TelaBatidaPonto(self, self)
        self.tela_batida_ponto.mainloop()

    def open_cadastro(self):
        self.withdraw()
        self.tela_cadastro = TelaCadastro(self)
        self.tela_cadastro.mainloop()


class TelaCadastro(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tela_login = None
        self.geometry("900x750")
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
        self.frame.place(relx=0.5, rely=0.52, anchor=tkinter.CENTER)

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
                                                  font=font_link, command=self.open_login)
        self.login_link.place(relx=0.5, rely=0.76, anchor=tkinter.CENTER)

        self.creator = customtkinter.CTkLabel(self, text='Criado por Caio Carvalho', text_color='#7D7987',
                                              bg_color='#D2DDF9', font=font_creator)
        self.creator.place(relx=0.5, rely=0.96, anchor=tkinter.CENTER)

    def open_login(self):
        self.withdraw()
        tela_login = TelaLogin()
        tela_login.mainloop()


class TelaBatidaPonto(customtkinter.CTkToplevel):
    def __init__(self, tela_login, tela_folha_ponto, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tela_folha_ponto = tela_folha_ponto
        self.tela_login = tela_login
        self.geometry("1200x750")
        self.title("Clockin - Batida de Ponto")
        self.config(bg='#F9F9F9')

        # Declarations
        font_title = customtkinter.CTkFont(family='', size=23, weight='bold')

        logo = customtkinter.CTkImage(light_image=Image.open("images/logo-clockin.png"), size=(85, 85))

        icon_clock_checked_white = customtkinter.CTkImage(light_image=Image.open("images/icon-clock-checked-white.png"),
                                                          size=(52, 52))
        icon_clock_schedule_white = customtkinter.CTkImage(light_image=Image.
                                                           open("images/icon-view-schedule-white.png"), size=(52, 52))
        icon_clock_logout_white = customtkinter.CTkImage(light_image=Image.open("images/icon-logout-white.png"),
                                                         size=(52, 52))

        icon_clock_add_blue = customtkinter.CTkImage(light_image=Image.open("images/icon-clock-add-blue.png"),
                                                     size=(52, 52))
        icon_clock_checked_blue = customtkinter.CTkImage(light_image=Image.open("images/icon-clock-checked-blue.png"),
                                                         size=(52, 52))
        icon_clock_schedule_blue = customtkinter.CTkImage(light_image=Image.open("images/icon-view-schedule-blue.png"),
                                                          size=(52, 52))
        icon_clock_logout_blue = customtkinter.CTkImage(light_image=Image.open("images/icon-logout-blue.png"),
                                                        size=(52, 52))

        # Creation of elements

        # -- header --
        # gambiarra
        self.header1 = customtkinter.CTkFrame(self, width=1990, height=130, fg_color='#D2DDF9', bg_color='#F9F9F9')
        self.header1.place(relx=0.5, rely=0.06, anchor=tkinter.CENTER)

        self.header = customtkinter.CTkFrame(self, width=900, height=130, fg_color='#D2DDF9', bg_color='#D2DDF9')
        self.header.place(relx=0.5, rely=0.06, anchor=tkinter.CENTER)

        self.title = customtkinter.CTkLabel(master=self.header, text='Batida de Ponto', text_color='#3F5B80',
                                            font=font_title)
        self.title.place(x=49, y=63)

        self.image_logo = customtkinter.CTkLabel(master=self.header, image=logo, text="", fg_color='#D2DDF9')
        self.image_logo.place(x=760, y=33)

        # --sidebar --
        self.sidebar = customtkinter.CTkFrame(self, width=90, height=400, fg_color='#D2DDF9', bg_color='#F9F9F9')
        self.sidebar.place(relx=0, rely=0.35)

        self.icon_clock_add = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_add_blue, text="")
        self.icon_clock_add.place(x=19, y=40)

        self.icon_clock_checked = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_checked_white, text="")
        self.icon_clock_checked.place(x=19, y=130)

        # evento é ativado quando mouse passa sobre a imagem
        self.icon_clock_checked.bind("<Enter>", lambda event: self.icon_clock_checked.
                                     configure(image=icon_clock_checked_blue))
        # evento é ativado quando mouse sai da imagem
        self.icon_clock_checked.bind("<Leave>", lambda event: self.icon_clock_checked.
                                     configure(image=icon_clock_checked_white))
        # função acontece quando é clicado na imagem
        self.icon_clock_checked.bind("<Button-1>", lambda event: self.open_acerto_ponto())

        self.icon_clock_schedule = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_schedule_white, text="")
        self.icon_clock_schedule.place(x=19, y=220)

        self.icon_clock_schedule.bind("<Enter>", lambda event: self.icon_clock_schedule.
                                      configure(image=icon_clock_schedule_blue))
        self.icon_clock_schedule.bind("<Leave>", lambda event: self.icon_clock_schedule.
                                      configure(image=icon_clock_schedule_white))
        self.icon_clock_schedule.bind("<Button-1>", lambda event: self.open_folha_ponto())

        self.icon_clock_logout = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_logout_white, text="")
        self.icon_clock_logout.place(x=19, y=310)

        self.icon_clock_logout.bind("<Enter>", lambda event: self.icon_clock_logout.
                                    configure(image=icon_clock_logout_blue))
        self.icon_clock_logout.bind("<Leave>", lambda event: self.icon_clock_logout.
                                    configure(image=icon_clock_logout_white))
        self.icon_clock_logout.bind("<Button-1>", lambda event: self.logout())

    def open_acerto_ponto(self):
        self.withdraw()  # fecha janela atual
        tela_acerto_ponto = TelaAcertoPonto(self, self, self)
        tela_acerto_ponto.mainloop()  # abre nova janela

    def open_folha_ponto(self):
        self.withdraw()  # fecha janela atual
        tela_folha_ponto = TelaFolhaPonto(self, self, self)  # criação da instância
        tela_folha_ponto.mainloop()  # abre nova janela

    def logout(self):
        self.destroy()
        tela_login = TelaLogin()
        tela_login.mainloop()


class TelaAcertoPonto(customtkinter.CTkToplevel):
    def __init__(self, tela_batida_ponto, tela_login, tela_folha_ponto, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tela_folha_ponto = tela_folha_ponto
        self.tela_batida_ponto = tela_batida_ponto
        self.tela_login = tela_login
        self.geometry("1200x800")
        self.title("Clockin - Acerto de Ponto")
        self.config(bg='#F9F9F9')

        # Declarations
        font_title = customtkinter.CTkFont(family='', size=23, weight='bold')

        logo = customtkinter.CTkImage(light_image=Image.open("images/logo-clockin.png"), size=(85, 85))

        icon_clock_add_white = customtkinter.CTkImage(light_image=Image.open("images/icon-clock-add-white.png"),
                                                      size=(52, 52))
        icon_clock_schedule_white = customtkinter.CTkImage(light_image=Image.
                                                           open("images/icon-view-schedule-white.png"), size=(52, 52))
        icon_clock_logout_white = customtkinter.CTkImage(light_image=Image.open("images/icon-logout-white.png"),
                                                         size=(52, 52))

        icon_clock_add_blue = customtkinter.CTkImage(light_image=Image.open("images/icon-clock-add-blue.png"),
                                                     size=(52, 52))
        icon_clock_checked_blue = customtkinter.CTkImage(light_image=Image.open("images/icon-clock-checked-blue.png"),
                                                         size=(52, 52))
        icon_clock_schedule_blue = customtkinter.CTkImage(light_image=Image.open("images/icon-view-schedule-blue.png"),
                                                          size=(52, 52))
        icon_clock_logout_blue = customtkinter.CTkImage(light_image=Image.open("images/icon-logout-blue.png"),
                                                        size=(52, 52))

        # Creation of elements

        # -- header --
        # gambiarra
        self.header12 = customtkinter.CTkFrame(self, width=1990, height=130, fg_color='#D2DDF9', bg_color='#F9F9F9')
        self.header12.place(relx=0.5, rely=0.06, anchor=tkinter.CENTER)

        self.header = customtkinter.CTkFrame(self, width=900, height=130, fg_color='#D2DDF9', bg_color='#D2DDF9')
        self.header.place(relx=0.5, rely=0.06, anchor=tkinter.CENTER)

        self.title = customtkinter.CTkLabel(master=self.header, text='Acerto de Ponto', text_color='#3F5B80',
                                            font=font_title)
        self.title.place(x=49, y=63)

        self.image_logo = customtkinter.CTkLabel(master=self.header, image=logo, text="", fg_color='#D2DDF9')
        self.image_logo.place(x=760, y=33)

        # --sidebar --
        self.sidebar = customtkinter.CTkFrame(self, width=90, height=400, fg_color='#D2DDF9', bg_color='#F9F9F9')
        self.sidebar.place(relx=0, rely=0.3)

        self.icon_clock_add = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_add_white, text="")
        self.icon_clock_add.place(x=19, y=40)

        # evento é ativado quando mouse passa sobre a imagem
        self.icon_clock_add.bind("<Enter>", lambda event: self.icon_clock_add.configure(image=icon_clock_add_blue))
        # evento é ativado quando mouse sai da imagem
        self.icon_clock_add.bind("<Leave>", lambda event: self.icon_clock_add.configure(image=icon_clock_add_white))
        # função acontece quando é clicado na imagem
        self.icon_clock_add.bind("<Button-1>", lambda event: self.open_batida_ponto())

        self.icon_clock_checked = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_checked_blue, text="")
        self.icon_clock_checked.place(x=19, y=130)

        self.icon_clock_schedule = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_schedule_white, text="")
        self.icon_clock_schedule.place(x=19, y=220)

        self.icon_clock_schedule.bind("<Enter>", lambda event: self.icon_clock_schedule.
                                      configure(image=icon_clock_schedule_blue))
        self.icon_clock_schedule.bind("<Leave>", lambda event: self.icon_clock_schedule.
                                      configure(image=icon_clock_schedule_white))
        self.icon_clock_schedule.bind("<Button-1>", lambda event: self.open_folha_ponto())

        self.icon_clock_logout = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_logout_white, text="")
        self.icon_clock_logout.place(x=19, y=310)

        self.icon_clock_logout.bind("<Enter>", lambda event: self.icon_clock_logout.
                                    configure(image=icon_clock_logout_blue))
        self.icon_clock_logout.bind("<Leave>", lambda event: self.icon_clock_logout.
                                    configure(image=icon_clock_logout_white))
        self.icon_clock_logout.bind("<Button-1>", lambda event: self.open_login())

    def open_batida_ponto(self):
        self.withdraw()  # fecha janela atual
        tela_batida_ponto = TelaBatidaPonto(self, self, self)  # criação da instância
        tela_batida_ponto.mainloop()  # abre nova janela

    def open_folha_ponto(self):
        self.withdraw()  # fecha janela atual
        tela_folha_ponto = TelaFolhaPonto(self, self, self)  # criação da instância
        tela_folha_ponto.mainloop()  # abre nova janela

    def open_login(self):
        self.withdraw()  # fecha janela atual
        tela_login = TelaLogin(self)
        tela_login.mainloop()  # abre nova janela


class TelaFolhaPonto(customtkinter.CTkToplevel):
    def __init__(self, tela_batida_ponto, tela_login, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tela_batida_ponto = tela_batida_ponto
        self.tela_login = tela_login
        self.geometry("1200x800")
        self.title("Clockin - Folha de Ponto")
        self.config(bg='#F9F9F9')

        # Declarations
        font_title = customtkinter.CTkFont(family='', size=23, weight='bold')

        logo = customtkinter.CTkImage(light_image=Image.open("images/logo-clockin.png"), size=(85, 85))

        icon_clock_add_white = customtkinter.CTkImage(light_image=Image.open("images/icon-clock-add-white.png"),
                                                      size=(52, 52))
        icon_clock_checked_white = customtkinter.CTkImage(light_image=Image.open("images/icon-clock-checked-white.png"),
                                                          size=(52, 52))
        icon_clock_logout_white = customtkinter.CTkImage(light_image=Image.open("images/icon-logout-white.png"),
                                                         size=(52, 52))

        icon_clock_add_blue = customtkinter.CTkImage(light_image=Image.open("images/icon-clock-add-blue.png"),
                                                     size=(52, 52))
        icon_clock_checked_blue = customtkinter.CTkImage(light_image=Image.open("images/icon-clock-checked-blue.png"),
                                                         size=(52, 52))
        icon_clock_schedule_blue = customtkinter.CTkImage(light_image=Image.open("images/icon-view-schedule-blue.png"),
                                                          size=(52, 52))
        icon_clock_logout_blue = customtkinter.CTkImage(light_image=Image.open("images/icon-logout-blue.png"),
                                                        size=(52, 52))

        # Creation of elements

        # -- header --
        # gambiarra
        self.header1 = customtkinter.CTkFrame(self, width=1990, height=130, fg_color='#D2DDF9', bg_color='#F9F9F9')
        self.header1.place(relx=0.5, rely=0.06, anchor=tkinter.CENTER)

        self.header = customtkinter.CTkFrame(self, width=900, height=130, fg_color='#D2DDF9', bg_color='#D2DDF9')
        self.header.place(relx=0.5, rely=0.06, anchor=tkinter.CENTER)

        self.title = customtkinter.CTkLabel(master=self.header, text='Folha de Ponto', text_color='#3F5B80',
                                            font=font_title)
        self.title.place(x=49, y=63)

        self.image_logo = customtkinter.CTkLabel(master=self.header, image=logo, text="", fg_color='#D2DDF9')
        self.image_logo.place(x=760, y=33)

        # --sidebar --
        self.sidebar = customtkinter.CTkFrame(self, width=90, height=400, fg_color='#D2DDF9', bg_color='#F9F9F9')
        self.sidebar.place(relx=0, rely=0.3)

        self.icon_clock_add = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_add_white, text="")
        self.icon_clock_add.place(x=19, y=40)

        # evento é ativado quando mouse passa sobre a imagem
        self.icon_clock_add.bind("<Enter>", lambda event: self.icon_clock_add.configure(image=icon_clock_add_blue))
        # evento é ativado quando mouse sai da imagem
        self.icon_clock_add.bind("<Leave>", lambda event: self.icon_clock_add.configure(image=icon_clock_add_white))
        # função acontece quando é clicado na imagem
        self.icon_clock_add.bind("<Button-1>", lambda event: self.open_batida_ponto())

        self.icon_clock_checked = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_checked_white, text="")
        self.icon_clock_checked.place(x=19, y=130)

        self.icon_clock_checked.bind("<Enter>", lambda event: self.icon_clock_checked.
                                     configure(image=icon_clock_checked_blue))
        self.icon_clock_checked.bind("<Leave>", lambda event: self.icon_clock_checked.
                                     configure(image=icon_clock_checked_white))
        self.icon_clock_checked.bind("<Button-1>", lambda event: self.open_acerto_ponto())

        self.icon_clock_schedule = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_schedule_blue, text="")
        self.icon_clock_schedule.place(x=19, y=220)

        self.icon_clock_logout = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_logout_white, text="")
        self.icon_clock_logout.place(x=19, y=310)

        self.icon_clock_logout.bind("<Enter>", lambda event: self.icon_clock_logout.
                                    configure(image=icon_clock_logout_blue))
        self.icon_clock_logout.bind("<Leave>", lambda event: self.icon_clock_logout.
                                    configure(image=icon_clock_logout_white))
        self.icon_clock_logout.bind("<Button-1>", lambda event: self.open_login())

    def open_batida_ponto(self):
        self.withdraw()  # fecha janela atual
        tela_batida_ponto = TelaBatidaPonto(self, self, self)  # criação da instância
        tela_batida_ponto.mainloop()  # abre nova janela

    def open_acerto_ponto(self):
        self.withdraw()  # fecha janela atual
        tela_acerto_ponto = TelaAcertoPonto(self, self, self)  # criação da instância
        tela_acerto_ponto.mainloop()  # abre nova janela

    def open_login(self):
        self.withdraw()  # fecha janela atual
        tela_login = TelaLogin(self)
        tela_login.mainloop()  # abre nova janela


# Functions
# if __name__ == "__main__":
#     # Criar a primeira janela de login
#     tela_login = TelaLogin()
#     tela_login.mainloop()


def clique():
    print("Login realizado")


def troca():
    print("Cadastro pronto")


app = TelaPrincipal()
app.mainloop()
