#!/usr/bin/env python3

# This script converts the unstructured memorial.txt format to JSON

import sys, json

all_crews = []
current_crew = {"crew":{}}
current_position = None

# The first 27 lines are ASCII art and fluff
for _ in range(27):
    next(sys.stdin)

for l in sys.stdin:
    line = l.rstrip()

    if line == "":
        all_crews.append(current_crew)
        current_crew = {"crew":{}}
        current_position = None
        continue

    if "-" in line:
        bits = [s.strip() for s in line.split("-")]
        years = "-".join(bits[:-1])
        current_crew["years"] = years
        line = bits[-1]

    if ":" in line:
        s = [t.strip() for t in line.split(":")]
        current_position = s[0]
        current_crew["crew"][s[0]] = s[1]
    elif current_position is not None:
        # Sometimes there are multiple people for one position, we
        # just append to the name
        current_crew["crew"][current_position] = f'{current_crew["crew"][current_position]}, {line.strip()}'

print(json.dumps(all_crews, indent=4))
