# 创建一个文件夹

# 创建一系列文件 以 sapm000 开头

import os,shutil,re

# 找出文件名中的数字
# pattern = re.compile(r'(\d+)')
# for f_obj in os.listdir("d:\\Linux"):
    # print(file)
    # if f_obj.startswith('spam'):
    #     # print(f_obj)
    #     num = list(pattern.search(f_obj).groups(1))
    #     print(num[0])
os.chdir("d:\\Linux")

# 找到指定文件夹中所有带指定前缀的文件
o_filenames = [x for x in os.listdir('.') if '.' in x and
                x.startswith('spam')]
print(o_filenames)

# 定位缺失的编号
numRegex = re.compile(r'^[a-z]+(.*?).txt$')
o_num_list = []
for o_filename in o_filenames:
    t_name_re = numRegex.search(o_filename)
    o_num_list.append(t_name_re.group(1))
print(o_num_list)

n_num_list = []
for i in range(1,len(o_num_list)+1):
    t_i = '%03d' % i
    n_num_list.append(t_i)
print(n_num_list)

for i in n_num_list:
    if i not in o_num_list:
        print("abc%s.txt" % i)

# # 对文件改名以消除缺失的编号
# for i,v in zip(o_num_list, n_num_list):
#     shutil.move('abc%s.txt'%i, 'abc%s.txt'%v)
#
# print('Rename project is done!')




