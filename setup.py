import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])#install package

def main():
    try:
        with open('requirements.txt', 'r') as f:
            for line in f.readlines():
                package = line.strip()
                install(package)
        print("All dependencies are installed successfully!")
    except Exception as e:
        print(f"Error installing packages: {e}")
        
if __name__ == "__main__":
    main()
