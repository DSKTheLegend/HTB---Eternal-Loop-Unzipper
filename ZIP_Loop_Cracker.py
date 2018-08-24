import sys
import zipfile
import optparse
from threading import Thread

def extractFile(zname):
    try:
        print '1'
        zFile = zipfile.ZipFile(zname)
        print '2'
        file_info =  zFile.infolist()
        print '3'
        filename =  file_info[0].filename
        print '4'
        password = filename.split(".")
        print '5'
        zFile.extractall(pwd = password[0])
        print '6'
        print "The file " + filename + " successfully extracted with password " + password[0]
        extractFile(filename)
        print '7'
       
    except:
        print "Did the script failed or did it decrypted ?"
        
def main():
    parser = optparse.OptionParser('usage: zipcracker.py ' + '-f <zipfile>')
    parser.add_option('-f', dest='zname',type='string',help='specify zip file')
    (options,args) = parser.parse_args()
    if (options.zname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
    extractFile(zname)

if __name__ == '__main__':
    main()
