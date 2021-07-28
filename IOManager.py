from typing import Type
import Parser
import Lookup
import os
import json
import time

from os import path


def chunkReader(fileopened):
    chunksize = 1024
    while True:
        data = fileopened.read(chunksize)
        if not data:
            break
        yield data


def writeFile(data, name):

    f = open(name, "a", encoding='utf-8')
    for d in data:
        f.write(str(d))
        f.write(f'\n')
    f.close()

def writeDownResults(data):
    with open('Results.txt', 'a', encoding='utf-8') as f:
        for d in data:
            f.write(str(d))
            f.write(f'\n')
    f.close()


def renameFile(rename, oldname):
    print("better")
    if (path.exists(rename)):
        os.remove(rename)
    if (path.exists(oldname)):
        os.rename(oldname, rename)
    else:
        print("Error no temp found, program error")
    return

def clearResults():
    if (path.exists("results.txt")):
        os.remove("results.txt")

def removeFile(filename):
    if (path.exists(filename)):
        os.remove(filename)

#a really simple search to find in dict where things are, works for ip and rdap
def quickSearch(data,select,where):
    #print("hey")

    tempList = []
    for d in data:
        #print(d['ip'])
        if (d[select]):
            if (where):
                if (d[select] == where):
                    tempString = "IP: " + d['ip'] + ", " + select + " " + where
                    tempList.append(tempString)
            else:
                tempString = "IP: " + d['ip'] + ", " + select + " " + d['type']
                tempList.append(tempString)
    
    writeFile(tempList, "Results.txt")

    return
    #will always print results to file listed as "results"
    
#section controls rdap lookup and saving
def rdaplookup(select, where):
    print("Logging RDAP")
    if (path.exists("tempRDAP.txt")):
        #print("purging cache")
        os.remove("tempRDAP.txt")

    tempList = []
    sizeCount = 0
    with open('tempList.txt') as file:
        for line in file:
            time.sleep(3)
            data = Lookup.RDAP(line)
            
            tempList.append(data)
            sizeCount += 1

            if (sizeCount == 30):
                if (select != None):
                    quickSearch(tempList,select,where)
                writeFile(tempList, 'tempRDAP.txt')
                
                sizeCount = 0
                tempList.clear()

    if (sizeCount >= 1):
        if (select != None):
            quickSearch(tempList,select,where)

        writeFile(tempList, 'tempRDAP.txt')
        tempList.clear()
        
    #print("wrote rdap cache")


#section controls looking up ip's and caches them
def iplookUp(select, where):
    print("Logging geoip")

    if (path.exists("tempipjson.txt")):
        #print("purging cache")
        os.remove("tempipjson.txt")    
    
    sizeCount = 0
    tempList = []
    with open('tempList.txt') as file:
        for line in file:
            #print(line)
            #limit io operations
            data = Lookup.IPGeo(line)

            tempList.append(data)
            sizeCount += 1

            if (sizeCount == 30):
                if (select != None):
                    quickSearch(tempList,select,where)
                writeFile(tempList, "tempipjson.txt")
                
                sizeCount = 0
                tempList.clear()


            #writeDownJSON(data)
    if (sizeCount >= 1):
        if (select != None):
            quickSearch(tempList,select,where)
        writeFile(tempList, "tempipjson.txt")
        tempList.clear()

    #print("wrote ip cache")

def reader(name):
    
    #print("Reading in file")
    
    if (path.exists("tempList.txt")):
        #print("purging ipcache")
        os.remove("tempList.txt")

    tempList = []
    sizeCount = 0

    with open(name, 'r') as file:
        for line in file:
            data = Parser.extractIP(line)
            for d in data:
                tempList.append(d)
            #tempList.append(data)
            sizeCount += 1

            if (sizeCount == 30):
                writeFile(tempList, "tempList.txt")
                sizeCount = 0
                tempList.clear()


            #writeDownJSON(data)

    if (sizeCount >= 1):
        writeFile(tempList, "tempList.txt")

            #print(piece, f"\n")

    #print("created tempfileip list")

    return

