import subprocess
import sys

def install_requirements():
    with open('requirements.txt', "r", encoding="utf-16") as f:
        packages = f.read().splitlines()
    
    for package in packages:
        try:
            __import__(package.split('==')[0].split('>=')[0].split('<=')[0])
            print(f"✓ {package} già installato")
            return True
        except ImportError:
            print(f"Sto scaricando: {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            return False

if __name__ == "__main__":
    print("Verifico l'istallazione del app")
    install_requirements()
    if install_requirements:
        print("Verifica completata!")
        import main
    else:
        print("Errore durante la verifica!")    
    
