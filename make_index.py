import os

folder = 'Reports/'

next = folder + 'next.txt'

links = os.listdir(folder)

links.remove('next.txt')
links.sort()
links.reverse()

f = open('index.md', 'w')

f.write("[The next (unofficial) report](" + next + ") \n")
f.write("\n")
f.write("[The latest report](" + folder + links.pop(0) + ") \n")
f.write("\n")
f.write("The rest: \n")
f.write("\n")
for string in links:
   f.write("[" + string + "](" + folder + string + ") \n")
   f.write("\n")
