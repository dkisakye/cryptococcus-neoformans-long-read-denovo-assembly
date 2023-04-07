import sys,os,glob

"""
samples=open ("samples.txt","r") 
samp_list=[]
for sample in samples:
        samp_list.append(sample.strip())
"""
samp_list=['UgCl_300', 'UgCl_332']
#samp_list = ['UgCl_250','UgCl_262','UgCl_300','UgCl_332','UgCl_379','UgCl_389','UgCl_461','UgCl_212','UgCl_255','UgCl_292','UgCl_326','UgCl_360','UgCl_382','UgCl_395','UgCl_535', 'UgCl_538',] 
#['UgCl_300','UgCl_236','UgCl_243','UgCl_247','UgCl_291','UgCl_357','UgCl_377','UgCl_390','UgCl_422','UgCl_438','UgCl_443','UgCl_447','UgCl_450','UgCl_462','UgCl_466', 'UgCl_468','UgCl_534','UgCl_541','UgCl_546','UgCl_547','UgCl_549']


for sample in samp_list:
 outfile=open("../next_polish_runconfig_"+sample.replace("_","")+".cfg","w")
 #outfile=open("../next_polish_runconfig_"+sample+".cfg","w")
 outfile.write("[General]\njob_type = local\njob_prefix = nextPolish\ntask = default\nrewrite = yes\nrerun = 3\nparallel_jobs = 4\nmultithread_jobs = 8\ngenome = ../../RIS_analysis_2/samples/ST93/"+sample+"/"+sample+"_assembly/"+sample.replace("_","")+"_assembly.contigs.fasta\ngenome_size = auto \nworkdir = ../../RIS_analysis_2/nextpolish/"+sample+"\npolish_options = -p 8\n\n\n[sgs_option]\nsgs_fofn = ../../RIS_analysis_2/nextpolish/sgs_"+sample.replace("_","")+".fofn\nsgs_options = -max_depth 100\n\n\n[lgs_option]\nlgs_fofn = ../../RIS_analysis_2/nextpolish/lgs_"+sample.replace("_","")+".fofn\nlgs_options = -min_read_len 2k -max_depth 80\nlgs_minimap2_options = -x map-ont\n\n")
 outfile.close()


for sample in samp_list:
        outfile2=open("../lgs_"+sample.replace("_","")+".fofn","w")
        outfile2.write("../../RIS_analysis_2/samples/ST93/"+sample+"/all_reads.fq.gz\n")
        outfile2.close()


for file in glob.glob("/../../../../../gerst035/nielsenk/UgCl/fastq/*R1*.fastq"):
        samp = os.path.basename(file).split('_')[0]
        if '-k' in samp:
                samp=samp[:-2]
        print(samp)
        outfile3=open("../sgs_"+samp+".fofn","w")
        outfile3.write(file+'\n')
        outfile3.write(file.replace("_R1_","_R2_")+'\n')

for sample in samp_list:
        outfile4=open("nextPolish_"+sample.replace("_","")+".sh","w")
        outfile4.write("#!/bin/bash -l\n#SBATCH -N 1\n#SBATCH -n 4\n#SBATCH -c 8\n#SBATCH --partition=amdsmall\n#SBATCH --mem=24000mb\n#SBATCH --time=24:00:00\n#SBATCH --mail-type=ALL\n#SBATCH --job-name=nextPolish_"+sample.replace("_","")+"\n#SBATCH -A nielsenk\n\n")
        outfile4.write("conda activate nextpolish\n\n/../../../bin/NextPolish/nextPolish ../next_polish_runconfig_"+sample.replace("_","")+".cfg\n\n")
        outfile4.close()
        os.system("sbatch nextPolish_"+sample.replace("_","")+".sh")
