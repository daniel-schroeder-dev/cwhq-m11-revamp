#!/home/daniel/Public/cwhq/curriculum/m11-revamp/m11/.venv/bin/python

import os

os.system("cp ../m11-transcrypt/wizardlib/builtins.py ./")
os.system(f"python -m transcrypt -b -m -n index.py")
