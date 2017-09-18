# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful
from shutil import copyfile




file = input('Give me a filename to copy: ')


def copier(f):
    try:
        f2 = f + "_copied" 
        copyfile(f, f2)
    except:
        pass
copier(file)