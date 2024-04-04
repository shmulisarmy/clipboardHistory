from __init__ import *

"""this file is used for retrieving an item from json to the clipboard"""

def red(text):
       """returns text in red"""
       return f"{f.RED}{text}{f.RESET}"

def blue(text):
       """returns the text in blue"""
       return f"{f.BLUE}{text}{f.RESET}"




if os.path.exists(json_filename):
    with open(json_filename, 'r') as json_file:
                data = json.load(json_file)
else:
    data = {"clipboard_content": []}


print("your clipboard: - - - - - - - - - - - -")
print(*data["clipboard_content"], sep="\n")
for i in range(len(data["clipboard_content"])):
       print(f'{red(i)} - {blue(data["clipboard_content"][i])}')
print()

index = int(input("enter an index to copy: "))
pyperclip.copy(data["clipboard_content"][index])
print(f'{data["clipboard_content"][index]} has been copied to your clipboard')