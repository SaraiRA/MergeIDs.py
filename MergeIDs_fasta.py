# Merge Fasta Ids
import sys
 
ids=dict()
with open(sys.argv[1]) as myfile:
  for line in myfile:
    line=line.rstrip()
    if line.startswith('>'):
      id=line[1:]
    else:
      if id in ids.keys():
        ids[id] += line
      else:
        ids[id] = line
 
for key in ids.keys():
  print ">"+key
  print ids[key]
 
exit(0)
