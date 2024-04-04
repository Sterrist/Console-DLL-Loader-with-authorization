import requests

DLL_LINK = '' # Ссылка на дллку которую будем инжектить
KEYS_LINK = '' # Ссылка на .txt файл с ключами(Каждый ключ не менее 10 символов)
DLL_NAME = requests.get('') # На сайте создаем файл с названием дллки(Которую скачиваем) в .txt файл пишем только название дллки ничего больше!
DLL_NAME = DLL_NAME.text
DLL_FOLDER = requests.get('') # Также как с dll_name только нужно написать путь к  папке где будет хранится скачаная дллка
DLL_FOLDER = DLL_FOLDER.text
PROCESS_NAME = requests.get('') # Также как с dll_name только нужно написать имя процесса в который будет инжектить
PROCESS_NAME = PROCESS_NAME.text
TEST_FILE_NAME = requests.get('') # Также как с dll_name только нужно написать имя любого файла для проверки админ прав
TEST_FILE_NAME = TEST_FILE_NAME.text
TEST_FILE_LINK = '' # ссылка на файл для проверки(Можно просто .txt с любым содержанием)
TEST_FILE_FOLDER = requests.get('') # Также как с dll_name только нужно написать путь к папке в которую прога будет пытаться переместить файл для проверки админ прав
TEST_FILE_FOLDER = TEST_FILE_FOLDER.text