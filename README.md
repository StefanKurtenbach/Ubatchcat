# batchcat
Merge (cat) fastq.gz files in multiple folders and save merged files for each folder

Options:
-p Y (default is -p N) 
triggers paired-end mode. All files containing "_R1_" in filename will be merged and saved seperatelly from files with                      "_R2_" in file name.

Usage:
python Ubatchcat.py
or
python Ubatchcat.py -p Y

Script will merge (cat) files in all folders and save a seperate output file for each folder. Output files will be named according to their folder name.

BEFORE RUN:

    --- UBatchcat.py
    --- Sample1
      --- 2016-05-03-01-F47_S7_L001_R1_001.fastq.gz
      --- 2016-05-03-01-F47_S7_L002_R1_001.fastq.gz
      --- 2016-05-03-01-F47_S7_L003_R1_001.fastq.gz
    --- Sample2
      --- 2016-05-03-07-Mel202-ctrl3_S4_L001_R1_001.fastq.gz
      --- 2016-05-03-07-Mel202-ctrl3_S4_L002_R1_001.fastq.gz
      --- 2016-05-03-07-Mel202-ctrl3_S4_L003_R1_001.fastq.gz
      --- 2016-05-03-07-Mel202-ctrl3_S4_L004_R1_001.fastq.gz
    

AFTER RUN:

    --- UBatchcatv1-1.py
    --- Sample1
      --- 2016-05-03-01-F47_S7_L001_R1_001.fastq.gz
      --- 2016-05-03-01-F47_S7_L002_R1_001.fastq.gz
      --- 2016-05-03-01-F47_S7_L003_R1_001.fastq.gz
    --- Sample2
      --- 2016-05-03-07-Mel202-ctrl3_S4_L001_R1_001.fastq.gz
      --- 2016-05-03-07-Mel202-ctrl3_S4_L002_R1_001.fastq.gz
      --- 2016-05-03-07-Mel202-ctrl3_S4_L003_R1_001.fastq.gz
      --- 2016-05-03-07-Mel202-ctrl3_S4_L004_R1_001.fastq.gz
    --- Output
      --- Sample1.fastq.gz
      --- Sample2.fastq.gz
