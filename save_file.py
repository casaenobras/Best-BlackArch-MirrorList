import shutil, sys, os

from bbdd import server_sel

#Reescribe el archivo blackarch-mirrorlist con los mirrors seleccionados descomentados
def save_file(select):

    orin_file = "/etc/pacman.d/blackarch-mirrorlist"
    back_file = "/etc/pacman.d/blackarch-mirrorlist.OLD"
    sel = server_sel(select)
    contenido = list()

    euid = os.geteuid() 
    if euid != 0: 
        args = ['sudo', sys.executable] + sys.argv + [os.environ]
        os.execlpe('sudo', *args)

    shutil.copy(orin_file, back_file)

    try:
        with open(orin_file, 'r') as file:
            contenido = file.readlines()
            for index, linea in enumerate(contenido):
                if linea[0] != "#" and linea != "\n":
                    linea = "#" + linea
                    contenido[index] = linea

        file.close()

        for server in sel:
            for index, linea in enumerate(contenido):
                if server[1] in linea:
                    linea = linea[1:]
                    contenido[index] = linea
        
        with open(orin_file, 'w') as file:
            file.writelines(contenido)
        
        file.close()
    
    except:

        shutil.copy(back_file, orin_file)
    
