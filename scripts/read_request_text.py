#!/usr/local/bin/python3

import os
import requests

"""
    Python script to read requests.text 
"""


def read_request_text():
    # hardcoded job ID
    job_id = 'muscle-I20220514-204523-0793-10767007-p1m'

    # get job type from the job ID
    job_type = job_id.split('-')
    job_type = job_type[0]

    # request
    response = requests.get('https://www.ebi.ac.uk/Tools/services/rest/'
                            + job_type + '/result/'
                            + job_id + '/aln-clustalw')

    # save alignment results
    aln_clustalw = response.text

    # annotation counters
    asterisk = 0
    colon = 0
    period = 0

    for line in aln_clustalw:
        for char in line:
            if char == '*':
                asterisk += 1
            if char == ':':
                colon += 1
            if char == '.':
                period += 1


    print(aln_clustalw)
    print('Asterisks (*): ' + str(asterisk))
    print('Colons (:): ' + str(colon))
    print('Periods (.): ' + str(period))


read_request_text()
