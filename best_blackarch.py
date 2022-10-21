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
    
    print("\n[*] This script tests the mirrors in the BlackArch repository, displays the results and replaces the blackarch-mirrorlist file for faster download and update")
    print("\n[*] How to use:")
    print("\n\t-h     Displays this help panel")
    print("\t-t     Take a new test and save the results for examination")
    print("\t-o     How to sort results:")
    print("\t            download_speed: From highest to lowest download speed")
    print("\t            total_time: From shorter to longer to complete the entire process")
    print("\t            connect_time: From shorter to longer to make the connection")
    print("\t-n     Works in conjunction with -o, indicates the number of mirrors to be displayed")
    print("\t-s     Uncomments the selected servers in the blackarch-mirrorlist file and comments out the remaining servers.")
    print("\t            Create a blackarch-mirrorlist.old backup")
    print("\t            Root permissions are required to replace blackarch-mirrorlist file.")
    print("\t            The argument is the ID,s of the results obtained. Ex: ./best_blackarch.py -s 20,53,30...")




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
            if order_mode == "download_speed" or order_mode == "total_time" or order_mode == "connect_time":
                print_results(order(order_mode, limit))
            else:
                help_panel()
        elif opt in ("-s"):
            select = arg
            save_file(select)
        else:
            help_panel()
            sys.exit(1)

    if order is None:
        help_panel()
    
    
if __name__ == '__main__':

    main(sys.argv[1:])