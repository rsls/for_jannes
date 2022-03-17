#!/bin/bash

# This is a bash script, learn to use them, they are all powerful
# When writing bash scripts, don't forget the #!/bin/bash as above

# These comments are not necessary but they help me to remember the numbering for the different arguments
# Notice different syntax for .sh and .submit files! 
# 3 arguments to run the hello world python script
# Arguments = $(A) $(B) $(C) $(D) $(OUT_DIR)
# Numbering = ${1} ${2} ${3} ${4} ${5}

# Variables defined in bash script must be defined in this syntax, no spaces allowed
output_file="${5}/hello_world_${4}_sh.txt"

echo "This is the output from the bash script"

# You should try to work in the temporary directory, ${TMPDIR} is always defined
mkdir -p ${TMPDIR}
cd ${TMPDIR}

# Create any output directories you need before running things
mkdir -p ${5}

echo Evaluating environment
# Evaluate environments needed to run your scripts correctly
eval `/cvmfs/icecube.opensciencegrid.org/py3-v4.0.1/setup.sh`


echo Starting python script
# Run python script, direct output to output file variable defined above
python /user/rstanley/for_jannes/hello_world.py -a ${1} -b ${2} -c ${3} -d ${4} > ${output_file}

echo Copying files
# Copy any files created by your scripts to their intended destination
cp -rf hello_world_*_py.txt ${5}


