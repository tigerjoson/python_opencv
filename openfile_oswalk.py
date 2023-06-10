#ref: https://www.ewdna.com/2012/04/pythonoswalk.html
# https://docs.python.org/3/library/os.html?highlight=walk#os.walk
import os
from os.path import join, getsize
for root, dirs, files in os.walk("D:\\"):
    print(root, "consumes", end=" ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
