#!/usr/local/bin/python3

import os
import requests

"""
    Python script to make Clustal* files using Requests Module 
"""


def make_file():
    # hardcoded job ID
    job_id = 'muscle-I20220509-233335-0712-47432951-p1m'

    # get job type rom job ID
    job_type = job_id.split('-')
    job_type = job_type[0]

    # request
    response = requests.get('https://www.ebi.ac.uk/Tools/services/rest/'
                            + job_type + '/result/'
                            + job_id + '/aln-clustalw')

    # save alignment results
    aln_clustalw = response.text

    # change directory to files
    os.chdir('../files')

    # create and write alignment file
    file = open((job_id + '.txt'), 'w')
    file.write(aln_clustalw)
    file.close()

    # print file name and path
    print('File created: ' + file.name)
    print('File path: ' + os.path.abspath(file.name))


make_file()
