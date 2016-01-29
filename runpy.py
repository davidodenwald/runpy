"""
Usage:
    autopy FILE
    autopy -h | --help

Options:
    -h --help   show this
"""

import docopt
import subprocess
import time

# get argument 'FILE'
args = docopt.docopt(__doc__)
file = args["FILE"]

# This while runs until you press ctr-c
# This must be changed to a more elegant soution!!!
while True:
    # read file
    text = open(file).read()

    # check if file content has changed
    # and sleep for 1 sec
    while text == open(file).read():
        time.sleep(1)

    # get screen width
    dims = subprocess.check_output(['stty size', 'r'], shell=True).split()
    width = int(dims[1].decode('utf-8'))

    # make title string
    title = "#" * int((width / 2 - 12)) + " Executing New Version  " + "#" * int((width / 2 - 12))

    # print title
    print(title)

    # prepare command for execution
    command = "python3", file

    # get time before command execution
    start_time = time.time()

    # execute command
    subprocess.call(command)

    # make result-title string
    title = "#" * int((width / 2 - 9)) + " Performance Data " + "#" * int((width / 2 - 9))

    # print result-title
    print(title)

    # print time the command has taken
    exec_time = str(time.time() - start_time) + " sec"
    print("#", exec_time, " " * (width - len(exec_time) - 5), "#")

    # print end seperator and newline
    print("#" * width + "\n")
