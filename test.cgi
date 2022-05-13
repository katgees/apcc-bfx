#!/usr/local/bin/python3

import cgi
import jinja2
import os
import requests

def main():

    print("Content-Type: text/html\n\n")

    # form
    form = cgi.FieldStorage()
    job = form.getvalue('job_id')

    if job == None:
        job = 'muscle-I20220509-233335-0712-47432951-p1m'

    # Jinja2
    template_loader = jinja2.FileSystemLoader(searchpath="./")  # find template
    env = jinja2.Environment(loader=template_loader)  # create environment
    template = env.get_template('output.html')  # load template

    # make request
    request = requests.get('https://www.ebi.ac.uk/Tools/services/rest/muscle/result/' + job + '/aln-clustalw')

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

    print(template.render(job_id=job, align=alignment, data=analysis))

if __name__ == '__main__':
    main()
