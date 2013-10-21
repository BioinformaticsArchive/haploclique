import sys
from cStringIO import StringIO

if len(sys.argv) == 1:
    print("Please provide the clique_to_reads.tsv file")
    sys.exit(0)

clique_name = {}
with open(sys.argv[1]) as f:
    for line in f:
        split = line[0:-1].split("\t")
        clique_name[split[0]] = split[1]

#for x in clique_name:
#    print(x)

for lines in sys.stdin:
    if len(lines) > 0:
        split = lines.split(" ")
        sys.stdout.write(split[0])
        sys.stdout.write("-+-")
        sys.stdout.write(clique_name[split[0]])
        for i in xrange(1,len(split)):
            sys.stdout.write(" ")
            sys.stdout.write(split[i])