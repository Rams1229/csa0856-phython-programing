rows = int(input("enter the no.of rows: "))
for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")
