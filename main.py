erp = []

with open("dataset/machine.data", "r") as f:
    for line in f:
        columns = line.strip().split(",")
        erp.append(int(columns[9]))

print(erp)
