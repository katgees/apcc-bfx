#!/usr/local/bin/python3

import os
import requests

"""
    Python script to make ClustalW files using Requests Module 
"""
def make_file():
    job_id = 'muscle-I20220509-233335-0712-47432951-p1m'

    type = job_id.split('-')
    type = type[0]

    response = requests.get('https://www.ebi.ac.uk/Tools/services/rest/'
                            + type + '/result/'
                            + job_id + '/aln-clustalw')  # requests.get returns a status code

    aln_clustalw = response.text  # .text returns the content

    os.chdir('C:/Users/Katharina/Documents/GitHub/apcc-bfx/files')

    file = open((job_id + '.txt'), 'w')  # create and open file for alignment
    (aln_clustalw)  # write alignment to file
    file.close()  # close file


make_file()
