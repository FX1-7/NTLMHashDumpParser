import csv
f = open("NTLMHashes.txt", "w")
with open(input("What is the file path you wish to open? "), 'r') as file:
    reader = csv.reader(file, delimiter=input("How do you want to split your string? "))
    for row in reader:
        LastObject = len(row) - 1
        print(row[LastObject])
        f.write(row[LastObject] + "\n")

f.close()
