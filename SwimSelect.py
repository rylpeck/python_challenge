import IOManager
import argparse
import sys

parser = argparse.ArgumentParser(description = 'System to read, save, load and parse through ip addresses')

parser.add_argument('-r', metavar='f', type = str, required=True, help = 'reads in a file containing ip addresses')
parser.add_argument('-s', metavar='f', type = str, help = 'will save the stripped file with filename given')

parser.add_argument('-geoip', action='store_true', help="performs geoip lookup, adding save will save the file")
parser.add_argument('-rdap', action='store_true', help="performs RDAP lookup, adding save will save the file, WARNING: RDAP server has a restriction on how many requests sent per minute, RDAP will take time")

parser.add_argument('-geoipsave', type = str, help = 'Saves the result of geoip lookup with filename given')
parser.add_argument('-rdapsave', type = str, help = 'Saves the result of an RDAP lookup with filename given')

parser.add_argument('-select',  type = str, help = "Will only show an ip and the given catagory, examples in readme")
parser.add_argument('-where',  type = str, help = "used with select, will only show entries in the catagory where the entry matches")

parser.add_argument('-qrdap', action='store_true', help="flag, will only search on RDAP")
parser.add_argument('-qgeoip', action='store_true', help="flag, will only search on geoip")

#renaming a file will replace the file if it exists, be careful
#reader flags


#-ip 
#-rdap
#-l , loads a given saved version
#TODO add sorting ones once we have the rolled out system

def main():
    args = parser.parse_args()
    #print(args.r)
    #print("hey")
    print("Welcome to parser tool")

    if (args.where):
        if (args.select):
            print()
        else:
            sys.exit("ERROR: No select given for where")

       
    IOManager.reader(args.r)

    
    if (args.select):
        IOManager.clearResults()

    if (args.s):
        IOManager.renameFile(args.s, "tempList.txt")

    if (args.geoip or args.geoipsave):
        if (args.select):
            if (args.qrdap == False):
                if (args.where):
                    IOManager.iplookUp(args.select, args.where)
                else:
                    IOManager.iplookUp(args.select, None)
        else:
            IOManager.iplookUp(None, None)
        if (args.geoipsave):
            IOManager.renameFile(args.geoipsave, "tempipjson.txt")
            print("Wrote geoip to file")


    if (args.rdap or args.rdapsave):
        if (args.select):
            if (args.qrdap == False):
                if (args.where):
                    IOManager.rdaplookup(args.select, args.where)
                else:
                    IOManager.rdaplookup(args.select, None)
        else:
            IOManager.rdaplookup(None, None)
        
        if (args.rdapsave):
            IOManager.renameFile(args.rdapsave, "tempRDAP.txt")
            print("Written to file")

    
    IOManager.removeFile("tempipjson.txt")
    IOManager.removeFile("tempList.txt")
    IOManager.removeFile("tempRDAP.txt")

    print("Done")



if __name__ == "__main__":
    main()

