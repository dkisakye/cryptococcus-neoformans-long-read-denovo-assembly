import sys,os
#samps=['04CN03050','BK08','BK139','BK143','BK145','BK150','BK224','BK226','BK35','BK42','BK46','BK95','BMD1646','BMD494','BMD761','BMD854T1','LD2','NT7533']
samps=['H99','UgCl018','UgCl029','UgCl030','UgCl032','UgCl045','UgCl057','UgCl212','UgCl223','UgCl236','UgCl243','UgCl247','UgCl250','UgCl252','UgCl255','UgCl262','UgCl291','UgCl292','UgCl300','UgCl326','UgCl332','UgCl357','UgCl360','UgCl362','UgCl377','UgCl379','UgCl382','UgCl389','UgCl390','UgCl393','UgCl395','UgCl422','UgCl438','UgCl443','UgCl447','UgCl450','UgCl461','UgCl462','UgCl466','UgCl468','UgCl495','UgCl534','UgCl535','UgCl538','UgCl541','UgCl546','UgCl547','UgCl549']

#!/bin/bash
#SBATCH -N 1
#SBATCH -n 12
#SBATCH --partition=batch
#SBATCH --mem=24000mb
#SBATCH --time=24:00:00
#SBATCH --mail-type=ALL
#SBATCH --job-name=canu
#SBATCH -A nielsenk

for samp in samps:
	outfile = open('canu_'+samp+'_nanopore_slurm.sh','w')
	# bash lines
	outfile.write('#!/bin/bash\n#SBATCH -N 1\n#SBATCH -n 1\n#SBATCH --cpus-per-task=64\n#SBATCH --partition=msilarge\n#SBATCH --mem=125000mb\n#SBATCH --time=4:00:00\n#SBATCH --mail-type=ALL\n#SBATCH --job-name='+samp+'_nanopore_canu\n#SBATCH -o canu_'+samp+'_nanopore_%A.out\n#SBATCH -e canu_'+samp+'_nanopore_%A.err\n#SBATCH -A nielsenk\n\n\n\n')
	# specify the sample directory
	outfile.write('samp="'+samp+'"\n')
	outfile.write('DIR="../../RIS_analysis_2/samples/ALL_LONG_READS/"\n')
	outfile.write('READS="${samp}*.gz"\n\n')
	outfile.write('cd ${DIR}\n\n')
	# write the canu command 

	outfile.write('../canu-2.2/bin/canu -p ${samp}_raw_assembly -d ../../RIS_analysis_2/samples/RAW_CANU_ASSEMBLY/${samp}_raw_assembly useGrid=FALSE genomeSize=19m minReadLength=700 minOverlapLength=500 minInputCoverage=5 correctedErrorRate=0.144 -nanopore ${READS}\n\n')# nanopore reads have a separate flag and higher error rate compared to pacbio
	outfile.close()
	os.system("sbatch canu_"+samp+"_nanopore_slurm.sh")
