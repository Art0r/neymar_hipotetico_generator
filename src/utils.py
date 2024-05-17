from datetime import date, datetime
import os
import sys

from config import LOG_PATH

def get_resource_path(relative_path):
    ''' 
    Get absolute path to resource, works for dev and for PyInstaller 
    '''
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def write_log() -> None:
    
    open(LOG_PATH, 'w').write(f"Last Tweet - {datetime.now().strftime('%d-%m-%Y')}")


def retrieve_log_and_verify(now: date) -> bool:

    if not os.path.isfile(LOG_PATH):
        return False

    date = open(LOG_PATH, 'r').read().split(" - ")[1]

    return now.strftime('%d-%m-%Y') == date