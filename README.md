# Best-BlackArch-MirrorList

Este Script para consola está escrito en python3, es para distribuciones ArchLinux con los repositorios de BlackArch para pentesting.  
Puede instalar BlackArch, o su repositorio en ArchLinux desde su [web](https://www.blackarch.org/)

- [Best-BlackArch-MirrorList](#best-blackarch-mirrorlist)
- [Que hace](#que-hace)
- [Modo de uso](#modo-de-uso)
    - [Parámetros:](#parámetros)


# Que hace

+ Se descarga la última version el archivo blackarch-mirrorlist desde su [github](https://github.com/BlackArch/blackarch-site/blob/master/blackarch-mirrorlist)
+ Realiza un test de descarga de un archivo aleatorio con un tamaño entre 1Mb y 2Mb (ideal para conexiones lentas)  
  de todos los mirrors que existen en blackarch-mirrorlist
+ Crea una base de datos sqlite para examinar los resulatados más adelante
+ Muestra los resultados por consola en una tabla
+ Crea una copia de seguridad del archivo **/etc/pacman.d/blackarch-mirrorlist** con extensión .OLD,  
  descomenta los mirrors seleccionados y comenta los restantes(es necesario tener permisos de root)

Con esto se asegura un mejor funcionamiento y velocidad en descargas y actualizaciones desde el repositorio de BlackArch

# Modo de uso

Para poder usar este script clone este repositorio en un directorio, de permisos de ejecución al archivo *best_blackarch.py*.
~~~
  chmod +x best_blackarch.py
~~~
Ejecutelo:  
~~~
./best_blackarch.py [param]
~~~  
or  
~~~
python3 best_blackarch.py [param]
~~~  

### Parámetros:

+ **-h**     Displays the help panel
  ~~~
  ./best_blackarch -h
  ~~~
+ **-t**     Take a new test and save the results for examination
  ~~~
  ./best_blackarch -t
  ~~~
+ **-o**     How to sort results
    + download_speed: From highest to lowest download speed
    + total_time: From shorter to longer to complete the entire process
    + connect_time: From shorter to longer to make the connection
  ~~~
  ./best_blackarch -o download_speed
  ~~~
+ **-n**     Indicates the number of lines to be displayed
  ~~~
  ./best_blackarch -o download_speed -n 10
  ~~~
+ **-s**     Uncomments the selected servers in the blackarch-mirrorlist file and comments out the remaining servers
  ~~~
  ./best_blackarch -s 20,53,59
  ~~~

De una manera más rápida se pueden unir parametros:
~~~
  ./best_blackarch -t -o total_time -n 5
~~~
En este ejemplo primero realizará el test e inmediatamente mostrará las cinco primeras lineas ordenadas por el tiempo total