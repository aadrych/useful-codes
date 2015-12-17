#!/usr/bin/python

# ---------------------------------------------------------------------------------------------------
#                 Build job folders and files for vacancy formation energy calculation
# ---------------------------------------------------------------------------------------------------
# Author:  C P Race
# Email:   christopher.race@manchester.ac.uk
# Date:    2014 / 12 / 02
# ---------------------------------------------------------------------------------------------------
# Description: Simple python script to generate directory structure and input files for a 
#              calculation of the vacancy formation energy in a model material.
#              Takes a base input file for Lammps and selectively replaces code strings with a 
#              series of different values
#
# ---------------------------------------------------------------------------------------------------

import os
import shutil

# Define a function to replace text in base input files
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

# Base input file. Strings in this file will be replaced with a series of different values
baseLammpsFile = 'in.base'
# File for EAM Fe empirical potential
potentialFile ='Fe.eam.fs'
coordsfile='coords.lmps'
jobFile = 'jobList.txt'
foutJobList = open(jobFile, 'w')

#a = 2.8665  # Equilibrium lattice parameter

k=[1,2,3,4,5,6,7,8]
# Loop over values of number of unit cells in simulation
# Create a folder and lammps input files for each variant

for j in range(len(k)):
    # Create  a folder for simulation and copy in the empirical potential file
    path = './555-111pka-fixxyz-min-neb-'+str(k[j])+'/' + '/'
    finalfile='pka188-min-'+str(k[j])+'.final'
    #pkaFile='../Potentials/fe1.lmps'
    if not os.path.exists(path):
    	os.makedirs(path, mode=0o777)
        shutil.copy2(potentialFile, path)
        shutil.copy2(coordsfile, path)
        shutil.copy2(finalfile, path)
    
        
    # Define values to replace in base input file
    replacements = {
        'INPUT':str(k[j])

    }
        
    # Create a lammps file and use base file with string replacements to create unique variant
    inputLammpsFile = baseLammpsFile
    outputLammpsFile = path+'in.lmps'        
    finLammps = open(inputLammpsFile, 'r').read()
    foutLammps = open(outputLammpsFile, 'w')
    out = replace_all(finLammps, replacements)
    foutLammps.write(out)
    foutLammps.close()
    foutJobList.write(path + '\n')

foutJobList.close()
