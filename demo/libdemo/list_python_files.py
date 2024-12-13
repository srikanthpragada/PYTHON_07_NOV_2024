import os

g = os.walk(r"c:\classroom\python\demo")
count = 0
for (dirname, folders, files) in g:
    for file in files:
        if file.endswith(".py"):
            print( dirname + "\\" + file)
            count += 1

print(f"Count = {count}")



