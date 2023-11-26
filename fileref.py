#ref: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory


import glob
# All files and directories ending with .txt and that don't begin with a dot:
print(glob.glob("C:\\Users\\tiger\\Pictures\\Saved Pictures\\*.txt")) 
# All files and directories ending with .txt with depth of 2 folders, ignoring names beginning with a dot:
print(glob.glob("C:\\Users\\tiger\\Pictures\\Saved Pictures\\*.jpg")) 
