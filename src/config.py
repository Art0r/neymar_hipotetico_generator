import os
from pathlib import Path


LOG_PATH = Path(__file__).parent.parent.as_posix() + "/.log"

DEBUG = bool(os.environ.get('DEBUG', '1'))