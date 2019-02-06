#
import os,shutil

def findFiles(OrgPath,DestPath):
    if os.path.exists(DestPath):
        # pass
        shutil.rmtree(DestPath)
    else:
        os.makedirs(DestPath)
    for dir,subdir,files in os.walk(OrgPath):
        for file in files:
            if file.endswith('.txt') or file.endswith('.pdf'):
                shutil.copy(os.path.join(dir,file),DestPath)
                # print(os.path.join(dir,file))

def FindBigFiles(Path):
    for dir,subdir,files in os.walk(Path):
        for file in files:
            # print(file)
            if os.path.getsize(os.path.join(dir,file)) > 1024*1024:
                print(os.path.join(dir,file) + ':')
                print(os.path.getsize(os.path.join(dir,file)))

# findFiles("d:\\test\\",'d:\\test1\\')



FindBigFiles('d:\\test\\')
# os.makedirs('d:\\test1\\')