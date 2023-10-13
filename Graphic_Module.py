from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from search_string import write, replaceAll, findLineCryptography
import Zobraz_Module as zm
import time as tm
import Login_Module as log
import Encryption_Module as enc


class Graphic:
    def graphic(self):
        window = tk.Tk(className=" Správce hesel")
        window.geometry("550x310+500+250")
        window.configure(bg="gray")

        def open_url():
            tk.messagebox.showwarning("Varování!", "Aktualizování aplikace není z důvodu vývoje kódu k dispozici!\nMožnost aktualizování bude zprovozněna v některé z dalších verzí.")
            #url = 'https://github.com/Merix-X/Password-administrator/tree/95885ab48bd609cb3debc409bfd79e5f5fd66e2e/Password_Administrator-v1.6.zip'
            #webbrowser.open(url)

        def kontakt():
            window_kontakt = tk.Tk(className=" Kontakt")
            label_kontakt = tk.Label(window_kontakt, text="Pokud by něco nefungovalo\nobraďte se na mě a pomůžu vám s čímkoliv!\n:-D\n----------------------------------------\nTel.:   +420 736 296 736\nMail:   Merix.Programing0539@gmail.com\n")
            label_kontakt.pack()
            button_quit_kontakt = tk.Button(window_kontakt, text="Zpět na Správce hesel", command=window_kontakt.destroy)
            button_quit_kontakt.pack()

        class Menues:
            def menues(self):
                menubar = tk.Menu(window)
                FileMenu = tk.Menu(menubar, tearoff=0)
                HelpMenu = tk.Menu(menubar, tearoff=0)

                menubar.add_cascade(label="Soubor", menu=FileMenu)

                menubar.add_cascade(label="Nápověda", menu=HelpMenu)

                FileMenu.add_command(label="Kód pro main.py", command=zm.main)
                FileMenu.add_command(label="Kód pro Graphic_Module.py", command=zm.graphic_module)
                FileMenu.add_command(label="Kód pro Search_String.py", command=zm.string_modifications)
                FileMenu.add_command(label="Kód pro View_Module.py", command=zm.zobraz_module)
                FileMenu.add_separator()
                FileMenu.add_command(label="Zobrazit seznam hesel", command=zm.zobraz_hesla)

                HelpMenu.add_command(label="O aplikaci", command=zm.readme)
                HelpMenu.add_command(label="Jak správně přidat heslo?", command=zm.jak_pridat_heslo)
                HelpMenu.add_separator()
                HelpMenu.add_command(label="Aktualizovat", command=open_url)
                HelpMenu.add_command(label="Kontakt", command=kontakt)

                window.config(menu=menubar)

        class Selections:
            def select_1(self):
                def delete_1_1():
                    label_nic_1.destroy()
                    label.destroy()
                    nov.destroy()
                    button.destroy()
                    delete_1_2()
                    window.geometry("550x330+500+250")

                label_nic_1 = tk.Label(window, text="###################################", bg="gray", fg="gray")
                label_nic_1.grid(row=3, column=2)
                label = tk.Label(window, text="Zadejte nové heslo podle návodu v nápovědě: ", bg="gray", fg="yellow")
                label.grid(row=3, column=1)
                window.geometry("650x310")
                button_quit1.place(x=565, y=240)        #X=šířka, Y=výška
                nov = tk.Entry(window, bg="orange", width=35)
                nov.grid(row=3, column=2)

                label_nic_3 = tk.Label(window, text="############################\n\n", bg="gray", fg="gray")
                label_nic_4 = tk.Label(window, text="############################\n\n", bg="gray", fg="gray")

                def delete_1_2():
                    label_nic_3.destroy()
                    label_nic_4.destroy()
                    window.geometry("550x330+500+250")

                def write_heslo():
                    novy = nov.get()
                    novy1 = enc.encrypt_password(novy)
                    print(novy1)
                    write("Hesla.txt", novy1)
                    tm.sleep(1)
                    tk.messagebox.showinfo("Úspěch!", "Heslo bylo přidáno do seznamu hesel!")
                    label_nic_3.grid(row=4, column=2)
                    label_nic_4.grid(row=6, column=2)

                def callback1():
                    button_zpet.destroy()
                    delete_1_1()
                    start()

                button = tk.Button(window, text="\n      OK      \n", command=write_heslo)
                button.grid(row=3, column=3)

                button_zpet = tk.Button(window, text="\n     Zpět     \n", command=callback1)
                button_zpet.place(x=465, y=240)




            def select_2(self):
                window.geometry("550x310+500+250")
                button_quit1.place(x=465, y=240)

                label_1 = tk.Label(window, text="Zadejte název hesla které hledáte: ", bg="gray", fg="yellow")
                label_1.place(x=60, y=57)       #X=šířka, Y=výška
                search_entry = tk.Entry(window, bg="orange", width=30)
                search_entry.place(x=261, y=57)     #X=šířka, Y=výška

                def search_heslo():
                    try:
                        string = findLineCryptography("Hesla.txt", search_entry.get())
                        entry_to_insert_passwd = tk.Entry(window, bg="orange", width=len(string))
                        entry_to_insert_passwd.place(x=115, y=130)      #X=šířka, Y=výška
                        entry_to_insert_passwd.delete(0, tk.END)
                        entry_to_insert_passwd.insert(tk.END, string)

                    except FileNotFoundError:
                        messagebox.showwarning("Upozornění!", "Dokud nejsou přidaná žádná hesla, nemůžete používat vyhledávač a upravování hesel! Nejdříve musíte přidat alespoň jedno heslo!")

                    except TypeError:
                        messagebox.showerror("Chyba", "Toto heslo bohužel neexistuje. Ujistěte se že jste neudělali chybu a zkuste to znovu")

                    def delete_2_1():
                        label_1.destroy()
                        search_entry.destroy()
                        button_ok1.destroy()
                        window.geometry("550x330+500+250")

                    def callback2():
                        try:
                            entry_to_insert_passwd.destroy()
                            button_zpet1.destroy()
                            delete_2_1()
                            start()
                        except NameError:
                            print("nejde odstranit")
                            button_zpet1.destroy()
                            delete_2_1()
                            start()


                    button_zpet1 = tk.Button(window, text="\n     Zpět     \n", command=callback2)
                    button_zpet1.place(x=365, y=240)

                button_ok1 = tk.Button(window, text="\n      OK      \n", command=search_heslo)
                button_ok1.place(x=465, y=37)


            def select_3(self):
                window.geometry("550x310+500+250")
                button_quit1.place(x=465, y=240)

                label_nic_5 = tk.Label(window, text="############################", bg="gray", fg="gray")
                label_nic_5.grid(row=3, column=2)
                label_nic_6 = tk.Label(window, text="##", bg="gray", fg="gray")
                label_nic_6.grid(row=4, column=0)
                label_nic_7 = tk.Label(window, text="##", bg="gray", fg="gray")
                label_nic_7.grid(row=5, column=2)
                label_8 = tk.Label(window, text="Zadejte název hesla které chcete upravit: ", bg="gray", fg="yellow")
                label_8.grid(row=3, column=1)
                label_9 = tk.Label(window, text="Zadejte nové heslo podle návodu v nápovědě: ", fg="yellow", bg="gray")
                label_9.grid(row=4, column=1)
                search_entry5 = tk.Entry(window, bg="orange", width=25)
                search_entry5.grid(row=3, column=2)
                replace_entry1 = tk.Entry(window, bg="orange", width=35)
                replace_entry1.grid(row=4, column=2)

                def replace_heslo():
                    try:
                        novy1 = search_entry5.get()
                        novy2 = replace_entry1.get()
                        print("novy1:", novy1, "novy2:", novy2)
                        rep = replaceAll("Hesla.txt", novy1, novy2)
                        if rep == "nepřepsáno":
                            tm.sleep(1)
                            tk.messagebox.showerror("Neúspěch!", "Heslo se nepodařilo upravit!\nZřejně v seznamu hesel není!")

                        elif novy1 == '' and novy2 == '':
                            print("1")
                            tm.sleep(1)
                            tk.messagebox.showerror("Error", "Políčka pro zadání názvu a nového hesla jsou prázdná. Takže nemůžete přepisovat!")

                        else:
                            tm.sleep(1)
                            tk.messagebox.showinfo("Úspěch!", "Heslo bylo úspěšně upraveno!")

                    except FileNotFoundError:
                        tk.messagebox.showwarning("Upozornění!",
                                                   "Dokud nejsou přidaná žádná hesla, nemůžete používat vyhledávač a upravování hesel! Nejdříve musíte přidat alespoň jedno heslo!")
                        label_nic_2 = tk.Label(window, text="#############", bg="gray", fg="gray")
                        label_nic_2.grid(row=5, column=1)

                    def delete_3_1():
                        label_nic_5.destroy()
                        label_nic_6.destroy()
                        label_nic_7.destroy()
                        label_8.destroy()
                        label_9.destroy()
                        search_entry5.destroy()
                        if rep == "přepsáno":
                            replace_entry1.destroy()
                        elif rep == "nepřepsáno":
                            print("label_informaci6.destroy()")
                        button_ok3.destroy()
                        window.geometry("550x330+500+250")

                    def callback3():
                        button_zpet3.destroy()
                        delete_3_1()
                        start()

                    button_zpet3 = tk.Button(window, text="\n     Zpět     \n", command=callback3)
                    button_zpet3.place(x=365, y=240)

                button_ok3 = tk.Button(window, text="\n      OK      \n", command=replace_heslo)
                button_ok3.grid(row=6, column=2)

            def delete_heslo(self):
                window.geometry("550x310+500+250")
                button_quit1.place(x=455, y=230)

                label_nic_5 = tk.Label(window, text="############################", bg="gray", fg="gray")
                label_nic_5.grid(row=3, column=2)
                label_nic_6 = tk.Label(window, text="##", bg="gray", fg="gray")
                label_nic_6.grid(row=4, column=0)
                label_nic_7 = tk.Label(window, text="##", bg="gray", fg="gray")
                label_nic_7.grid(row=5, column=2)
                label_8 = tk.Label(window, text="Zadejte název hesla které chcete odstranit: ", bg="gray",
                                   fg="yellow")
                label_8.grid(row=3, column=1)
                search_entry5 = tk.Entry(window, bg="orange", width=25)
                search_entry5.grid(row=3, column=2)

                def replace_heslo():
                    try:
                        novy1 = search_entry5.get()
                        rep = replaceAll("Hesla.txt", novy1, "")
                        if rep == "přepsáno":
                            tm.sleep(1)
                            tk.messagebox.showinfo("Úspěch!", "Heslo bylo úspěšně odstraněno ze seznamu hesel!")
                        elif rep == "nepřepsáno":
                            tm.sleep(1)
                            tk.messagebox.showerror("Neúspěch!", "Heslo nebylo možné odstranit ze seznamu hesel!\nZřejně v seznamu hesel není!")

                    except FileNotFoundError:
                        messagebox.showwarning("Upozornění!",
                                               "Dokud nejsou přidaná žádná hesla, nemůžete je odstraňovat! Nejdříve musíte přidat alespoň jedno heslo!")
                        label_nic_2 = tk.Label(window, text="#############", bg="gray", fg="gray")
                        label_nic_2.grid(row=5, column=1)

                    def delete_3_1():
                        label_nic_5.destroy()
                        label_nic_6.destroy()
                        label_nic_7.destroy()
                        label_8.destroy()
                        search_entry5.destroy()
                        if rep == "přepsáno":
                            print("!")
                        elif rep == "nepřepsáno":
                            print(".!")
                        button_ok3.destroy()
                        window.geometry("550x330+500+250")

                    def callback3():
                        button_zpet3.destroy()
                        delete_3_1()
                        start()

                    button_zpet3 = tk.Button(window, text="\n     Zpět     \n", command=callback3)
                    button_zpet3.place(x=365, y=231)

                button_ok3 = tk.Button(window, text="\n      OK      \n", command=replace_heslo)
                button_ok3.grid(row=5, column=2)

        def start():
            window.geometry("550x330+500+250")
            button_quit1.place(x=465, y=240)

            Menues.menues("menues")
            moznosti = ["Chci přidat heslo", "Chci najít heslo - dočasně mimo provoz", "Chci upravit heslo", "Chci odstranit heslo"]
            combo = ttk.Combobox(window, values=moznosti)
            combo.grid(row=2, column=1)

            def option_selected():
                selected_option = combo.get()
                if selected_option == "Chci přidat heslo":
                    label_moznost.destroy()
                    combo.destroy()
                    button_ok.destroy()
                    Selections.select_1("je 1.")

                elif selected_option == "Chci najít heslo - dočasně mimo provoz":
                    label_moznost.destroy()
                    combo.destroy()
                    button_ok.destroy()
                    Selections.select_2("je 2.")

                elif selected_option == "Chci upravit heslo":
                    label_moznost.destroy()
                    combo.destroy()
                    button_ok.destroy()
                    Selections.select_3("je 3.")

                elif selected_option == "Chci odstranit heslo":
                    label_moznost.destroy()
                    combo.destroy()
                    button_ok.destroy()
                    Selections.delete_heslo("je 4.")

            button_ok = tk.Button(window, text="Potvrdit", command=option_selected)
            button_ok.grid(row=2, column=4)

            label_moznost = tk.Label(window, text="Vyberte možnost:                  ", fg="yellow", bg="gray")
            label_moznost.grid(row=1, column=1)

            label_nic1 = tk.Label(window, text="                    ", fg="yellow", bg="gray")
            label_nic1.grid(row=2, column=0)

            label_nic2 = tk.Label(window, text="                    ", fg="gray", bg="gray")
            label_nic2.grid(row=2, column=3)

            label_nic3 = tk.Label(window, text="                    \n", bg="gray")
            label_nic3.grid(row=0, column=1)

            combo.bind("<<SelectedOption>>", option_selected)

            window.mainloop()

        button_quit1 = tk.Button(window, text="\n   Ukončit   \n", command=window.destroy)
        button_quit1.place(x=465, y=240)
        start()

Graphic.graphic("grafika")