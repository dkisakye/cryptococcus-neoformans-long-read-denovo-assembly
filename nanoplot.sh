#!/bin/bash
#SBATCH -N 1
#SBATCH -n 32
#SBATCH --partition=amd2tb
#SBATCH --mem=100000mb
#SBATCH --time=12:00:00
#SBATCH --mail-type=ALL
#SBATCH --job-name=nanoplot
#SBATCH -A nielsenk
#SBATCH -o nanoplot_all_%j.output
#SBATCH -e nanoplot_all_%j.error

cd ../RIS_analysis_2/samples/ALL_LONG_READS/

module load nanoplot #load nanoplot


for SAMP in `cat ../../RIS_analysis_2/samples/ALL_LONG_READS/all_samples.txt`;

do 
READS=${SAMP}*.fq

NanoPlot -t 8 --fastq ${READS} -p ${SAMP} --loglength -o ../../RIS_analysis_2/samples/fastqc/${SAMP}_nanoplot --plots dot

done

