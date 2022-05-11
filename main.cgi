#!/usr/local/bin/python3

import cgi
import jinja2
import os
import requests

def main():

    # form
    form = cgi.FieldStorage()
    job_id = form.getvalue('job_id')

    if job_id == None:
        job_id = 'muscle-I20220509-233335-0712-47432951-p1m'

    # Jinja2
    template_loader = jinja2.FileSystemLoader(searchpath="./")  # find template
    env = jinja2.Environment(loader=template_loader)  # create environment
    template = env.get_template('output.html')  # load template

    # make request
    type = job_id.split('-')
    type = type[0]
    request = requests.get('https://www.ebi.ac.uk/Tools/services/rest/' + type + '/result/' + job_id + '/aln-clustalw')

    alignment = request.text
    asterisk = 0
    colon = 0
    period = 0
    analysis = []

    for char in alignment:
        if char == '*':
            asterisk+=1
        if char == ':':
            colon+=1
        if char == '.':
            period+=1

    analysis.append(asterisk)
    analysis.append(colon)
    analysis.append(period)

    # save data
    id_list = open('files/list.txt', 'a')       # open file for job IDs
    id_list.write(job_id+'\n')                  # write job ID to file
    id_list.close()                             # close ID list file
    file = open(('files/'+job_id+'.txt'), 'w')  # create and open file for alignment
    file.write(request.text)                    # write alignment to file
    file.close()                                # close file

    print("Content-Type: text/html\n\n")
    print(template.render(job_id=job_id, align=alignment, data=analysis))

if __name__ == '__main__':
    main()
