import subprocess
import sys

def install_requirements():
    """requirements.txt dosyasındaki bağımlılıkları yükler."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Bağımlılıklar başarıyla yüklendi!")
    except subprocess.CalledProcessError as e:
        print(f"Bağımlılıkları yüklerken bir hata oluştu: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()
