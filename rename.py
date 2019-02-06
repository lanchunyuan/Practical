import os,sys
path = '/mnt/c/work/samples_50'
# lists = os.listdir(path)
# bmps = []
# for item in lists:
#     if os.path.splitext(item)[1] == ".bmp":
#         bmps.append(item)
# print(bmps)
# for i in range(len(bmps)):
i = 0
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        if file.find('-')>0:
            os.rename(os.path.join(path,file),os.path.join(path,f'{i:02d}.bmp'))
            # print(i)
            print(f'{file} ok')
    i += 1
