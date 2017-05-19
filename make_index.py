import os

folder = 'Reports/'

next = folder + 'next.txt'

links = os.listdir(folder)

links.sort()
links.reverse()

f = open('index.md', 'w')

f.write("[The next (unofficial) report](" + next + ") \r\n")
f.write("[The latest report](" + folder + links.pop(0) + ") \r\n")
f.write("The rest: \r\n")
for string in links:
   f.write("[" + string + "](" + folder + string + ") \r\n")
