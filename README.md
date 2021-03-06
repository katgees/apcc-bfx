# MSA Viewer

**AS.410.712 Advanced Practical Computer Concepts for Bioinformatics**

**Final Project**

**Katharina Gees**

***
### Getting Started
In order to use the MSA viewer, you will need a recent (within the 
last 7 days) multiple sequence alignment (MSA) from EMBL-EBI. There
are multiple MSA tools available at https://www.ebi.ac.uk/Tools/msa/,
however only 4 of them generate results in ClustalW format 
which is required for this viewer. These are the 4 tools: Clustal 
Omega, MAFFT*, MUSCLE, and T-Coffee.

**Please note that the default output format for Clustal Omega is 
Clustal with character counts and the default format for MAFFT is 
Pearson/FASTA. Only use ClustalW.*

>The **files** folder in the repository contains a text file called
> **job_id_list.txt** which contains some MSA job IDs, though they 
> may be 'expired'.

>To quickly generate MSA results/acquire a job ID you can use 
> the 'example sequence' option.

#### Prerequisites
1. Have a basic understanding of UNIX OS/command line and Python, and have
these technologies installed.
2. Install these required Python modules:

   * cgi
   * cgitb
   * jinja2
   * requests

3. Download the entire GitHub repository.

### Using the Demos

There are 2 demonstration versions of the MSA viewer.

1. To see what the input and output pages should look like without running 
the project, open the **demo_input.html** file in your browser. The form 
on this page is "fake" so you can enter anything or leave it blank. The 
submit button is also "fake". This button is a link to the **demo_view.html** 
file. The **demo_view.html** can also be viewed without using the fake input 
page. The html code in the file was generated using the **demo.cgi** with 
the **demo_output.html** template. 
2. To see what the main project does with input use the **demo.cgi** file.
This can be done by: (1) changing the permissions of the file (*$ chmod 755* 
***demo.cgi***), (2) converting the file to UNIX format (*$ dos2unix
**demo.cgi***),(3) running the file (*$ ./**demo.cgi***), and (4) viewing
the file in your browser.

**All HTML files use the **css.css** style sheet.*

### Using the Main

**These instructions assume that you have read through and completed the 
'Getting Started' and 'Prerequisites' sections above.*

1. Use *$ cd* to relocate cwd to within the **apcc-bfx** folder.
2. Run these commands on the command line (replacing asterisk with *):
   1. *$ chmod -R 755 asterisk*
   2. *$cd **files***
   3. *$ chmod 777 asterisk**
   4. *$cd ..**
   5. *$dos2unix **main.cgi***
   6. *$./**main.cgi***
3. View **input.html** in your browser.
4. Input the job ID into the form.
5. Click the submit button
6. View the MSA viewer.

***
### Resources

The **scripts** folder in the repository contains multiple scripts related 
to the project. These scripts perform different tasks which are combined 
within the cgi files.

* **make_file.py** - Python script to make Clustal* files using Requests Module
* **make_request.py** - Python script to examine requests module 
* **read_file.py** - Python script to read Clustal* files
* **read_request_text.py** - Python script to read requests.text

These exist as "building blocks" for future projects.

>The tar.gz file was created using *$ tar czf 
tarball-apcc-bfx.tar.gz **apcc-bfx***.