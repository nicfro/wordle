import json
from collections import defaultdict

output = defaultdict(list)
with open('words.txt') as f:
    for line in f:
        line = line.strip()
        length = len(line)
        output[length].append(line)

out_file = open("words.json", "w")
json.dump(output, out_file, indent = 4, sort_keys = False)
out_file.close()
