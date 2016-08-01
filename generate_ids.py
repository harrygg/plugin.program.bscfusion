import re

m3u = open("bulsat.m3u", 'r').read()
m = re.compile("logo=\"(.+?)\"").findall(m3u)
print "%s ids found" % len(m)

ids = open("excluded_ids.txt", "w")
for i in range (0, len(m)):
  ids.write(m[i] + '\n')
ids.close()
