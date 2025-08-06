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
num_asset_names = int(input("How many asset names to change? ").strip())
replacement_names = []
for i in range(num_asset_names):
    name = input(f"Asset name #{i}: ").strip()
    replacement_names.append(name)
mod_name = input("Mod name: ").strip()

def process_bat_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    changethename_replaced = False

    for line in lines:
        new_lines.append(line)

        if "CHANGETHENAME" in line and not changethename_replaced:
            line = line.replace("CHANGETHENAME", replacement_names[0])
            new_lines[-1] = line 
            changethename_replaced = True

            for asset_name in replacement_names[1:]:
                new_copy_line = f'    copy "%%f" "%dest_path%{asset_name}!ext!" >nul\n'
                new_lines.append(new_copy_line)

    content = "".join(new_lines)
    content = content.replace("\\archive\\base\\", replace_base_path)
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
