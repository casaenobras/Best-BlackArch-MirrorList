# Best-BlackArch-MirrorList

This Console Script is written in python3, it is for ArchLinux distributions with BlackArch repositories for pentesting.  
You can install BlackArch, or its repository on ArchLinux from your [web](https://www.blackarch.org/).

### Table of contents
- [Best-BlackArch-MirrorList](#best-blackarch-mirrorlist)
    - [Table of contents](#table-of-contents)
- [What does](#what-does)
- [How to use](#how-to-use)
  - [Parameters:](#parameters)
- [Requirements](#requirements)


# What does

+ The latest version of the blackarch-mirrorlist file is downloaded from its [github](https://github.com/BlackArch/blackarch-site/blob/master/blackarch-mirrorlist).
+ Perform a download test of a random file with a size between 1Mb and 2Mb (ideal for slow connections)  
  of all the mirrors that exist in blackarch-mirrorlist.
+ Create a sqlite database to examine the results later.
+ Show the results by console in a table.
+ Create a backup of the file **/etc/pacman.d/blackarch-mirrorlist** with extension **.OLD**,  
  uncomment the selected mirrors and comment the rest (root permissions required).

This ensures better performance and speed in downloads and updates from the BlackArch repository.

# How to use

In order to use this script clone this repository into a directory, give execute permissions to the **best_blackarch.py** file.
~~~
  git clone https://github.com/casaenobras/Best-BlackArch-MirrorList
  chmod +x best_blackarch.py
~~~
run it:  
~~~
./best_blackarch.py [param]
~~~  
or  
~~~
python3 best_blackarch.py [param]
~~~  

## Parameters:

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

Parameters can be attached:
In this example it will first perform the test and immediately display the first five lines ordered by total time.

~~~
  ./best_blackarch -t -o total_time -n 5
~~~

# Requirements

See requirements.txt or execute

~~~
  pip install -r requirements.txt
~~~