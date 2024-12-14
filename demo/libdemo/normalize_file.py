import re

with open("story.txt", "rt") as f:
    contents = f.read()

result = re.sub(' +', ' ', contents)  # replace one or more spaces with one space
result = re.sub('\n+', '\n', result)  # replace one or more newline with one newline

with open("story.txt", "wt") as f:
    f.write(result)
