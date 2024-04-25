import sys 

try:
    import colorama
except ImportError:
    print("Failed to import colorama !")
    sys.exit(99)

def isWin32Platform():
    if sys.platform.startswith("win32"):
        return True

def SUCCESS(string: str) -> str:
    if isWin32Platform() == True:
        colorama.just_fix_windows_console()
        
    strOut = colorama.Fore.GREEN + "[+] " + colorama.Style.RESET_ALL + string 
    print(strOut)