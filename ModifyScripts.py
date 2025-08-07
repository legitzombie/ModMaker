#  ▄▄▄██▀▀▀▄▄▄       ███▄ ▄███▓▓█████   ██████
#    ▒██  ▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ ▒██    ▒
#    ░██  ▒██  ▀█▄  ▓██    ▓██░▒███   ░ ▓██▄
# ▓██▄██▓ ░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄   ▒   ██▒
#  ▓███▒   ▓█   ▓██▒▒██▒   ░██▒░▒████▒▒██████▒▒
#  ▒▓▒▒░   ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░
#  ▒ ░▒░    ▒   ▒▒ ░░  ░      ░ ░ ░  ░░ ░▒  ░ ░
#  ░ ░ ░    ░   ▒   ░      ░      ░   ░  ░  ░
#  ░   ░        ░  ░       ░      ░  ░      ░
#
#          ▄▄▄█████▓ ██░ ██ ▓█████
#          ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀
#          ▒ ▓██░ ▒░▒██▀▀██░▒███
#          ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄
#            ▒██▒ ░ ░▓█▒░██▓░▒████▒
#            ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░
#              ░     ▒ ░▒░ ░ ░ ░  ░
#            ░       ░  ░░ ░   ░
#                    ░  ░  ░   ░  ░
#
#  ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███
# ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
# ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
# ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄
# ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
#  ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
#  ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
#  ░  ░░ ░  ░   ▒   ░        ░ ░░ ░    ░     ░░   ░
#  ░  ░  ░      ░  ░░ ░      ░  ░      ░  ░   ░

import os
import sys

if len(sys.argv) > 1:
    choice = sys.argv[1]
else:
    choice = "0"


mod_utils_path = os.path.join("mod", "Utils")
reset_bat_path = os.path.join("mod", "Reset.bat")

num_asset_names = 0
atlas_name = ""

replace_base_path = input("Folder Path: ").strip()
if choice == "1":
    num_asset_names = int(input("How many files? ").strip())
elif choice == "2":
    atlas_name = input("Atlas name: ").strip()
    num_asset_names = int(input("How many parts? ").strip())
    
replacement_names = []

for i in range(num_asset_names):
    if choice == "1":
        name = input(f"Filename #{i}: ").strip()
    elif choice == "2":
        name = input(f"Partname #{i}: ").strip()
    replacement_names.append(name)
mod_name = input("Mod name: ").strip()

def process_bat_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    changethename_replaced = False

    for line in lines:
        original_line = line 

        if "INKATLASPATH" in line:
            line = line.replace('"INKATLASPATH"', f'"{replace_base_path[1:-1]}"')

        if "CUSTOMINKATLASNAME" in line:
            line = line.replace('CUSTOMINKATLASNAME', f'{atlas_name}')

        if "CHANGETHENAME" in line and not changethename_replaced:
            line = line.replace("CHANGETHENAME", replacement_names[0])
            changethename_replaced = True

            new_lines.append(line) 

            for asset_name in replacement_names[1:]:
                new_copy_line = f'    copy "%%f" "%dest_path%{asset_name}!ext!" >nul\n'
                new_lines.append(new_copy_line)
        else:
            new_lines.append(line)

    content = "".join(new_lines)
    content = content.replace("\\archive\\base\\", replace_base_path)
    content = content.replace("Custom.archive", mod_name + ".archive")
    content = content.replace("custom.", mod_name.lower() + ".")
    content = content.replace("custom", mod_name.lower())
    

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)



for filename in os.listdir(mod_utils_path):
    if filename.upper() == "GETHELPERS.BAT":
        continue
    process_bat_file(os.path.join(mod_utils_path, filename))


if os.path.isfile(reset_bat_path):
    process_bat_file(reset_bat_path)
    
new_mod_folder = mod_name
os.rename("mod", new_mod_folder)
