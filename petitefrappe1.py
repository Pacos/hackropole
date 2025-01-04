import re


with open(".resources/petitefrappe/petite_frappe_1.txt") as f:
    result = []
    for line in f:
        if match := re.search(r"EV_KEY.*KEY_(\w).*value 1", line):
            result.append(match.group(1))
    print("".join(result))
