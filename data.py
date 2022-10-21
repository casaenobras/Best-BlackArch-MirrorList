import pycurl, sys, requests, re, random

from pwn import *

 
# Return a list with the servers extracted from the official website
def get_mirrorList():

    url_mirrorList = "https://raw.githubusercontent.com/BlackArch/blackarch-site/master/blackarch-mirrorlist"

    list_mirrors = []

    try:
        data = requests.get(url_mirrorList).text

        data = data.split()

        for line in data:
            if re.findall('^[fh]', line):
                line = line[0:-14]
                list_mirrors.append(line)

    except:
        print("\n[!] No se puede conectar con " + url_mirrorList + ". Comprueba tu conexión a internet")
        sys.exit(1)
        
    return list_mirrors

# Returns a random file from the server to perform the test
def get_random_file(mirrorlist):

    files = []
    file_name = ""
    file_size = 0

    complet_server = mirrorlist[0] + "blackarch/os/x86_64/"

    data = requests.get(complet_server).text

    data = data.split()

    for line in data:
        
        if re.findall('^href', line):
            index_1 = line.index('"') + 1
            index_2 = line.index('>') - 1
            file_name_temp = str(line[index_1:index_2])
            
            if not re.findall('sig$', file_name_temp):
                file_name = file_name_temp

        if re.findall('^[0-9]+$', line):
            file_size = int(line)

        if file_size > 1000000 and file_size < 2000000:
            files.append(file_name)

    n_files = len(files)

    r = random.randint(0, n_files)
 
    return files[r]

# Returns a list of data obtained from each server
def get_datos(mirrorlist):

    file_test = "blackarch/os/x86_64/" + get_random_file(mirrorlist)
    data_list = []
    n_mirrors = len(mirrorlist)
    acco_mirrors = 1
    progress = log.progress("Testing")

    for server in mirrorlist:
        URL = server + file_test
        c = pycurl.Curl()
        c.setopt(pycurl.URL, URL)
        c.setopt(pycurl.CONNECTTIMEOUT, 10)

        try:
            progress.status(server + " " + str(acco_mirrors) + " of " + str(n_mirrors))
            c.perform_rb()

            CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
            TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
            SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
            SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

            server_result = (str(server), int(SIZE_DOWNLOAD / 1024), int(SPEED_DOWNLOAD / 1024), int(CONNECT_TIME * 1000), int(TOTAL_TIME * 1000))

            data_list.append(server_result)
            
        except :
            pass

        c.close()

        acco_mirrors += 1

    return data_list

def def_handler(sig, frame):
    print("\n[!] Exiting.....\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)