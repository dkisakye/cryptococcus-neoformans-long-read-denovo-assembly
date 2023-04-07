#!/bin/bash
#SBATCH -N 1
#SBATCH -n 16
#SBATCH --partition=msismall
#SBATCH --mem=10000mb
#SBATCH --time=2:00:00
#SBATCH --mail-type=ALL
#SBATCH --job-name=mummer_isolate_vs_FungidbH99
#SBATCH -A nielsenk
#SBATCH -o mummer_isolate_vs_FungidbH99_renamed%j.output
#SBATCH -e mummer_isolate_vs_FungidbH99_renamed%j.error

module load mummer/4.0.0.beta2

for sample in $(cat ../../RIS_analysis_2/nextpolish/all_genomes/renamed_genomes/sample_list.txt)
do
ISOLATE="../../RIS_analysis_2/nextpolish/all_genomes/renamed_genomes/${sample}_renamed_genome.nextpolish.fasta"
done
#contigs were renamed in a previous script to shorten their names

STATS="98perc_5000bp"
DIR="../../RIS_analysis_2/mummer_comparisons/${sample}_vs_FungidbH99_renamed"_${STATS}
mkdir -p ${DIR}
cd ${DIR}
H99="../../RIS_analysis_2/H99/fungidb-genomes-2022-05-16/renamed_chromosomes/FungiDB-57_CneoformansH99_Genome_renamed_chr.fasta"
#changed the numbering of the H99 chromosomes in a previous script to numerical format,with the exception of the mitochondrial genome
QRY=${sample}
LENF=${STATS/bp}
LEN=${LENF/98perc_}

nucmer ${H99} ${ISOLATE} --prefix="${QRY}_vs_H99" 
delta-filter -i 98 -l ${LEN} -q "${QRY}_vs_H99.delta" > "${QRY}_vs_H99_${STATS}.filter" # -i (identity), -l match length, -q for mapping querry contigs to ref
mummerplot -l --fat --png -p "${QRY}_vs_H99" "${QRY}_vs_H99_${STATS}.filter" # -l layout 
show-coords -r -T -l -H "${QRY}_vs_H99_${STATS}.filter" > "${QRY}_vs_H99_${STATS}.coords" # -r sort lines by ref IDs and coordinates, -T switch to tab delim file, -l include length of sequence in output format, -H exlcude header (used this option for input into ribbon)
show-diff "${QRY}_vs_H99_${STATS}.filter" > "${QRY}_vs_H99_${STATS}.diff" # outputs structural differences between sequences
