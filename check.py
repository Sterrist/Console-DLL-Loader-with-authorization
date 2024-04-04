import requests
import time
import config
import shutil
import os

getkey = requests.get(config.KEYS_LINK)

def checkkey(key):
    if key in getkey.text:
        pass
    else:
        print('Не верный ключ!')
        time.sleep(2)
        exit()

def checkkey_none(key):
    if len(key) < 10:
        print('Не верный ключ!')
        exit()
    else:
        pass

def checkexistencefile():
    try:
        shutil.move(config.DLL_NAME, config.DLL_FOLDER)
    except shutil.Error:
        os.remove(f'{config.DLL_FOLDER}\\{config.DLL_NAME}')
        shutil.move(config.DLL_NAME, config.DLL_FOLDER)
    except:
        os.remove(config.DLL_NAME)
        print('Запусти программу от имени администратора!')
        time.sleep(5)
        exit()