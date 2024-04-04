import ctypes
import shutil
import time
import os
import config
import inject
import check
import download

ctypes.windll.kernel32.SetConsoleTitleA(b"DLL-LOADER")

download.download_test_dll()
try:
    shutil.move(config.TEST_FILE_NAME, config.TEST_FILE_FOLDER)
    os.remove(f'{config.TEST_FILE_FOLDER}\\{config.TEST_FILE_NAME}')
except:
    os.remove(config.TEST_FILE_NAME)
    print('Запусти программу от имени администратора!')
    exit()

print('')
print('     ██████╗░██╗░░░░░██╗░░░░░░░░░░░██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░')
print('     ██╔══██╗██║░░░░░██║░░░░░░░░░░░██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗')
print('     ██║░░██║██║░░░░░██║░░░░░█████╗██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝')
print('     ██║░░██║██║░░░░░██║░░░░░╚════╝██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗')
print('     ██████╔╝███████╗███████╗░░░░░░███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║')
print('     ╚═════╝░╚══════╝╚══════╝░░░░░░╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝')
print('')

key = input('Введи свой ключ: ')

check.checkkey_none(key)
check.checkkey(key)
download.download_dll()
check.checkexistencefile()
inject.inject()
print('DLL Загружен')
time.sleep(2)
