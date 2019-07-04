#!/bin/csh -f 

#$ -o ../logs/log.scen1.aug.txt	 			 ##$ output file name

#$ -N s1aug						##$ name of my job
#$ -S /bin/csh						##$ specify the shell
#$ -cwd							##$ job is submitted from here
#$ -V  							##$ uses current env variables / preserves your environment
#$ -q Students.q 
#$ -pe FillUp 1 					##$ set paralel environment to run parallel 
#$ -j y							##$ joint output and error into one file
#$ -M ehsan.mosadegh@dri.edu 
#$ -m abe


#source /etc/csh.cshrc					##$ to load the module for compiling
source /scratch/ehsanm/virtualEnv/virenvConda/bin/activate.csh virenvConda

module purge
module load intel/2015
module list
unlimit
limit
 
echo " job =====> submitted" 			
date

python -u ../run_scripts/spatial_CMAQ_analysis_scen1_aug.py > ../logs/log.${CMAQ_POL}.scen1.aug.txt

echo " job =====> ended"
date