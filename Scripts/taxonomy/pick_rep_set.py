#!/bin/bash

#SBATCH -p short
#SBATCH -n 24
#SBATCH -t 1:00:00
#Load modules to run python
module load eb
module load Miniconda2
# loading virtualenv
echo "loading virtualenv"
source activate qiime1
# setting temporary directory
export TMPDIR=~/qiime_tmp
# pick representative sequence
echo "Picking representative sequences"
time pick_rep_set.py -i ./otus_closed_silva/uclust_ref_picked_otus/seqs_otus.txt -f ./slout/seqs.fna -o rep_set_silva.fna
source deactivate
