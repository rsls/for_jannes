"""
Writes dag file for hello_world.sh/hello_world.submit
This can and should also be done with the Option Parser
"""
import numpy as np
import random
import string
from datetime import date
from datetime import datetime
import os

"""
Define your parameters for your jobs, maxes, mins etc
Do this with Option Parser if possible to save changing this file every time
"""
job_number = 5
min_int = 0
max_int = 100
min_float = 0.5
max_float = 100.5
top_out_directory = '/user/rstanley/for_jannes/output/'

"""
Set up directories for particular time/date combinations for your dag files
"""
get_date = date.today().strftime('%Y%m%d')
get_time = datetime.now().strftime("%H%M%S")
dag_file_path = '/user/rstanley/for_jannes/dagfiles/{0}/{1}/'.format(get_date, get_time)
os.makedirs(dag_file_path, exist_ok=True)
dag_file = '/user/rstanley/for_jannes/dagfiles/{0}/{1}/run_hello_world_{0}_{1}.dag'.format(get_date, get_time)
outfile=open(dag_file, 'w')

out_directory = top_out_directory + str(get_date) + '_' + str(get_time)
os.makedirs(out_directory, exist_ok=True)

"""
Write to dag file for each job you want to run, remember to put spaces and line breaks in the right places
Line break after submit file is defined
Line break after all arguments are defined
Spaces between all arguments
"""
for job in range(job_number):
    job_int = random.randint(min_int, max_int)
    job_float = random.uniform(min_float, max_float)
    job_bool = random.choice([True, False])
    job_string = ''.join(random.choices(string.ascii_lowercase, k = 10))    

    outfile.write('JOB job_{0} /user/rstanley/for_jannes/hello_world.submit\n'.format(job)) #must have JOB keyword
    outfile.write('VARS job_{0} '.format(job)) #must have VARS keyword
    outfile.write('A="{0}" '.format(job_int)) #variable values must be quoted, ie surrounded by quote marks ""
    outfile.write('B="{0}" '.format(job_float)) #notice different quote mark types
    outfile.write('C="{0}" '.format(job_bool))
    outfile.write('D="{0}" '.format(job_string)) 
    outfile.write('OUT_DIR="{0}" '.format(out_directory))
    outfile.write('LOG_NAME="{0}"\n'.format(job_string)) #must write a log name and it must be UNIQUE to your job

outfile.close()
