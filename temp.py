from github import Github

def stahnout_soubor(uzivatel, jmeno_repozitare, cesta_souboru):
    g = Github()
    repo = g.get_repo(f"{uzivatel}/{jmeno_repozitare}")
    nejnovsi_verze = repo.get_latest_release()
    soubor = repo.get_contents(cesta_souboru, ref=nejnovsi_verze.tag_name)

    with open(soubor.path, "wb") as f:
        f.write(soubor.decoded_content)


# Použití:
uzivatel = "Merix-X"
jmeno_repozitare = "Password-administrator"
cesta_souboru = "main/release.json"

stahnout_soubor(uzivatel, jmeno_repozitare, cesta_souboru)