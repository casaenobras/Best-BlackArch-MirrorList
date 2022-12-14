
from genericpath import isfile

# Print the table with the results


def print_results(results):

    if isfile("mirrors.db"):

        print("|----|--------------------------------------------------------------|----------------------|----------------------|----------------------|----------------------|")
        print("| {:^2} | {:^60} | {:^20} | {:^20} | {:^20} | {:^20} |".format(
            'ID', 'Mirror', 'SizeDownload (Kb)', 'SpeedDonwload (Kb/s)', 'ConnectTime (ms)', 'TotalTime (ms)'))
        print("|----|--------------------------------------------------------------|----------------------|----------------------|----------------------|----------------------|")

        for i in results:
            id, mirror, s_down, speed_down, c_time, t_time = i

            print("| {:^2} | {:^60} | {:^20} | {:^20} | {:^20} | {:^20} |".format(
                id, mirror, s_down, speed_down, c_time, t_time))
            print("|----|--------------------------------------------------------------|----------------------|----------------------|----------------------|----------------------|")
