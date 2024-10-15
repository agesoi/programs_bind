import subprocess
import keyboard


#быстрое объяснение в цикле мы ожидаем когда пользователь нажмёт кнопку что бы исполнить файл 

        
def press_keyboard():
    while True:
        keyboard.wait("9")
        subprocess.Popen(r"C:\Users\agesoi\AppData\Roaming\Telegram Desktop\Telegram.exe")



