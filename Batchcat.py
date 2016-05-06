# Batchcat version 1.0
# Stefan Kurtenbach

import os

folderlist = [a for a in os.listdir('.') if os.path.isdir(a)]
bufferSize = 80000000  # Adjust this according to how memory efficient you need the script to be
os.makedirs("Output")

for folder in folderlist:

    fileList = [f for f in os.listdir('./'+folder)]
    print("Woking on folder "+folder)
    destFilename = "./Output/"+folder+"-fastq.gz"


    with open(destFilename, 'wb') as destFile:
        for fileName in fileList:
            with open("./"+folder+"./"+fileName, 'rb') as sourceFile:
                chunk = True
                while chunk:
                    chunk = sourceFile.read(bufferSize)
                    destFile.write(chunk)
