#!/usr/local/bin/python3

import requests

def main():

    job_id = 'muscle-I20220509-233335-0712-47432951-p1m'
    request = requests.get('https://www.ebi.ac.uk/Tools/services/rest/muscle/result/'+job_id+'/aln-clustalw')
    print(request.text)

    id_list = open('files/list.txt', 'a')
    id_list.write(job_id+'\n')

    id_list.close()

if __name__ == '__main__':
    main()

# Katharina Gees

