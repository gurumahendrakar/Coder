import os 
import shutil


os.chdir(os.path.join(os.getcwd(),'allfiles'))
# print(os.makedirs('Guru/Gurji'))
# print(os.removedirs('texting.csv'))

for x,y,z in os.walk(os.getcwd()):
    print(x)
    print(y)
    print(z)