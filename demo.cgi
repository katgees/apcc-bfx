#!/usr/local/bin/python3

import jinja2
import requests

# CGI error reporting
import cgitb
cgitb.enable()

print("Content-Type: text/html\n\n")

# DEMO ONLY
job_id = 'muscle-I20220513-220023-0114-59900534-p2m'  # hardcoded job id
# DEMO ONLY

# Jinja2
templateLoader = jinja2.FileSystemLoader(searchpath="./templates")  # find template
env = jinja2.Environment(loader=templateLoader)  # create environment
template = env.get_template('demo_output.html')  # load template

# save job IDs to text file (list)
id_list = open('files/job_id_list.txt', 'a')  # open file for job IDs
id_list.write(job_id + '\n')  # write job ID to file
id_list.close()  # close ID list file

# make request
job_type = job_id.split('-')
job_type = job_type[0]
response = requests.get('https://www.ebi.ac.uk/Tools/services/rest/'
                        + job_type + '/result/'
                        + job_id + '/aln-clustalw')  # requests.get returns a status code

# save alignment to text file
aln_clustalw = response.text  # .text returns the content
file = open('files/alignment.txt', 'w')  # open file for alignment
file.write(aln_clustalw)  # write alignment to file
file.close()  # close file

# save alignment to text file (list)
file = open('files/alignment_list.txt', 'a')  # open list for alignments
file.write(aln_clustalw + '\n')  # write alignment to list
file.close()  # close file

# variables
aln = []
asterisk = 0
colon = 0
period = 0

file = open('files/alignment.txt')
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
