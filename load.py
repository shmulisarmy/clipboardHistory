
from __init__ import * 

def save_to_json(filename, text):
    # Check if the JSON file exists
    if os.path.exists(filename):
        # If the file exists, load its content
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
    else:
        # If the file doesn't exist, create an empty list
        data = {"clipboard_content": []}

    # Get the content from the clipboard
    
    # Append the clipboard content to the list
    if text not in data["clipboard_content"]:
        data["clipboard_content"].append(text)
    
    # Write the updated data to the JSON file
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"{text} has been appended '{filename}' successfully.")



def main():
    recent = None
    while True:
        copied = pyperclip.paste()
        if copied == recent:
            sleep(5)
            continue
        recent = copied
        save_to_json(json_filename, copied)


if __name__ == "__main__":
    main()    
