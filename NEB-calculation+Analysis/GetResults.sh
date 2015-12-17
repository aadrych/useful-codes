#!/bin/bash

# ---------------------------------------------------------------------------------------------------
#                       Get results for simple bulk modulus calculation
# ---------------------------------------------------------------------------------------------------
# Author:  C P Race
# Email:   christopher.race@manchester.ac.uk
# Date:    2015 / 01 / 06
# ---------------------------------------------------------------------------------------------------
# Description: Simple (bash) shell script to post process results of neb calculation
#
# ---------------------------------------------------------------------------------------------------

outputFile1=resultsInitial.txt
outputFile2=resultsFinal.txt
#echo "" | awk '{printf "%-20s %-20s\n", "#Coord", "Energy (eV)"}' > ${outputFile1}
#echo "" | awk '{printf "%-20s %-20s\n", "#Coord", "Energy (eV)"}' > ${outputFile2}

nreplicas=10

COUNTER=0
while [  $COUNTER -lt $nreplicas ]
do
	col1=$(( 2*COUNTER+10 ))
	col2=$(( 2*COUNTER+11 ))
	
	file="../log.lammps"
	tail -6 ${file} | head -1 | awk '{printf "%-20s %-20s\n", $'${col1}', $'${col2}'}' >> ${outputFile1}
	tail -1 ${file} | head -1 | awk '{printf "%-20s %-20s\n", $'${col1}', $'${col2}'}' >> ${outputFile2}
	
	let COUNTER=COUNTER+1
done