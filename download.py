import requests
import config

def download_dll():
    filename = config.DLL_LINK.split('/')[-1]
    r = requests.get(config.DLL_LINK, allow_redirects=True)
    open(filename, "wb").write(r.content)
def download_test_dll():
    filename = config.TEST_FILE_LINK.split('/')[-1]
    r1 = requests.get(config.TEST_FILE_LINK, allow_redirects=True)
    open(filename, "wb").write(r1.content)