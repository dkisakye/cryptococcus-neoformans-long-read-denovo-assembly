This repo contains scripts used to perform long read denovo assembly on cryptococcus neoformans isolates
Steps:
1.Qc run with nanoplot.sh
2.Canu scripts created and run with create_canu_shells_nanopore_raw.py
3.Denovo assemblies polished with illumina short read sequences using nextpolish:make.config.files.nextpolish.py   
4.Whole genome alignments where performed using the mummer utility,nucmer. The output file (.delta) was filtered to retain alignments with 98 percent similarity per 5000bp:mummer_UgCl_isolate_vs_FungidbH99_renamed.sh 
