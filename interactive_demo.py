import os

path = 'CU11'

if (os.path.isdir(path)):
    print ('exist')
else:
    os.mkdir(path)
    print ('created')


#new_cmd = input("Input new command\n")
#print ("<<:", new_cmd)
#print (new_cmd is 'log list all')
#while True:
#    new_cmd = input("then?\n")
#    if (new_cmd is 'b"log list all\n"'):
#        print ("yes")
#    else:
#        print (new_cmd, " (no)")