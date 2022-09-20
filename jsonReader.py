import json
import csv
import argparse
import logging
import os
from os import path
from sys import argv
from types import *
from xml.dom.minicompat import StringTypes



def main():
    parser = argparse.ArgumentParser(
        description = 'Convert json file to csv'
    )
    parser.add_argument(    
        '-i', 
        '--inputFolder', 
        dest = 'inputFolder',
        help = 'Source file',
        required = True,
        default = None 
    )
    parser.add_argument(
        '-o', 
        '--outputFile', 
        dest = 'outputFile', 
        help = 'csv file',
        required = True,
        default = None 
    )
    args = parser.parse_args()
    inputFolder = args.inputFolder
    outputFile = args.outputFile
    fileData = []

    writeHeader = True
    itemKeys = []

    try:
        # load all csv files in the inputFolder into an array of dictionaries
        for file in sorted(os.listdir(inputFolder)):
            if file.endswith(".json"):
                with open(os.path.join(inputFolder, file), 'r') as f:
                    tempData = json.load(f)
                    fileData.append(tempData)

    except Exception as x:
        raise x

    with open(outputFile, 'w') as csvFile:
        writer = csv.writer(csvFile)
        keys = ["resourceId", "headline", "description", "articleBody"]
        writer.writerow(keys)
        itemInfo = []
        
       # write keys from each dictionary in the array to the csv file
        for data in fileData:
            info = [data[key] for key in keys] 
            if all([isinstance(data[key], StringTypes) for key in keys]):
                [itemInfo.append(value) for value in info]
            else:
                itemInfo.append(str(info.decode()))


            writer.writerow(itemInfo)
                
if __name__ == "__main__":
    main()