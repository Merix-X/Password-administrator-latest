from cryptography.fernet import Fernet

# Generování klíče a uložení ho do souboru
key = Fernet.generate_key()
with open("key.key", "wb") as key_file:
    key_file.write(key)

# Funkce pro načtení klíče
def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
        return key

key1 = load_key()

# Funkce pro zašifrování hesla
def encrypt_passwd(key, password):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

# Funkce pro dešifrování hesla
def decrypt_passwd(key, encrypted_password):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password

# Funkce pro vyhledání a dešifrování hesla v souboru
def findLineCryptography(file, search_encrypted):
    key = load_key()
    with open(file, 'rb') as f:  # Otevřít soubor v binárním režimu
        for i, line in enumerate(f, 1):
            if search_encrypted in line:
                decrypted_line = decrypt_passwd(key, line)
                return decrypted_line
    return "Soubor neobsahuje zadaný zašifrovaný řetězec"

# Příklad použití:
password = "TotoJeHeslo123"
encrypted_password = encrypt_passwd(key1, password)
with open("tmp.txt", "ab") as fd:  # Uložit zašifrované heslo do souboru v binárním režimu
    fd.write(encrypted_password + b'\n')
print("Zašifrované heslo:", encrypted_password)

# Pro vyhledání a dešifrování hesla v souboru:
search_encrypted = encrypt_passwd(key1, "TotoJeHeslo123")
print(search_encrypted)
decrypted_password = findLineCryptography("tmp.txt", search_encrypted)
print("Dešifrované heslo:", decrypted_password)