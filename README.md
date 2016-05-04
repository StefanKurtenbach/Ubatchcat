# batchcat
Batch cat fastq.gz files in all folders and makes multiple output (cat) files in a combined output folder

Script will merge (cat) files in all folders present where the python script is located, and save an output file for each folder. Output files will all be saved to the "Output" folder. Files will be named according to the folder name.


BEFORE RUN:

FolderX
    --- Batchcat.py
    
    --- Folder1
      --- 2016-05-03-01-F47_S7_L001_R1_001.fastq.gz
      --- 2016-05-03-01-F47_S7_L002_R1_001.fastq.gz
      --- 2016-05-03-01-F47_S7_L003_R1_001.fastq.gz
      
    --- Folder2
      --- 2016-05-03-07-Mel202-ctrl3_S4_L001_R1_001.fastq.gz
      --- 2016-05-03-07-Mel202-ctrl3_S4_L002_R1_001.fastq.gz
      --- 2016-05-03-07-Mel202-ctrl3_S4_L003_R1_001.fastq.gz
      --- 2016-05-03-07-Mel202-ctrl3_S4_L004_R1_001.fastq.gz
    

AFTER RUN:

FolderX
    --- Batchcat.py
    
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
      --- Sample.fastq.gz
