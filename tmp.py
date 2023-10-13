import Encryption_Module as enc
from cryptography.fernet import Fernet
import cryptography


def findLineString(file, search_content):
    with open(file, 'rb') as f:  # Otevření souboru v binárním režimu
        for i, line in enumerate(f, 1):
            line = line.strip()  # Odstranění bílých znaků a konců řádků
            try:
                decrypted_line = enc.decrypt_password(line).decode()  # Dešifrování a převod na řetězec
            except cryptography.fernet.InvalidToken:
                continue  # Pokud řádek není šifrovaný, přeskočit
            if search_encrypted in decrypted_line:
                return decrypted_line
    return None


# Příklad použití:
search_content = input("zadej řetězec: ")
found_line = findLineString("Hesla.txt", search_content)

if found_line:
    print("Nalezený řádek:", found_line)
else:
    print("Hledaný obsah nebyl nalezen v žádném řádku.")
