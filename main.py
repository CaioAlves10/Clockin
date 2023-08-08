import customtkinter
from PIL import Image
import mysql.connector
import tkinter as tk
from tkinter import ttk
import tkinter.font
from tkinter import messagebox
import datetime
from tkcalendar import Calendar

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")


def connect():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='year@2023.caio',
            database='clockin_db'
        )
        if conn.is_connected():
            print('Conexão bem-sucedida ao banco de dados.')
            return conn
    except mysql.connector.Error as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
        messagebox.showerror('Erro', 'Erro ao conectar ao banco de dados.')


def close_connection(conn):
    if conn.is_connected():
        conn.close()
        print('Conexão ao banco de dados fechada.')


def atualizar_status_batida(status):
    try:
        conn = connect()
        cursor = conn.cursor()

        # Atualizar o status na tabela
        query = "UPDATE batidas_ponto SET status_ = %s WHERE status_ = %s"
        valores = (status, "validando")
        cursor.execute(query, valores)
        conn.commit()

        cursor.close()
        close_connection(conn)

    except Exception as e:
        print(f"Erro ao atualizar o status da batida de ponto: {e}")


class App(customtkinter.CTk):
    def __init__(self, root):
        super().__init__()
        self.motivo = None
        self.subtitle_motivo = None
        self.frame_hora_entrada = None
        self.saida = None
        self.subtitle_saida = None
        self.frame_hora_saida = None
        self.entrada = None
        self.subtitle_entrada = None
        self.calendar = None
        self.subtitle_data = None
        self.fazendo_acerto_button = None
        self.title_acerto = None
        self.id_user = None
        self.frame_horario = None
        self.horario = None
        self.title_batida = None
        self.batendo_ponto_button = None
        self.tela_bater_ponto = None
        self.logar = None
        self.config = None
        self.current_page = None
        self.tela_cadastro = None
        self.tela_login = None
        self.root = root
        self.pages = []

        # Criar páginas
        tela_login = customtkinter.CTkFrame(root)
        self.pages.append(tela_login)  # 0

        tela_cadastro = customtkinter.CTkFrame(root)
        self.pages.append(tela_cadastro)  # 1

        tela_batida_ponto = customtkinter.CTkFrame(root)
        self.pages.append(tela_batida_ponto)  # 2

        tela_acerto_ponto = customtkinter.CTkFrame(root)
        self.pages.append(tela_acerto_ponto)  # 3

        tela_folha_ponto = customtkinter.CTkFrame(root)
        self.pages.append(tela_folha_ponto)  # 4

        self.tela_login = self.pages[0]
        self.tela_cadastro = self.pages[1]
        self.tela_batida_ponto = self.pages[2]
        self.tela_acerto_ponto = self.pages[3]
        self.tela_folha_ponto = self.pages[4]

        # Declarations
        font_title = customtkinter.CTkFont(family='', size=20, weight='bold')
        font_button = customtkinter.CTkFont(family='', size=14, weight='bold')
        font_link = customtkinter.CTkFont(family='inter', size=13, weight='bold', underline=True)
        font_creator = customtkinter.CTkFont(family='inter', size=15)

        logo = customtkinter.CTkImage(light_image=Image.open("images/logo-clockin.png"), size=(110, 110))
        text_logo = customtkinter.CTkImage(light_image=Image.open("images/text-clockin.png"), size=(130, 30))

        font_title_header = customtkinter.CTkFont(family='', size=23, weight='bold')

        logo_header = customtkinter.CTkImage(light_image=Image.open("images/logo-clockin.png"), size=(85, 85))

        icon_clock_add_white = customtkinter.CTkImage(light_image=Image.open("images/icon-clock-add-white.png"),
                                                      size=(52, 52))

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

        # Adicionar widgets à page tela_login
        # Creation of elements
        self.bg_tela_login = customtkinter.CTkFrame(self.tela_login, width=30, height=255, corner_radius=15,
                                                    fg_color='#D2DDF9', bg_color='#D2DDF9')
        self.bg_tela_login.pack(fill='both')

        self.image_logo = customtkinter.CTkLabel(self.bg_tela_login, image=logo, text="",
                                                 fg_color='#D2DDF9',
                                                 bg_color='#D2DDF9')  # display image with a CTkLabel
        self.image_logo.pack(pady=(55, 0), ipadx=0, fill='both')

        self.image_text_logo = customtkinter.CTkLabel(self.bg_tela_login, image=text_logo, text="",
                                                      fg_color='#D2DDF9',
                                                      bg_color='#D2DDF9')  # display image with a CTkLabel
        self.image_text_logo.pack(pady=20, fill='both')

        self.frame_login = customtkinter.CTkFrame(self.bg_tela_login, width=400, height=255, corner_radius=15,
                                                  fg_color='#F2F2F2', bg_color='#D2DDF9')
        self.frame_login.pack(pady=(20, 0))

        self.title = customtkinter.CTkLabel(master=self.frame_login, text='Logar:', text_color='#7D7987',
                                            font=font_title)
        self.title.place(x=35, y=30)

        self.login_logar = customtkinter.CTkEntry(master=self.frame_login, width=330, height=40,
                                                  placeholder_text="Seu login")
        self.login_logar.place(x=35, y=70)

        self.password_logar = customtkinter.CTkEntry(master=self.frame_login, width=330, height=40,
                                                     placeholder_text="Sua senha", show="*")
        self.password_logar.place(x=35, y=130)

        self.login_button = customtkinter.CTkButton(master=self.frame_login, width=100, height=40, text='LOGIN',
                                                    corner_radius=6, font=font_button, fg_color='#FAA115',
                                                    hover_color='#FBA827', command=self.fazer_login)
        self.login_button.place(x=150, y=190)

        self.cadastro_link = customtkinter.CTkButton(master=self.bg_tela_login, text='CADASTRE-SE',
                                                     text_color='#3F5B80',
                                                     fg_color='transparent', bg_color='#D2DDF9', hover=False,
                                                     font=font_link, command=self.open_cadastro)
        self.cadastro_link.pack(pady=(30, 0))

        self.creator = customtkinter.CTkLabel(self.bg_tela_login, text='Criado por Caio Carvalho', text_color='#545454',
                                              bg_color='#D2DDF9', font=font_creator)
        self.creator.pack(pady=(130, 10), fill='both')

        # Adicionar widgets à page tela_cadastro
        # Creation of elements
        self.bg_tela_cadastro = customtkinter.CTkFrame(self.tela_cadastro, width=30, height=255, corner_radius=15,
                                                       fg_color='#D2DDF9', bg_color='#D2DDF9')
        self.bg_tela_cadastro.pack(fill='both')

        self.image_logo = customtkinter.CTkLabel(self.bg_tela_cadastro, image=logo, text="",
                                                 fg_color='#D2DDF9')  # display image with a CTkLabel
        self.image_logo.pack(pady=(55, 0))

        self.image_text_logo = customtkinter.CTkLabel(self.bg_tela_cadastro, image=text_logo, text="",
                                                      fg_color='#D2DDF9')  # display image with a CTkLabel
        self.image_text_logo.pack(pady=20)

        self.frame_cadastro = customtkinter.CTkFrame(self.bg_tela_cadastro, width=400, height=255, corner_radius=15,
                                                     fg_color='#F2F2F2', bg_color='#D2DDF9')
        self.frame_cadastro.pack(pady=(20, 0))

        self.title = customtkinter.CTkLabel(master=self.frame_cadastro, text='Cadastrar:', text_color='#7D7987',
                                            font=font_title)
        self.title.place(x=35, y=30)

        self.login_cadastrar = customtkinter.CTkEntry(master=self.frame_cadastro, width=330, height=40,
                                                      placeholder_text="Seu login")
        self.login_cadastrar.place(x=35, y=70)

        self.password_cadastrar = customtkinter.CTkEntry(master=self.frame_cadastro, width=330, height=40,
                                                         placeholder_text="Sua senha", show="*")
        self.password_cadastrar.place(x=35, y=130)

        self.cadastro_button = customtkinter.CTkButton(master=self.frame_cadastro, width=100, height=40,
                                                       text='CADASTRAR', corner_radius=6, font=font_button,
                                                       fg_color='#FAA115', hover_color='#FBA827',
                                                       command=self.fazer_cadastro)
        self.cadastro_button.place(x=150, y=190)

        self.login_link = customtkinter.CTkButton(self.bg_tela_cadastro, text='LOGAR', text_color='#3F5B80',
                                                  fg_color='transparent', bg_color='#D2DDF9', hover=False,
                                                  font=font_link, command=self.open_login)
        self.login_link.pack(pady=(30, 0))

        self.creator = customtkinter.CTkLabel(self.bg_tela_cadastro, text='Criado por Caio Carvalho',
                                              text_color='#545454', bg_color='#D2DDF9', font=font_creator)
        self.creator.pack(pady=(130, 10))

        # Adicionar widgets à page tela_batida_ponto
        self.bg_tela_batida_ponto = customtkinter.CTkFrame(self.tela_batida_ponto, width=30, height=255,
                                                           corner_radius=15, fg_color='#F9F9F9', bg_color='#D2DDF9')
        self.bg_tela_batida_ponto.pack(fill='both')
        # -- header --
        self.header1 = customtkinter.CTkFrame(self.bg_tela_batida_ponto, corner_radius=0, width=1990, height=130,
                                              fg_color='#D2DDF9', bg_color='#F9F9F9')  # gambiarra
        self.header1.pack()

        self.header = customtkinter.CTkFrame(self.header1, width=900, height=130, fg_color='#D2DDF9',
                                             bg_color='#D2DDF9')
        self.header.place(relx=0.5, rely=0.5, anchor='center')

        self.title_header = customtkinter.CTkLabel(master=self.header, text='Batida de Ponto', text_color='#3F5B80',
                                                   font=font_title_header)
        self.title_header.place(x=55, y=54)

        self.image_logo = customtkinter.CTkLabel(master=self.header, image=logo_header, text="", fg_color='#D2DDF9')
        self.image_logo.place(x=760, y=22.50)

        # --sidebar --
        self.sidebar = customtkinter.CTkFrame(self.bg_tela_batida_ponto, width=90, height=408, fg_color='#D2DDF9',
                                              bg_color='#F9F9F9')
        self.sidebar.pack(side='left', pady=110, fill='both')

        self.icon_clock_add = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_add_blue, text="")
        self.icon_clock_add.place(x=19, y=30)

        self.icon_clock_checked = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_checked_white, text="")
        self.icon_clock_checked.place(x=19, y=122)

        # evento é ativado quando mouse passa sobre a imagem
        self.icon_clock_checked.bind("<Enter>", lambda event: self.icon_clock_checked.
                                     configure(image=icon_clock_checked_blue))
        # evento é ativado quando mouse sai da imagem
        self.icon_clock_checked.bind("<Leave>", lambda event: self.icon_clock_checked.
                                     configure(image=icon_clock_checked_white))
        # função acontece quando é clicado na imagem
        self.icon_clock_checked.bind("<Button-1>", lambda event: self.open_acerto_ponto())

        self.icon_clock_schedule = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_schedule_white, text="")
        self.icon_clock_schedule.place(x=19, y=214)

        self.icon_clock_schedule.bind("<Enter>", lambda event: self.icon_clock_schedule.
                                      configure(image=icon_clock_schedule_blue))
        self.icon_clock_schedule.bind("<Leave>", lambda event: self.icon_clock_schedule.
                                      configure(image=icon_clock_schedule_white))
        self.icon_clock_schedule.bind("<Button-1>", lambda event: self.open_folha_ponto())

        self.icon_clock_logout = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_logout_white, text="")
        self.icon_clock_logout.place(x=19, y=306)

        self.icon_clock_logout.bind("<Enter>", lambda event: self.icon_clock_logout.
                                    configure(image=icon_clock_logout_blue))
        self.icon_clock_logout.bind("<Leave>", lambda event: self.icon_clock_logout.
                                    configure(image=icon_clock_logout_white))
        self.icon_clock_logout.bind("<Button-1>", lambda event: self.open_login())

        self.content = customtkinter.CTkFrame(self.bg_tela_batida_ponto, width=0, height=800, fg_color='#F9F9F9')
        self.content.pack(fill='both', expand=True)

        self.batidas_ponto_button = customtkinter.CTkButton(master=self.content, width=100, height=40, text='Ponto',
                                                            corner_radius=6, font=font_button, fg_color='#FAA115',
                                                            hover_color='#FBA827', command=self.open_tela_bater_ponto)
        self.batidas_ponto_button.pack(anchor='w', padx=100, pady=(50, 0))

        self.frame_borda = customtkinter.CTkFrame(self.content, fg_color="#FDA721", bg_color="#F9F9F9")
        self.frame_borda.pack(fill='both', expand=True, padx=100, pady=(20, 50))

        # Estilizar a tabela
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview",
                        background="#FFFFFF",
                        foreground="#000",
                        rowheight=30,
                        fieldbackground="#F2F2F2",
                        bordercolor="#000",
                        borderwidth=0,
                        font=("Helvetica", 10))
        style.map('Treeview', background=[('selected', '#FFD964')])

        # Estilizar os cabeçalhos
        style.configure("Treeview.Heading",
                        background="#FDA721",
                        foreground="white",
                        relief="flat",
                        font=("Helvetica", 10, "bold"))
        style.map("Treeview.Heading",
                  background=[('active', '#FDA721')])

        # Criar um widget Treeview - tabela
        self.table_batidas_ponto = ttk.Treeview(self.frame_borda, style="Treeview")
        self.table_batidas_ponto["columns"] = ("id_batida", "col1", "col2", "col3")

        # Configurar as colunas para exibir o cabeçalho e definir o tamanho
        self.table_batidas_ponto.column("#0", width=0, stretch=tk.NO)
        self.table_batidas_ponto.column("id_batida", anchor=tk.CENTER, width=60)
        self.table_batidas_ponto.column("col1", anchor=tk.CENTER, width=100)
        self.table_batidas_ponto.column("col2", anchor=tk.CENTER, width=100)
        self.table_batidas_ponto.column("col3", anchor=tk.CENTER, width=100)

        # Defina os cabeçalhos das colunas
        self.table_batidas_ponto.heading("#0", text="", anchor=tk.CENTER)
        self.table_batidas_ponto.heading("id_batida", text="ID", anchor=tk.CENTER)
        self.table_batidas_ponto.heading("col1", text="DATA", anchor=tk.CENTER)
        self.table_batidas_ponto.heading("col2", text="BATIDA", anchor=tk.CENTER)
        self.table_batidas_ponto.heading("col3", text="STATUS", anchor=tk.CENTER)

        # Definir quais colunas devem ser exibidas (exceto a primeira que está vazia)
        self.table_batidas_ponto["displaycolumns"] = ("id_batida", "col1", "col2", "col3")

        self.scrollbar_x = customtkinter.CTkScrollbar(self.frame_borda, orientation="horizontal",
                                                      button_color="#CFCFCF", button_hover_color="#D9D9D9",
                                                      command=self.table_batidas_ponto.xview)
        self.scrollbar_x.pack(side="bottom", fill="x")
        self.table_batidas_ponto.configure(xscrollcommand=self.scrollbar_x.set)

        self.scrollbar_y = customtkinter.CTkScrollbar(self.frame_borda, orientation="vertical",
                                                      button_color="#CFCFCF", button_hover_color="#D9D9D9",
                                                      command=self.table_batidas_ponto.yview)
        self.scrollbar_y.pack(side="right", fill="y")
        self.table_batidas_ponto.configure(yscrollcommand=self.scrollbar_y.set)

        self.table_batidas_ponto.pack(fill='both', padx=5, pady=5, expand=True)

        # Adicionar widgets à page tela_acerto_ponto
        self.bg_tela_acerto_ponto = customtkinter.CTkFrame(self.tela_acerto_ponto, width=30, height=255,
                                                           corner_radius=15, fg_color='#F9F9F9', bg_color='#D2DDF9')
        self.bg_tela_acerto_ponto.pack(fill='both')
        # -- header --
        self.header1 = customtkinter.CTkFrame(self.bg_tela_acerto_ponto, corner_radius=0, width=1990, height=130,
                                              fg_color='#D2DDF9', bg_color='#F9F9F9')  # gambiarra
        self.header1.pack()

        self.header = customtkinter.CTkFrame(self.header1, width=900, height=130, fg_color='#D2DDF9',
                                             bg_color='#D2DDF9')
        self.header.place(relx=0.5, rely=0.5, anchor='center')

        self.title_header = customtkinter.CTkLabel(master=self.header, text='Acerto de Ponto', text_color='#3F5B80',
                                                   font=font_title_header)
        self.title_header.place(x=55, y=54)

        self.image_logo = customtkinter.CTkLabel(master=self.header, image=logo_header, text="", fg_color='#D2DDF9')
        self.image_logo.place(x=760, y=22.50)

        # --sidebar --
        self.sidebar = customtkinter.CTkFrame(self.bg_tela_acerto_ponto, width=90, height=408, fg_color='#D2DDF9',
                                              bg_color='#F9F9F9')
        self.sidebar.pack(side='left', pady=110, fill='both')

        self.icon_clock_add_acerto = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_add_white, text="")
        self.icon_clock_add_acerto.place(x=19, y=30)

        self.icon_clock_add_acerto.bind("<Enter>", lambda event: self.icon_clock_add_acerto.
                                        configure(image=icon_clock_add_blue))

        self.icon_clock_add_acerto.bind("<Leave>", lambda event: self.icon_clock_add_acerto.
                                        configure(image=icon_clock_add_white))

        self.icon_clock_add_acerto.bind("<Button-1>", lambda event: self.open_batida_ponto())

        self.icon_clock_checked_acerto = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_checked_blue,
                                                                text="")
        self.icon_clock_checked_acerto.place(x=19, y=122)

        self.icon_clock_schedule_acerto = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_schedule_white,
                                                                 text="")
        self.icon_clock_schedule_acerto.place(x=19, y=214)

        self.icon_clock_schedule_acerto.bind("<Enter>", lambda event: self.icon_clock_schedule_acerto.
                                             configure(image=icon_clock_schedule_blue))
        self.icon_clock_schedule_acerto.bind("<Leave>", lambda event: self.icon_clock_schedule_acerto.
                                             configure(image=icon_clock_schedule_white))
        self.icon_clock_schedule_acerto.bind("<Button-1>", lambda event: self.open_folha_ponto())

        self.icon_clock_logout_acerto = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_logout_white,
                                                               text="")
        self.icon_clock_logout_acerto.place(x=19, y=306)

        self.icon_clock_logout_acerto.bind("<Enter>", lambda event: self.icon_clock_logout_acerto.
                                           configure(image=icon_clock_logout_blue))
        self.icon_clock_logout_acerto.bind("<Leave>", lambda event: self.icon_clock_logout_acerto.
                                           configure(image=icon_clock_logout_white))
        self.icon_clock_logout_acerto.bind("<Button-1>", lambda event: self.open_login())

        self.content = customtkinter.CTkFrame(self.bg_tela_acerto_ponto, width=0, height=800, fg_color='#F9F9F9')
        self.content.pack(fill='both', expand=True)

        self.acerto_ponto_button = customtkinter.CTkButton(master=self.content, width=100, height=40, text='Acerto',
                                                           corner_radius=6, font=font_button, fg_color='#FAA115',
                                                           hover_color='#FBA827', command=self.open_tela_acerto_ponto)
        self.acerto_ponto_button.pack(anchor='w', padx=100, pady=(50, 0))

        self.frame_borda = customtkinter.CTkFrame(self.content, fg_color="#FDA721", bg_color="#F9F9F9")
        self.frame_borda.pack(fill='both', expand=True, padx=100, pady=(20, 50))

        # Criar um widget Treeview - tabela
        self.table_acertos_ponto = ttk.Treeview(self.frame_borda, style="Treeview")
        self.table_acertos_ponto["columns"] = ("id_acerto", "col1", "col2", "col3", "col4", "col5")

        # Configurar as colunas para exibir o cabeçalho e definir o tamanho
        self.table_acertos_ponto.column("#0", width=0, stretch=tk.NO)
        self.table_acertos_ponto.column("id_acerto", anchor=tk.CENTER, width=60)
        self.table_acertos_ponto.column("col1", anchor=tk.CENTER, width=100)
        self.table_acertos_ponto.column("col2", anchor=tk.CENTER, width=100)
        self.table_acertos_ponto.column("col3", anchor=tk.CENTER, width=100)
        self.table_acertos_ponto.column("col4", anchor=tk.CENTER, width=100)
        self.table_acertos_ponto.column("col5", anchor=tk.CENTER, width=100)

        # Definir os cabeçalhos das colunas
        self.table_acertos_ponto.heading("#0", text="", anchor=tk.CENTER)
        self.table_acertos_ponto.heading("id_acerto", text="ID", anchor=tk.CENTER)
        self.table_acertos_ponto.heading("col1", text="DATA ACERTO", anchor=tk.CENTER)
        self.table_acertos_ponto.heading("col2", text="ENTRADA", anchor=tk.CENTER)
        self.table_acertos_ponto.heading("col3", text="SAIDA", anchor=tk.CENTER)
        self.table_acertos_ponto.heading("col4", text="MOTIVO", anchor=tk.CENTER)
        self.table_acertos_ponto.heading("col5", text="STATUS", anchor=tk.CENTER)

        # Definir quais colunas devem ser exibidas (exceto a primeira que está vazia)
        self.table_acertos_ponto["displaycolumns"] = ("id_acerto", "col1", "col2", "col3", "col4", "col5")

        self.scrollbar_x = customtkinter.CTkScrollbar(self.frame_borda, orientation="horizontal",
                                                      button_color="#CFCFCF", button_hover_color="#D9D9D9",
                                                      command=self.table_acertos_ponto.xview)
        self.scrollbar_x.pack(side="bottom", fill="x")
        self.table_acertos_ponto.configure(xscrollcommand=self.scrollbar_x.set)

        self.scrollbar_y = customtkinter.CTkScrollbar(self.frame_borda, orientation="vertical",
                                                      button_color="#CFCFCF", button_hover_color="#D9D9D9",
                                                      command=self.table_acertos_ponto.yview)
        self.scrollbar_y.pack(side="right", fill="y")
        self.table_acertos_ponto.configure(yscrollcommand=self.scrollbar_y.set)

        self.table_acertos_ponto.pack(fill='both', padx=5, pady=5, expand=True)

        # Adicionar widgets à page tela_folha_ponto
        self.bg_tela_folha_ponto = customtkinter.CTkFrame(self.tela_folha_ponto, width=30, height=255,
                                                          corner_radius=15, fg_color='#F9F9F9', bg_color='#D2DDF9')
        self.bg_tela_folha_ponto.pack(fill='both')
        # -- header --
        self.header1 = customtkinter.CTkFrame(self.bg_tela_folha_ponto, corner_radius=0, width=1990, height=130,
                                              fg_color='#D2DDF9', bg_color='#F9F9F9')  # gambiarra
        self.header1.pack()

        self.header = customtkinter.CTkFrame(self.header1, width=900, height=130, fg_color='#D2DDF9',
                                             bg_color='#D2DDF9')
        self.header.place(relx=0.5, rely=0.5, anchor='center')

        self.title_header = customtkinter.CTkLabel(master=self.header, text='Folha Ponto', text_color='#3F5B80',
                                                   font=font_title_header)
        self.title_header.place(x=55, y=54)

        self.image_logo = customtkinter.CTkLabel(master=self.header, image=logo_header, text="", fg_color='#D2DDF9')
        self.image_logo.place(x=760, y=22.50)

        # --sidebar --
        self.sidebar = customtkinter.CTkFrame(self.bg_tela_folha_ponto, width=90, height=408, fg_color='#D2DDF9',
                                              bg_color='#F9F9F9')
        self.sidebar.pack(side='left', pady=110, fill='both')

        self.content = customtkinter.CTkFrame(self.bg_tela_folha_ponto, width=0, height=800, fg_color='#F9F9F9')
        self.content.pack(fill='both', expand=True)

        self.icon_clock_add_folha = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_add_white, text="")
        self.icon_clock_add_folha.place(x=19, y=30)

        self.icon_clock_add_folha.bind("<Enter>", lambda event: self.icon_clock_add_folha.
                                       configure(image=icon_clock_add_blue))

        self.icon_clock_add_folha.bind("<Leave>", lambda event: self.icon_clock_add_folha.
                                       configure(image=icon_clock_add_white))

        self.icon_clock_add_folha.bind("<Button-1>", lambda event: self.open_batida_ponto())

        self.icon_clock_checked_folha = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_checked_white,
                                                               text="")
        self.icon_clock_checked_folha.place(x=19, y=122)

        self.icon_clock_checked_folha.bind("<Enter>", lambda event: self.icon_clock_checked_folha.
                                           configure(image=icon_clock_checked_blue))

        self.icon_clock_checked_folha.bind("<Leave>", lambda event: self.icon_clock_checked_folha.
                                           configure(image=icon_clock_checked_white))

        self.icon_clock_checked_folha.bind("<Button-1>", lambda event: self.open_acerto_ponto())

        self.icon_clock_schedule_folha = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_schedule_blue,
                                                                text="")
        self.icon_clock_schedule_folha.place(x=19, y=214)

        self.icon_clock_logout_folha = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_logout_white,
                                                              text="")
        self.icon_clock_logout_folha.place(x=19, y=306)

        self.icon_clock_logout_folha.bind("<Enter>", lambda event: self.icon_clock_logout_folha.
                                          configure(image=icon_clock_logout_blue))

        self.icon_clock_logout_folha.bind("<Leave>", lambda event: self.icon_clock_logout_folha.
                                          configure(image=icon_clock_logout_white))

        self.icon_clock_logout_folha.bind("<Button-1>", lambda event: self.open_login())

        # Mostrar a page inicial
        self.open_login()

    def fazer_cadastro(self):
        login = self.login_cadastrar.get()
        password = self.password_cadastrar.get()

        # Verificar se os campos não estão vazios
        if not login or not password:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        # Verificar se a senha tem pelo menos 8 caracteres
        if len(password) < 8:
            messagebox.showerror("Erro", "A senha deve ter no mínimo 8 caracteres")
            return

        try:
            conn = connect()
            cursor = conn.cursor()

            # Verifica se o login já existe no banco de dados
            query_verificar_login = "SELECT COUNT(*) FROM cadastro WHERE login = %s"
            cursor.execute(query_verificar_login, (login,))
            resultado = cursor.fetchone()

            if resultado[0] > 0:
                messagebox.showerror("Erro", "O login já está em uso.")
                return

            query = f"INSERT INTO cadastro (login, senha) VALUES (%s, %s)"
            valores = (login, password)
            cursor.execute(query, valores)
            conn.commit()
            cursor.close()
            close_connection(conn)

            messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")

            # Limpar os campos de entrada
            self.login_cadastrar.delete(0, "end")
            self.password_cadastrar.delete(0, "end")

        except mysql.connector.Error as error:
            messagebox.showerror("Erro", f"Não foi possível cadastrar: {error}")

    def fazer_login(self):
        login = self.login_logar.get()
        password = self.password_logar.get()

        # Verificar se os campos não estão vazios
        if not login or not password:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        try:
            conn = connect()
            cursor = conn.cursor()

            # Verificar se o login e a senha coincidem no banco de dados
            query_verificar_login_senha = "SELECT COUNT(*) FROM cadastro WHERE login = %s AND senha = %s"
            cursor.execute(query_verificar_login_senha, (login, password))
            resultado = cursor.fetchone()

            if resultado[0] == 0:
                messagebox.showerror("Erro", "Login e/ou senha incorretos.")
                return

            query_pegar_id_user = "SELECT id_user FROM cadastro WHERE login = %s"
            cursor.execute(query_pegar_id_user, (login,))
            id_user = cursor.fetchone()[0]

            self.id_user = id_user

            cursor.close()
            close_connection(conn)

            messagebox.showinfo("Login", "Login realizado com sucesso!")

            self.atualizar_tabela_batidas_ponto()
            self.atualizar_tabela_acertos_ponto()

            # Limpar os campos de entrada
            self.login_logar.delete(0, "end")
            self.password_logar.delete(0, "end")

            self.show_page(2)

        except mysql.connector.Error as error:
            messagebox.showerror("Erro", f"Não foi possível fazer login: {error}")

    def open_tela_bater_ponto(self):
        self.tela_bater_ponto = customtkinter.CTkToplevel(root)
        self.tela_bater_ponto.title("Batida de Ponto")
        self.tela_bater_ponto.geometry("400x300")
        self.tela_bater_ponto.config(bg='#FFFFFF')

        font_title = customtkinter.CTkFont(family='', size=25, weight='bold')
        font_button = customtkinter.CTkFont(family='', size=14, weight='bold')

        self.title_batida = customtkinter.CTkLabel(master=self.tela_bater_ponto, text='Nova batida', text_color='#3F5B80',
                                                   bg_color='#FFFFFF', font=font_title)
        self.title_batida.pack(pady=(20, 0))

        self.frame_horario = customtkinter.CTkFrame(master=self.tela_bater_ponto, corner_radius=6, fg_color='#F2F2F2',
                                                    bg_color='#FFFFFF')
        self.frame_horario.pack(anchor='center', pady=45)

        # Rótulo para mostrar o horário atual em tempo real
        self.horario = customtkinter.CTkLabel(master=self.frame_horario, text="", font=("Helvetica", 50))
        self.horario.pack(padx=10, pady=10)

        self.batendo_ponto_button = customtkinter.CTkButton(master=self.tela_bater_ponto, width=100, height=40,
                                                            text='Bater ponto', corner_radius=6, font=font_button,
                                                            fg_color='#FAA115', hover_color='#FBA827',
                                                            command=self.nova_batida)
        self.batendo_ponto_button.pack(side='bottom', pady=(0, 20))

        # Atualizar o rótulo com o horário atual em tempo real
        self.root.after(1000, self.mostrar_horario_atual)

    def mostrar_horario_atual(self):
        horario_atual = datetime.datetime.now().strftime("%H:%M:%S")
        self.horario.configure(text=horario_atual)
        root.after(1000, self.mostrar_horario_atual)  # Atualizar a cada 1000 milissegundos (1 segundo)

    def nova_batida(self):
        # Obter o dia e o horário atual
        dia_atual = datetime.datetime.now().strftime("%Y-%m-%d")
        horario_atual = datetime.datetime.now().strftime("%H:%M:%S")

        tipo = "entrada"
        status = "validando"

        try:
            conn = connect()
            cursor = conn.cursor()

            # Verificar se o usuário já realizou batidas no dia atual
            query_verificar_batidas = \
                "SELECT tipo, hora FROM batidas_ponto WHERE id_user = %s AND dia = %s ORDER BY id_batida DESC LIMIT 1"
            cursor.execute(query_verificar_batidas, (self.id_user, dia_atual))
            resultado = cursor.fetchone()

            # Se já existir batida para o usuário no dia atual, alternar o valor do atributo "tipo"
            if resultado:
                tipo_anterior = resultado[0]
                print("Resultado da consulta:", resultado)
                tipo = "saida" if tipo_anterior == "entrada" else "entrada"

                # Obter o horário da última batida
                hora_ultima_batida = resultado[1]
                # Converter timedelta para string no formato HH:MM:SS
                hora_ultima_batida_str = str(hora_ultima_batida)
                # Converter a string hora_ultima_batida_str para o tipo time
                hora_ultima_batida_obj = datetime.datetime.strptime(hora_ultima_batida_str, "%H:%M:%S").time()

                # Converter a string horario_atual para o tipo time
                horario_atual_obj = datetime.datetime.strptime(horario_atual, "%H:%M:%S").time()

                # Verificar a diferença de tempo entre a última batida e o horário atual
                diff_horarios = datetime.datetime.combine(datetime.date.min, horario_atual_obj) - datetime.datetime.combine(datetime.date.min, hora_ultima_batida_obj)

                # Se a diferença for menor que 15 minutos, não permitir a batida
                if diff_horarios.total_seconds() < 15 * 60:
                    self.tela_bater_ponto.destroy()
                    messagebox.showerror("Erro", "Não é permitido bater o ponto com menos de 15 minutos de intervalo.")
                    return

            # Inserir os valores na tabela
            query = "INSERT INTO batidas_ponto (id_user, dia, hora, tipo, status_) VALUES (%s, %s, %s,%s, %s)"
            valores = (self.id_user, dia_atual, horario_atual, tipo, status)
            cursor.execute(query, valores)
            conn.commit()

            cursor.close()
            close_connection(conn)

            # Atualizar o status para "ok" após a inserção bem-sucedida
            atualizar_status_batida("ok")
            print("Batida de ponto registrada com sucesso!")

            self.atualizar_tabela_batidas_ponto()
            self.tela_bater_ponto.destroy()

        except Exception as e:
            print(f"Erro ao registrar a batida de ponto: {e}")
            # Atualizar o status para "erro" em caso de erro na inserção
            atualizar_status_batida("erro")

    def atualizar_tabela_batidas_ponto(self):
        # Limpar os dados existentes na tabela
        self.table_batidas_ponto.delete(*self.table_batidas_ponto.get_children())

        try:
            conn = connect()
            cursor = conn.cursor()

            # Consultar as batidas de ponto do usuário
            query_consulta_batidas = \
                "SELECT id_batida, dia, hora, tipo, status_ FROM batidas_ponto WHERE id_user = %s ORDER BY id_batida DESC"
            cursor.execute(query_consulta_batidas, (self.id_user,))
            resultados = cursor.fetchall()

            # Inserir os dados na tabela
            for resultado in resultados:
                id_batida = resultado[0]
                dia_formatado = resultado[1].strftime("%d/%m/%Y")
                hora_formatada = resultado[2].strftime("%H:%M:%S") if isinstance(resultado[2], datetime.time) else \
                    str(resultado[2])
                status = resultado[4]

                self.table_batidas_ponto.insert("", "end", values=(id_batida, dia_formatado, hora_formatada, status))

            cursor.close()
            close_connection(conn)

        except Exception as e:
            print(f"Erro ao consultar as batidas de ponto: {e}")

    def open_tela_acerto_ponto(self):
        self.tela_acerto_ponto = customtkinter.CTkToplevel(root)
        self.tela_acerto_ponto.title("Acerto de Ponto")
        self.tela_acerto_ponto.geometry("500x700")
        self.tela_acerto_ponto.config(bg='#FFFFFF')

        font_title = customtkinter.CTkFont(family='', size=25, weight='bold')
        font_subtitle = customtkinter.CTkFont(family='', size=18, weight='bold')
        font_button = customtkinter.CTkFont(family='', size=14, weight='bold')

        self.title_acerto = customtkinter.CTkLabel(master=self.tela_acerto_ponto, text='Novo acerto',
                                                   text_color='#3F5B80', bg_color='#FFFFFF', font=font_title)
        self.title_acerto.pack(pady=(40, 0))

        self.subtitle_data = customtkinter.CTkLabel(master=self.tela_acerto_ponto, text='Selecione a data do acerto:',
                                                    text_color='#545454', bg_color='#FFFFFF', font=font_subtitle)
        self.subtitle_data.pack(pady=(30, 0))

        self.calendar = Calendar(master=self.tela_acerto_ponto, selectmode="day", date_pattern="yyyy-mm-dd")
        self.calendar.pack(pady=20)

        self.frame_hora_entrada = customtkinter.CTkFrame(master=self.tela_acerto_ponto, width=800, height=200,
                                                         fg_color="#FFFFFF")
        self.frame_hora_entrada.pack(pady=(0, 20))

        self.subtitle_entrada = customtkinter.CTkLabel(master=self.frame_hora_entrada, text="Entrada:",
                                                       text_color='#545454', bg_color='#FFFFFF', font=font_subtitle)
        self.subtitle_entrada.pack(side='left')

        self.entrada = customtkinter.CTkComboBox(master=self.frame_hora_entrada, bg_color="#FFFFFF",
                                                 values=self.get_hour_list(), width=100, state="readonly")
        self.entrada.pack(side='left', padx=(21, 0))

        self.frame_hora_saida = customtkinter.CTkFrame(master=self.tela_acerto_ponto, width=800, height=200,
                                                       fg_color="#FFFFFF")
        self.frame_hora_saida.pack(pady=(0, 20))

        self.subtitle_saida = customtkinter.CTkLabel(master=self.frame_hora_saida, text="Saída:",
                                                     text_color='#545454', bg_color='#FFFFFF', font=font_subtitle)
        self.subtitle_saida.pack(side='left')

        self.saida = customtkinter.CTkComboBox(master=self.frame_hora_saida, bg_color="#FFFFFF",
                                               values=self.get_hour_list(), width=100, state="readonly")
        self.saida.pack(side='left', padx=(41, 0))

        self.subtitle_motivo = customtkinter.CTkLabel(master=self.tela_acerto_ponto, text="Motivo:",
                                                      text_color='#545454', bg_color='#FFFFFF', font=font_subtitle)
        self.subtitle_motivo.pack(padx=(0, 131))

        self.motivo = customtkinter.CTkTextbox(master=self.tela_acerto_ponto, width=250, height=100, corner_radius=6,
                                               border_width=2, fg_color="#F6F6F6", border_color="#D3D3D3")
        self.motivo.pack(pady=(10, 20))

        self.fazendo_acerto_button = customtkinter.CTkButton(master=self.tela_acerto_ponto, width=100, height=40,
                                                             text='Fazer ponto', corner_radius=6, font=font_button,
                                                             fg_color='#FAA115', hover_color='#FBA827',
                                                             command=self.novo_acerto)
        self.fazendo_acerto_button.pack(side='bottom', pady=(0, 40))

    def get_hour_list(self):
        hours = []
        for hour in range(24):
            hours.append(f"{hour:02}:00")
        return hours

    def novo_acerto(self):
        data_acerto = self.calendar.get_date()
        entrada = self.entrada.get()
        saida = self.saida.get()
        motivo = self.motivo.get("0.0", "end")

        print("Data selecionada:", data_acerto)
        print("Hora entrada:", entrada)
        print("Hora saida:", saida)
        print("Motivo:", motivo)

        id_user = self.id_user

        # Verificar se os campos não estão vazios
        if not data_acerto or not entrada or not saida:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        status = "pendente"

        try:
            conn = connect()
            cursor = conn.cursor()

            query = \
                f"INSERT INTO acertos_ponto (id_user, data_acerto, entrada, saida, motivo, status_) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (id_user, data_acerto, entrada, saida, motivo, status)
            cursor.execute(query, valores)
            conn.commit()

            cursor.close()
            close_connection(conn)

            messagebox.showinfo("Acerto de ponto", "Acerto realizado com sucesso. Aguarde a aprovação do gestor.")

            self.atualizar_tabela_acertos_ponto()
            self.tela_acerto_ponto.destroy()

        except Exception as e:
            print(f"Erro ao realizar o acerto de ponto: {e}")
            messagebox.showerror("Erro", "Ocorreu um erro ao registrar o acerto de ponto. Por favor, tente novamente.")

    def atualizar_tabela_acertos_ponto(self):
        # Limpar os dados existentes na tabela
        self.table_acertos_ponto.delete(*self.table_acertos_ponto.get_children())

        try:
            conn = connect()
            cursor = conn.cursor()

            # Consultar os acertos de ponto do usuário
            query_consulta_acertos = \
                "SELECT id_acerto, data_acerto, entrada, saida, motivo, status_, id_user FROM acertos_ponto WHERE id_user = %s ORDER BY id_acerto DESC"
            cursor.execute(query_consulta_acertos, (self.id_user,))
            resultados = cursor.fetchall()

            for resultado in resultados:
                id_acerto = resultado[0]
                data_acerto = resultado[1].strftime("%d/%m/%Y")
                entrada = resultado[2]
                saida = resultado[3]
                motivo = resultado[4]
                status = resultado[5]
                id_user = resultado[6]

                self.table_acertos_ponto.insert("", "end", values=(id_acerto, data_acerto, entrada, saida, motivo, status, id_user))

            cursor.close()
            close_connection(conn)

        except Exception as e:
            print(f"Erro ao consultar os acertos de ponto: {e}")

    # add methods to app
    def open_login(self):
        self.show_page(0)

    def open_cadastro(self):
        self.show_page(1)

    def open_batida_ponto(self):
        self.show_page(2)

    def open_acerto_ponto(self):
        self.show_page(3)

    def open_folha_ponto(self):
        self.show_page(4)

    def show_page(self, index):
        if self.current_page is not None:
            self.current_page.pack_forget()  # Esconde a página atual

        self.current_page = self.pages[index]
        self.current_page.pack()  # Mostra a nova página


# Criar a janela principal
root = customtkinter.CTk()
root.geometry("950x730")
root.title("Clockin")
root.config(bg='#D2DDF9')

app = App(root)
root.mainloop()
