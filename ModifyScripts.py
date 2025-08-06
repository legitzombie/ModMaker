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

mod_utils_path = os.path.join("mod", "Utils")
reset_bat_path = os.path.join("mod", "Reset.bat")

replace_base_path = input("Asset path to replace \\archive\\base\\ with: ").strip()
replacement_name = input("Asset name: ").strip()
mod_name = input("Mod name: ").strip()

def process_bat_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    content = content.replace("\\archive\\base\\", replace_base_path)
    content = content.replace("CHANGETHENAME", replacement_name)
    content = content.replace("Custom.archive", mod_name + ".archive")

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


for filename in os.listdir(mod_utils_path):
    if not filename.lower().endswith('.bat') or filename.upper() == "GETHELPERS.BAT":
        continue
    process_bat_file(os.path.join(mod_utils_path, filename))


if os.path.isfile(reset_bat_path):
    process_bat_file(reset_bat_path)
    
new_mod_folder = mod_name
if not os.path.exists(new_mod_folder):
    os.rename("mod", new_mod_folder)
