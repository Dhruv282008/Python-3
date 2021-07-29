import os 
import shutil

path = input("Enter the folder to be copied : ")
destination = input("Enter the destination : ")

path = path + '/'
destination = destination + '/'

listoffiles = os.listdir(path)

for file in listoffiles:
    shutil.copy((path + file), (destination))
    
