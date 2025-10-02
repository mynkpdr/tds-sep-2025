import json
import sys

f = sys.argv[1] if len(sys.argv) > 1 else "q-multi-cursor-json.txt"
with open(f) as file:
    data = dict(line.strip().split("=", 1) for line in file if "=" in line)
print(json.dumps(data, separators=(",", ":")))
