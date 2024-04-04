import os

from pymem import *
import config
import time

def inject():
    dll_path = f'{config.DLL_FOLDER}\\{config.DLL_NAME}'
    dll_path_bytes = bytes(dll_path, 'UTF-8')
    open_process = Pymem(config.PROCESS_NAME)
    try:
        process.inject_dll(open_process.process_handle, dll_path_bytes)
    except:
        try:
            os.remove(config.DLL_NAME)
        except:
            pass
        try:
            os.remove(f'{config.DLL_FOLDER}\\{config.DLL_NAME}')
        except:
            pass
        print(f'Запусти процесс {config.PROCESS_NAME}')
        time.sleep(5)
        exit()