import subprocess
import os
import time
import webbrowser
import sys
import shutil

# === LOCALIZA O manage.py ===
def localizar_manage_py():
    usuario = os.path.expanduser("~")

    caminhos = [
        os.path.join(usuario, "Documentos", "web automacao", "monitor_linha", "manage.py"),
        os.path.join(usuario, "Documents", "web automacao", "monitor_linha", "manage.py"),
    ]

    # Busca OneDrive
    for pasta in os.listdir(usuario):
        if "OneDrive" in pasta:
            caminhos.append(
                os.path.join(usuario, pasta, "Documentos", "web automacao", "monitor_linha", "manage.py")
            )

    for c in caminhos:
        if os.path.exists(c):
            return c
    return None


# === LOCALIZA O PYTHON REAL DO SISTEMA ===
def localizar_python_real():
    # 1. Tenta o python do PATH
    py = shutil.which("python")
    if py:
        return py

    # 2. Tenta python3
    py = shutil.which("python3")
    if py:
        return py

    # 3. Busca no AppData (instalações comuns do Windows)
    possiveis = [
        r"C:\Python312\python.exe",
        r"C:\Python311\python.exe",
        r"C:\Python310\python.exe",
        os.path.join(os.path.expanduser("~"), "AppData", "Local", "Programs", "Python", "Python312", "python.exe"),
        os.path.join(os.path.expanduser("~"), "AppData", "Local", "Programs", "Python", "Python311", "python.exe"),
    ]

    for p in possiveis:
        if os.path.exists(p):
            return p

    return None


manage = localizar_manage_py()
python_real = localizar_python_real()

if not manage:
    print("❌ manage.py não encontrado.")
    time.sleep(5)
    sys.exit()

if not python_real:
    print("❌ Python real não encontrado no sistema!")
    print("Instale o Python em: https://www.python.org/downloads/")
    time.sleep(8)
    sys.exit()

print(f"✔ manage.py encontrado: {manage}")
print(f"✔ Python real encontrado: {python_real}")
print("🚀 Iniciando Django...")

# === INICIA O SERVIDOR COM O PYTHON REAL ===
processo = subprocess.Popen(
    [python_real, manage, "runserver", "127.0.0.1:8000"],
)

time.sleep(3)

print("🌍 Abrindo navegador...")
webbrowser.open("http://127.0.0.1:8000/")

print("\n===========================================")
print("  Servidor Django está em execução.")
print("  NÃO feche esta janela!                  ")
print("===========================================\n")

# Mantém aberto
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Encerrando...")
    processo.terminate()
    sys.exit()
