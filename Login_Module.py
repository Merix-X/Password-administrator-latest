import tkinter as tk

class Login:
    def log(self):
        window = tk.Tk(className=" Správce hesel")
        window.geometry("550x310+500+250")
        window.configure(bg="gray")

        def name():
            entry_name = tk.Entry(font=("arial", 17), bg="orange", width=25)
            entry_name.place(x=112, y=100)
            background_text = "Uživatelské jméno"
            entry_name.insert(0, background_text)

            def on_entry_click(event):
                if entry_name.get() == background_text:
                    entry_name.delete(0, tk.END)  # Odebrání textu na pozadí

            entry_name.bind("<FocusIn>", on_entry_click)
            A = entry_name.get()
            return A

        def passwd():
            entry = tk.Entry(font=("arial", 17), bg="orange", width=25)
            entry.place(x=112, y=150)
            background_text = "Heslo"
            entry.insert(0, background_text)

            def on_entry_click(event):
                if entry.get() == background_text:
                    entry.delete(0, tk.END)  # Odebrání textu na pozadí

            entry.bind("<FocusIn>", on_entry_click)
            B = entry.get()
            return B

        C = name()
        D = passwd()
        window.mainloop()
        return C, D