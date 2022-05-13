#!/usr/local/bin/python3

import os

"""
    Python script to read ClustalW files 
"""


def read_file():
    msa_type = 'muscle'  # hardcoded job type

    os.chdir('C:/Users/Katharina/Documents/GitHub/apcc-bfx/files')
    file_list = os.listdir()  # returns a list of the files in cwd

    file_name = [i for i in file_list if i.startswith(msa_type)]
    job_id = file_name[0]

    asterisk = 0
    colon = 0
    period = 0

    file = open(job_id)
    for line in file:
        for char in line:
            if char == '*':
                asterisk += 1
            if char == ':':
                colon += 1
            if char == '.':
                period += 1

    print('File name: ' + file.name)
    print('* (asterisks): ' + str(asterisk))
    print(': (colons): ' + str(colon))
    print('. (periods): ' + str(period))


read_file()
