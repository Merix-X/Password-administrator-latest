# setup.py
import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "includes": ["Graphic_Module.py", "search_string.py", "Zobraz_Module.py"],  # Názvy modulů, které chcete zahrnout
    "packages": [],               # Seznam balíčků, které chcete zahrnout
    "excludes": ["Hesla.txt", "temp.py", "tmp.py", "release.json", "Aktualizovat.py", "search.py"],     # Seznam modulů, které chcete vyloučit
    "include_files": [],          # Seznam souborů, které chcete zahrnout
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Pokud chcete aplikaci bez konzole, použijte "Win32GUI"

setup(
    name="MyApp",
    version="1.0",
    description="My Python Application",
    options={"build_exe": build_exe_options},
    executables=[Executable("Main.py", base=base)],
)
