fh = open("InterestedObjects")
IOSet = list()
for lines in fh:
    IOSet.append(lines.rstrip())
print(IOSet)