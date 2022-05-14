#!/usr/local/bin/python3

import cgi
import jinja2
import os
import requests

print("Content-Type: text/html\n\n")

# form
form = cgi.FieldStorage()
job_id = form.getvalue('job_id')

# to run w/o form input
if job_id == None:
    job_id = 'muscle-I20220513-220023-0114-59900534-p2m'

# Jinja2
template_loader = jinja2.FileSystemLoader(searchpath="./templates")  # find template
env = jinja2.Environment(loader=template_loader)  # create environment
template = env.get_template('output.html')  # load template

# save job IDs to text file
id_list = open('files/list.txt', 'a')  # open file for job IDs
id_list.write(job_id + '\n')  # write job ID to file
id_list.close()  # close ID list file

# make request
job_type = job_id.split('-')
job_type = job_type[0]
response = requests.get('https://www.ebi.ac.uk/Tools/services/rest/'
                        + job_type + '/result/'
                        + job_id + '/aln-clustalw')  # requests.get returns a status code

aln_clustalw = response.text  # .text returns the content

os.chdir('../apcc-bfx/files')

file = open((job_id + '.txt'), 'w')  # create and open file for alignment
file.write(aln_clustalw)  # write alignment to file
file.close()  # close file

file_list = os.listdir()  # returns a list of the files in cwd

file_name = [i for i in file_list if i.startswith(job_type)]
job_file = file_name[0]

aln = []
asterisk = 0
colon = 0
period = 0

file = open(job_file)
for line in file:
    line = line.rstrip('\n')
    aln.append(line)
    for char in line:
        if char == '*':
            asterisk += 1
        if char == ':':
            colon += 1
        if char == '.':
            period += 1

print(template.render(ji=job_id, aln=aln, ast=asterisk, col=colon, per=period))

# Katharina Gees
