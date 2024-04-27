import os
from pathlib import Path

# cwd current work dir
print(os.getcwd())
print(Path.cwd())

os.chdir('../..')
print(os.getcwd())
print(Path.cwd())
