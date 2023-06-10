#ref: https://www.ewdna.com/2012/04/pythonoswalk.html
# https://docs.python.org/3/library/os.html?highlight=walk#os.walk
import os
from os.path import join, getsize
for root, dirs, files in os.walk("D:\\"):
    print(root, "consumes", end=" ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
#???
import os
from os.path import join, getsize
for a, b, c in os.walk("D:\\"):
    print(a, "consumes", end=" ")
    print(sum(getsize(join(a, name)) for name in c), end=" ")
    print("bytes in", len(c), "non-directory c")

    
    
    
    ###
#ref: https://www.ewdna.com/2012/04/pythonoswalk.html
# https://docs.python.org/3/library/os.html?highlight=walk#os.walk
# https://medium.com/seaniap/python-os-walk-%E5%88%97%E5%87%BA%E6%89%80%E6%9C%89%E7%9B%AE%E9%8C%84%E8%88%87%E6%AA%94%E5%90%8D-b638b9c4eba2

    import os
from os.path import join, getsize
#for root, dirs, files in os.walk("D:\\",topdown=True):
project_dir = "D:\\"
source = os.walk(project_dir)
for folder, subfolders, filenames in source:
    print(f'目前資料夾路徑為：{folder}')
    
    for subfolder in subfolders:
        print(f'{folder}的子資料夾為：{subfolder}')
    for filename in filenames:
        print(f'{folder}/{subfolder}內含檔案為：{filename}')
