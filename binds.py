import subprocess
import keyboard

exe_path = r"C:\Users\agesoi\AppData\Roaming\Telegram Desktop\Telegram.exe"  #путь к файлу
  
while True:
    keyboard.wait("9")
    subprocess.Popen(exe_path)
