#!e:\Flasky\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'alembic==0.7.7','console_scripts','alembic'
__requires__ = 'alembic==0.7.7'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('alembic==0.7.7', 'console_scripts', 'alembic')()
    )
