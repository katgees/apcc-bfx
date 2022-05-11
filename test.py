#!/usr/local/bin/python3

import requests

def main():

    job_id = 'muscle-I20220509-233335-0712-47432951-p1m'
    type = job_id.split('-')
    type = type[0]

    # request
    request = requests.get('https://www.ebi.ac.uk/Tools/services/rest/'+type+'/result/'+job_id+'/aln-clustalw')
    print(request.text)

    alignment = request.text
    asterisk = 0
    colon = 0
    period = 0

    for char in alignment:
        if char == '*':
            asterisk+=1
        if char == ':':
            colon+=1
        if char == '.':
            period+=1

    print('*='+str(asterisk)+', :='+str(colon)+ ', .='+str(period))


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

