import os, fnmatch
#goal of code is to search through directories for readme files in txt and md format, list them, and list their respective paths. 
ListandPath = open('ReadmeListandPath.txt', 'a')
listOfFiles = os.listdir("..\\PythonDirectory")  
pattern = "readme.*"  
for root, dirs, files in os.walk("..\\PythonDirectory", topdown=False):
   for name in files:
      if fnmatch.fnmatch(name, pattern):
        print(os.path.join(root, name))
        List = os.path.join(root, name)
        ListandPath.write(str(List)+'\n')
