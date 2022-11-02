
import shutil
import sys
import os
import requests

from bbdd import server_sel


# Create a backup of "blackarch-mirrorlist", update it from the official page and
# uncomments selected mirrors
def save_file(select):

    url_mirrorList = "https://raw.githubusercontent.com/BlackArch/blackarch-site/master/blackarch-mirrorlist"
    original_file = "/etc/pacman.d/blackarch-mirrorlist"
    backup_file = "/etc/pacman.d/blackarch-mirrorlist.OLD"
    sel = server_sel(select)
    content = list()

    euid = os.geteuid()
    if euid != 0:
        args = ['sudo', sys.executable] + sys.argv + [os.environ]
        os.execlpe('sudo', *args)

    shutil.copy(original_file, backup_file)

    try:
        data = requests.get(url_mirrorList).text
        with open(original_file, 'w') as file:
            file.writelines(data)

        file.close()

        with open(original_file, 'r') as file:
            content = file.readlines()
            for index, linea in enumerate(content):
                if linea[0] != "#" and linea != "\n":
                    linea = "#" + linea
                    content[index] = linea

        file.close()

        for server in sel:
            for index, linea in enumerate(content):
                if server[1] in linea:
                    linea = linea[1:]
                    content[index] = linea

        with open(original_file, 'w') as file:
            file.writelines(content)

        file.close()

        print("\n[+] The changes have been made successfully!!\n")

    except:

        shutil.copy(backup_file, original_file)
