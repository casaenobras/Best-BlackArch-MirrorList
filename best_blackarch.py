#!/usr/bin/python3
#coding: utf-8

import sys, getopt

from data import *
from bbdd import *
from results_bash import *
from save_file import *


order_mode = None

# Show help
def help_panel():
    
    print("\n[*] Este script testea los mirrors del repositorio de BlackArch, muestra los resultados y reemplaza el archivo blackarh-mirrorlist.")
    print("\n[*] Modo de uso:")
    print("\n\t-h     Muestra este panel de ayuda")
    print("\t-t     Realiza un nuevo test y guarda los resultados para examinarlos")
    print("\t-o     Modo de ordenar los resultados:")
    print("\t            vel_descarga: De mayor a menor velocidad de descarga")
    print("\t            tiempo_total: De menor a mayor tiempo en completar todo el proceso")
    print("\t            tiempo_conex: De menor a mayor tiempo en realizar la conexión")
    print("\t-n     Funciona en conjunto con -o, indica el numero de mirrors a mostar")
    print("\t-s     Descomenta los servidores seleccionados en el archivo blackarch-mirrorlist y comenta los restantes.")
    print("\t            Crea una copia de seguridad blackarch-mirrorlist.old")
    print("\t            Se necesitan permisos de root para reemplazar el archivo blackarch-mirrorlist.")
    print("\t            El argumento són los ID,s de los resultados obtenidos. Ej: ./best_blackarch.py -s 20,53,30")




def main(argv):

    if len(sys.argv) == 1:
        help_panel()

    try:
        opts, args = getopt.getopt(argv, "hto:n:s:")

    except getopt.GetoptError:
        print("\n[!] Opción no válida!!")
        help_panel()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ("-n"):
            limit = arg
        else:
            limit = ""

    for opt, arg in opts:
        if opt in ("-h"):
            help_panel()
            sys.exit()
        elif opt in ("-t"):
            create_db()
        elif opt in ("-n"):
            pass
        elif opt in ("-o"):
            order_mode = arg
            if order_mode == "vel_descarga" or order_mode == "tiempo_total" or order_mode == "tiempo_conex":
                print_results(ordenar(order_mode, limit))
            else:
                help_panel()
        elif opt in ("-s"):
            select = arg
            save_file(select)
        else:
            help_panel()
            sys.exit(1)

    if ordenar is None:
        help_panel()
    
    
if __name__ == '__main__':

    main(sys.argv[1:])