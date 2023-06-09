import tkinter
import tkinter.font

import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self, root):
        super().__init__()
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

        # Declarations
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
                                                 fg_color='#D2DDF9', bg_color='#D2DDF9')  # display image with a CTkLabel
        self.image_logo.pack(pady=(55, 0), ipadx=0, fill='both')

        self.image_text_logo = customtkinter.CTkLabel(self.bg_tela_login, image=text_logo, text="",
                                                      fg_color='#D2DDF9', bg_color='#D2DDF9')  # display image with a CTkLabel
        self.image_text_logo.pack(pady=20, fill='both')

        self.frame_login = customtkinter.CTkFrame(self.bg_tela_login, width=400, height=255, corner_radius=15,
                                                  fg_color='#F2F2F2', bg_color='#D2DDF9')
        self.frame_login.pack(pady=(20, 0))

        self.title = customtkinter.CTkLabel(master=self.frame_login, text='Logar:', text_color='#7D7987',
                                            font=font_title)
        self.title.place(x=35, y=30)

        self.login = customtkinter.CTkEntry(master=self.frame_login, width=330, height=40, placeholder_text="Seu login")
        self.login.place(x=35, y=70)

        self.password = customtkinter.CTkEntry(master=self.frame_login, width=330, height=40,
                                               placeholder_text="Sua senha", show="*")
        self.password.place(x=35, y=130)

        self.login_button = customtkinter.CTkButton(master=self.frame_login, width=100, height=40, text='LOGIN',
                                                    corner_radius=6, font=font_button, fg_color='#FAA115',
                                                    hover_color='#FBA827', command=self.open_batida_ponto)
        self.login_button.place(x=150, y=190)

        self.cadastro_link = customtkinter.CTkButton(master=self.bg_tela_login, text='CADASTRE-SE', text_color='#3F5B80',
                                                     fg_color='transparent', bg_color='#D2DDF9', hover=False,
                                                     font=font_link, command=self.open_cadastro)
        self.cadastro_link.pack(pady=(30, 0))

        self.creator = customtkinter.CTkLabel(self.bg_tela_login, text='Criado por Caio Carvalho', text_color='#7D7987',
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

        self.login = customtkinter.CTkEntry(master=self.frame_cadastro, width=330, height=40,
                                            placeholder_text="Seu login")
        self.login.place(x=35, y=70)

        self.password = customtkinter.CTkEntry(master=self.frame_cadastro, width=330, height=40,
                                               placeholder_text="Sua senha", show="*")
        self.password.place(x=35, y=130)

        self.cadastro_button = customtkinter.CTkButton(master=self.frame_cadastro, width=100, height=40,
                                                       text='CADASTRAR', corner_radius=6, font=font_button,
                                                       fg_color='#FAA115', hover_color='#FBA827')
        self.cadastro_button.place(x=150, y=190)

        self.login_link = customtkinter.CTkButton(self.bg_tela_cadastro, text='LOGAR', text_color='#3F5B80',
                                                  fg_color='transparent', bg_color='#D2DDF9', hover=False,
                                                  font=font_link, command=self.open_login)
        self.login_link.pack(pady=(30, 0))

        self.creator = customtkinter.CTkLabel(self.bg_tela_cadastro, text='Criado por Caio Carvalho',
                                              text_color='#7D7987', bg_color='#D2DDF9', font=font_creator)
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

        self.content = customtkinter.CTkFrame(self.bg_tela_batida_ponto, width=0, height=800, fg_color='#F9F9F9')
        self.content.pack(fill='both', expand=True)

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

        self.content = customtkinter.CTkFrame(self.bg_tela_acerto_ponto, width=0, height=800, fg_color='#F9F9F9')
        self.content.pack(fill='both', expand=True)

        self.icon_clock_add_acerto = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_add_white, text="")
        self.icon_clock_add_acerto.place(x=19, y=30)

        self.icon_clock_add_acerto.bind("<Enter>", lambda event: self.icon_clock_add_acerto.
                                        configure(image=icon_clock_add_blue))

        self.icon_clock_add_acerto.bind("<Leave>", lambda event: self.icon_clock_add_acerto.
                                        configure(image=icon_clock_add_white))

        self.icon_clock_add_acerto.bind("<Button-1>", lambda event: self.open_batida_ponto())

        self.icon_clock_checked_acerto = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_checked_blue, text="")
        self.icon_clock_checked_acerto.place(x=19, y=122)

        self.icon_clock_schedule_acerto = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_schedule_white, text="")
        self.icon_clock_schedule_acerto.place(x=19, y=214)

        self.icon_clock_schedule_acerto.bind("<Enter>", lambda event: self.icon_clock_schedule_acerto.
                                             configure(image=icon_clock_schedule_blue))
        self.icon_clock_schedule_acerto.bind("<Leave>", lambda event: self.icon_clock_schedule_acerto.
                                             configure(image=icon_clock_schedule_white))
        self.icon_clock_schedule_acerto.bind("<Button-1>", lambda event: self.open_folha_ponto())

        self.icon_clock_logout_acerto = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_logout_white, text="")
        self.icon_clock_logout_acerto.place(x=19, y=306)

        self.icon_clock_logout_acerto.bind("<Enter>", lambda event: self.icon_clock_logout_acerto.
                                           configure(image=icon_clock_logout_blue))
        self.icon_clock_logout_acerto.bind("<Leave>", lambda event: self.icon_clock_logout_acerto.
                                           configure(image=icon_clock_logout_white))
        self.icon_clock_logout_acerto.bind("<Button-1>", lambda event: self.open_login())

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

        self.icon_clock_checked_folha = customtkinter.CTkLabel(master=self.sidebar, image=icon_clock_checked_white, text="")
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
