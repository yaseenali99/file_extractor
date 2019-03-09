
import os
import shutil
import csv

#script run from directory where folders are located
path = os.getcwd()

print(path)
file_list = []




def extract_files(path,extensions):
    '''
    This function extracts all the .csv files from a folder structure and puts them in a folder called files.
    :param path:
    :return:
    '''
    #destination folder where files will be extracted to
    dest = os.path.join(path,"files")

    #creating destination folder
    if not os.path.isdir(dest):
        os.mkdir(dest)

        for dir,subdir,filelist in os.walk(path):
            for f in filelist:
                if f.endswith(extensions):
                    shutil.copy(os.path.join(dir,f),dest)
                    #print(os.path.abspath(f))
   
def get_extensions(path):
    ext = []
    for dir,subdir,filelist in os.walk(path):
        for f in filelist:
            ext.append(f.split('.')[-1])              
    return set(ext)

def main():
    path = os.getcwd()

    print(path)
    
    extensions = get_extensions(path)
    
    with open("ext.txt,'w'") as f:
        f.write(extensions)
    


if __name__ == "__main__":
    main()
    