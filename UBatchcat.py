# UBatchcat Version 2.1

import os
import argparse
import os

#get arguments from command line

parser = argparse.ArgumentParser(description='Uaveragebedgraphs_args')
parser.add_argument('-p','--paired_end', help='when set to "Y" Ubatchcat will look for _R1_ and _R2_ in filenames and cat accordingly', required=False, type=str, default = "N")
args = vars(parser.parse_args())
pairedend = args['paired_end']

folderlist = [a for a in os.listdir('.') if os.path.isdir(a)]
bufferSize = 80000000  # Adjust this according to how memory efficient you need the program to be.
os.makedirs("Output")

if pairedend == "Y":
    print("Paired-end mode triggered")
#R1 reads
    for folder in folderlist:
        fileList = sorted([f for f in os.listdir('./'+folder)])
        print("Woking on folder "+ folder + " R1 reads")
        destFilename = "./Output/"+folder+"_R1.fastq.gz"

        with open(destFilename, 'wb') as destFile:
            for fileName in fileList:
                if fileName.find("_R1_") != -1:
                    print("   " + fileName)
                    with open("./"+folder+"/"+fileName, 'rb') as sourceFile:
                        chunk = True
                        while chunk:
                            chunk = sourceFile.read(bufferSize)
                            destFile.write(chunk)
#R2 reads
    for folder in folderlist:
        fileList = sorted([f for f in os.listdir('./' + folder)])
        print("Woking on folder " + folder + " R2 reads")
        destFilename = "./Output/" + folder + "_R2.fastq.gz"

        with open(destFilename, 'wb') as destFile:
            for fileName in fileList:
                if fileName.find("_R2_") != -1:
                    print("   " + fileName)
                    with open("./" + folder + "/" + fileName, 'rb') as sourceFile:
                        chunk = True
                        while chunk:
                            chunk = sourceFile.read(bufferSize)
                            destFile.write(chunk)

if pairedend == "N":
    print("Single-end reads")
    check_R1_ = False
    check_R2_ = False
    for folder in folderlist:
        fileList = sorted([f for f in os.listdir('./' + folder)])
        print("Woking on folder "+ folder)
        destFilename = "./Output/" + folder + ".fastq.gz"
        with open(destFilename, 'wb') as destFile:
            for fileName in fileList:
                print("   " + fileName)
                if fileName.find("_R1_"): check_R1_ = True
                if fileName.find("_R2_"): check_R2_ = True
                with open("./" + folder + "/" + fileName, 'rb') as sourceFile:
                    chunk = True
                    while chunk:
                        chunk = sourceFile.read(bufferSize)
                        destFile.write(chunk)
    if check_R1_ == True and check_R2_ == True:
        print("******** WARNING!!! SURE THIS IS SINGLE END SEQ DATA?? ********")
        print("******** WARNING!!! SURE THIS IS SINGLE END SEQ DATA?? ********")
        print("******** WARNING!!! SURE THIS IS SINGLE END SEQ DATA?? ********")
