#!/usr/local/bin/python3

import os

"""
    Python script to read Clustal* files 
"""


def read_file():
    # hardcoded job type
    job_type = 'muscle'

    # change directory to files
    os.chdir('../files')

    # get list of the files in cwd
    file_list = os.listdir()

    # get job ID == file name from file list
    file_name = [i for i in file_list if i.startswith(job_type)]
    job_id = file_name[0]

    # annotation counters
    asterisk = 0
    colon = 0
    period = 0

    # read file and count annotations
    file = open(job_id)
    for line in file:
        for char in line:
            if char == '*':
                asterisk += 1
            if char == ':':
                colon += 1
            if char == '.':
                period += 1

    # pring file name and annotation counts
    print('File name: ' + file.name)
    print('Asterisks (*): ' + str(asterisk))
    print('Colons (:): ' + str(colon))
    print('Periods (.): ' + str(period))


read_file()
