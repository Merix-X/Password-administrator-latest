def search(file, coding, string):
    with open(file, encoding=coding, mode='r') as soubor:
        obsah = soubor.readlines()
        for line in obsah:
            C = obsah.index(line)
            if line.find(string) != -1:
                C =+ 1  # Číslo řádku je C
                return C, line

def SearchAll(file, coding, string):
    with open(file, encoding=coding, mode='r') as soubor:
        obsah = soubor.readlines()
        vyskyty = []
        for line in obsah:
            C = obsah.index(line)
            if line.find(string) != -1:
                vyskyty.extend([C, line])
                continue
        return vyskyty

def SearchIndex(file, coding, string):
    with open(file, encoding=coding, mode='r') as soubor:
        obsah = soubor.readlines()
        for line in obsah:
            C = obsah.index(line)
            if line.find(string) != -1:
                C =+ 1
                return C

def SearchString(file, coding, string):
    with open(file, encoding=coding, mode='r') as soubor:
        obsah = soubor.readlines()
        for line in obsah:
            C = obsah.index(line)
            if line.find(string) != -1:
                C =+ 1
                return line
