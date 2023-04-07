#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 8
#SBATCH --partition=msibigmem
#SBATCH --mem=12000mb
#SBATCH --time=24:00:00
#SBATCH --mail-type=ALL
#SBATCH --job-name=liftoff
#SBATCH -A nielsenk
#SBATCH -o liftoff%j.output
#SBATCH -e liftoff%j.error


conda activate liftoff

cd ../../RIS_analysis_2/liftoff/

for DIR in $(find ../../RIS_analysis_2/nextpolish/ -maxdepth 1  -type d -name "UgCl*")
do
    SAMP=$(basename $DIR)
    #mkdir -p ../../RIS_analysis_2/liftoff/${SAMP}
    cd ../../RIS_analysis_2/liftoff/${SAMP}
    #GFF3="../../RIS_analysis_2/H99/FungiDB-61_15_02_2023/FungiDB-61_CneoformansH99.gff"
	GFF3="../../RIS_analysis_2/H99/ncbi-genomes-2023-02-20/GCA_000149245.3_CNA3_genomic.gff" #liftoff run with files from ncbi, but was not sucessful when run with .gff and .fasta files from fungidb
	REFERENCE="../../RIS_analysis_2/H99/ncbi-genomes-2023-02-20/GCA_000149245.3_CNA3_genomic.fa"    
TARGET="../../RIS_analysis_2/nextpolish/${SAMP}/genome.nextpolish.fasta"
    #REFERENCE="../../RIS_analysis_2/H99/FungiDB-61_15_02_2023/FungiDB-61_CneoformansH99_AnnotatedCDSs.fasta"
   
 liftoff -g ${GFF3} -cds -p 8 -o ${SAMP}_annotations.gff -u ${SAMP}_unmapped_annotations.gff ${TARGET} ${REFERENCE}

done


