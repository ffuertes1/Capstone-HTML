FileName = "fil.txt"  # Corrected the filename
data = open(FileName, "r").readlines()
data.sort()

for i in range(len(data)):
    print(data[i])  # Corrected the print statement

