import requests
import tkinter as tk
import webbrowser
import subprocess
from github import Github

def ziskat_aktualni_verzi():
    url = "https://api.github.com/repos/Merix-X/Password-administrator/releases/latest"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["tag_name"]
    else:
        return None


def aktualizovat_program():
    aktualni_verze = "1.0"  # Nahraďte aktuální verzi vašeho programu

    nova_verze = ziskat_aktualni_verzi()
    if nova_verze is not None and nova_verze != aktualni_verze:
        print("Probíhá aktualizace programu...")
        # Zde můžete provést kód pro aktualizaci programu, např. stáhnout novou verzi ze stránky a spustit instalátor

        # Příklad: Stáhnout soubor z URL
        url = "https://github.com/Merix-X/Password-administrator/raw/main/Password%20Administrator%20-%20v1.2.exe".format(nova_verze)
        # Nahraďte "uzivatel/jmeno_repozitare" a doplňte název souboru instalátoru nebo jiného aktualizačního souboru

        # Příklad: Stáhnout soubor pomocí modulu requests
        import requests

        response = requests.get(url)
        if response.status_code == 200:
            with open("Správce hesel - 1.2.exe", "wb") as f:
                f.write(response.content)
            print("Aktualizace byla stažena.")

        # Příklad: Spustit instalátor
        subprocess.call(["python", "Správce hesel - 1.2.exe"])

window = tk.Tk()

button_aktualizovat = tk.Button(window, text="Aktualizovat", command=aktualizovat_program)
button_aktualizovat.pack()

window.mainloop()
