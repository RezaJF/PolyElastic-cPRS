#! /bin/bash

module load plink/1.90b
module load R/3.6.0/gcc.7.1.0
module load python/3.7.3/gcc.4.4.7

if [ $# -ne 3 ]
then
    echo "Usage: `basename $0` PATH_to_PRSice TARGET_BED OUTPUT_DIRECTORY"
    exit 1
fi

echo "`date -u` : Run started successfully" > logfile.txt



PATH_to_PRSice=$1
target=$2
out=$3


cat base_sum_stats.txt | while read i j k
	do
        	${PATH_to_PRSice} \
                	--A1 A1 \
                	--A2 A2 \
                	--bar-levels 1e-40,1e-30,1e-20,1e-10,1e-09,1e-08,1e-07,1e-06,1e-05,0.0001,0.0002,0.0005,0.001,0.002,0.005,0.01,0.05,0.1,1 \
                	--base $i \
                	--beta  \
                	--binary-target F \
                	--bp BP \
                	--chr CHR \
                	--clump-kb 250 \
                	--clump-p 1.000000 \
                	--clump-r2 0.100000 \
                	--interval 5e-05 \
                	--lower 5e-08 \
                	--missing MEAN_IMPUTE \
                	--model add \
                	--out ${out}/${k}_prs \
                	--perm 10000 \
                	--pvalue P \
                	--score avg \
                	--seed 910185829 \
                	--snp SNP \
                	--stat $j \
                	--target ${target} \
                	--thread 1 \
                	--upper 0.5

	done


echo "`date -u` : PRS calculation finished successfully!" >> logfile.txt


ls *_prs.best > PRS_list.txt

cat PRS_list.txt | while read i,
	do
        	sed -i 's/[[:blank:]]*$//' $i
        	sed -i -e "1s/PRS/$i/" $i

	done

echo "`date -u` : PRS pre-processing finished successfully!" >> logfile.txt
echo "`date -u` : Initiating composite PRS score calculation!" >> logfile.txt


python auxiliary.py


