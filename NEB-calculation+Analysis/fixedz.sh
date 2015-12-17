#!/bin/bash
#$ -S /bin/bash
#$ -cwd                                  # Job runs in current directory (where you run qsub)
#$ -V                                    # Job inherits environment (settings from loaded modules etc)
#$ -pe smp.pe 4                         # This example requests 32 cores (i.e., 2 physical nodes
#$ -t 1-8
# with InfiniBand networking hardware).
#python Buildjobs.py
SUBDIR=`awk "NR==$SGE_TASK_ID" jobList.txt`
cd $SUBDIR

mpirun -np 25 lmp_linux -partition 25x1 -in in.base > Fepka.out

