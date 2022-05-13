#!/usr/local/bin/python3

import jinja2
import os
import requests

# DEMO ONLY
job_id = 'muscle-I20220513-220023-0114-59900534-p2m'  # hardcoded job id
# DEMO ONLY

templateLoader = jinja2.FileSystemLoader(searchpath="./templates")  # find template
env = jinja2.Environment(loader=templateLoader)  # create environment
template = env.get_template('demo.html')  # load template

id_list = open('files/list.txt', 'a')  # open file for job IDs
# id_list.write(job_id + '\n')  # write job ID to file
id_list.close()  # close ID list file

job_type = job_id.split('-')
job_type = job_type[0]

response = requests.get('https://www.ebi.ac.uk/Tools/services/rest/'
                        + job_type + '/result/'
                        + job_id + '/aln-clustalw')  # requests.get returns a status code

aln_clustalw = response.text  # .text returns the content

os.chdir('C:/Users/Katharina/Documents/GitHub/apcc-bfx/files')

file = open((job_id + '.txt'), 'w')  # create and open file for alignment
file.write(aln_clustalw)  # write alignment to file
file.close()  # close file

file_list = os.listdir()  # returns a list of the files in cwd

file_name = [i for i in file_list if i.startswith(job_type)]
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

print("Content-Type: text/html\n\n")
print(template.render(ji=job_id, aln=aln_clustalw, ast=asterisk, col=colon, per=period))
