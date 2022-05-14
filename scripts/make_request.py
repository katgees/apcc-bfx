#!/usr/local/bin/python3

import json
import requests

"""
    Python script to examine requests module 
"""


def make_request():
    job_id = 'muscle-I20220514-204523-0793-10767007-p1m'

    job_type = job_id.split('-')
    job_type = job_type[0]

    response = requests.get('https://www.ebi.ac.uk/Tools/services/rest/'
                            + job_type + '/result/'
                            + job_id + '/aln-clustalw')

    # requests module methods
    print('.apparent_encoding = ' + json.dumps(response.apparent_encoding))
    print('.encoding = ' + json.dumps(response.encoding))
    print('.history = [' + ', '.join(response.history) + ']')
    print('.links = ' + json.dumps(response.links))
    print('.status_code = ' + str(response.status_code))
    print('.text = ' + response.text)
    print('.url = ' + response.url)


make_request()
