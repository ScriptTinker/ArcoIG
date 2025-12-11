"""MOCKING DEPRECATED FUNCTION"""
import sys
from unittest.mock import MagicMock

try:
    import huggingface_hub.utils
    if not hasattr(huggingface_hub.utils, 'reset_sessions'):
        huggingface_hub.utils.reset_sessions = MagicMock()
        print("✓ Mocked reset_sessions")
except Exception as e:
    print(f"Warning during mock setup: {e}")

"""END MOCKING"""

import subprocess
import sys

def install_requirements():
    try:
        with open('requirements.txt', "r", encoding="utf-16") as f:
            packages = f.read().splitlines()
        
        all_installed = True
        for package in packages:
            package = package.strip()
            if not package or package.startswith('#'):
                continue
                
            package_name = package.split('==')[0].split('>=')[0].split('<=')[0]
            try:
                __import__(package_name.replace('-', '_'))
                print(f"✓ {package} già installato")
            except ImportError:
                print(f"Sto scaricando: {package}...")
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                except Exception as e:
                    print(F"ERRORE DURANTE L'INSTALLAZIONE DI {package}")

                all_installed = False
        
        return all_installed
    except Exception as e:
        print(f"Errore: {e}")
        return False

if __name__ == "__main__":
    print("Verifico l'installazione dell'app")
    result = install_requirements()
    if result:
        print("Verifica completata! Tutti i pacchetti sono installati.")
        import main
    else:
        print("Installazione completata! Avvio l'app...")
        import main