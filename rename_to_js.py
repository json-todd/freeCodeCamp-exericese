"""
Enter the path of a folder
Re-define the extension of all files in the folder as .js 
"""

import os 

path = 'C:/Users/Tree Ant Full/Documents/Programming Learn/freecodecamp'

os.chdir(path)

for file in os.listdir():
    name, extension = os.path.splitext(file)
    newName = '{}{}'.format(name,'.js')
    os.rename(file,newName)