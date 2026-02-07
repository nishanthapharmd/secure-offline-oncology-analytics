import sys
import platform

def system_check():
    print("System check OK")
    print("Python version:", sys.version)
    print("Platform:", platform.system())

if __name__ == "__main__":
    system_check()
