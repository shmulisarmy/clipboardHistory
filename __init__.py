"""acts as a single dependency manager, following the dry principle"""


import pyperclip
import json
import os.path
from time import sleep
from colorama import Fore as f


   

json_filename = "clipboard_content.json"

print(f"the {__name__} is being used")