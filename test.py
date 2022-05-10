#!/usr/local/bin/python3

import cgi
import json
import requests

def main():

    # form
    form = cgi.FieldStorage()
    job_id = form.getvalue('job_id')

    ###
    job_id = 'muscle-I20220509-233335-0712-47432951-p1m'
    ###

    # MUSCLE request
    request = requests.get('https://www.ebi.ac.uk/Tools/services/rest/muscle/result/'+job_id+'/aln-clustalw')
    print(request.text)

    # job ID list
    id_list = open('files/list.txt', 'a')
    id_list.write(job_id+'\n')
    id_list.close()

    # CLUSTAL MSA by MUSCLE alignments
    file = open(('files/'+job_id+'.txt'), 'w')
    file.write(request.text)
    file.close()

if __name__ == '__main__':
    main()

# Katharina Gees

