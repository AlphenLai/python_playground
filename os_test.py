import os, sys
import glob

barcode = 'black'

ph = ''
# listing directories
print ("The dir is: %s" % os.listdir(os.getcwd()))

existed_folder = glob.glob('CubeLOGS/'+barcode+'*')
print (existed_folder)
if (existed_folder):
    ph = '-' + str(len(existed_folder))

# renaming directory ''tutorialsdir"
os.rename("CubeLOGS/temp","CubeLOGS/"+barcode+ph)

print ("Successfully renamed.")

# listing directories after renaming "tutorialsdir"
print ("the dir is: %s" %os.listdir(os.getcwd()))