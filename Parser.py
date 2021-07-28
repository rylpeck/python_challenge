import re

def extractIP(piece):

    __regex = '(?:(?:1\d\d|2[0-5][0-5]|2[0-4]\d|0?[1-9]\d|0?0?\d)\.){3}(?:1\d\d|2[0-5][0-5]|2[0-4]\d|0?[1-9]\d|0?0?\d)'

    #__regex = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

    __extracted_Ip = re.findall(__regex, piece)
    return (__extracted_Ip)




