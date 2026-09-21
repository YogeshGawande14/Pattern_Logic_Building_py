def print_tri(row,col):
    for i in range(row):
        for j in range(col-i):
            print("*",end=" ")
        print()

row=5;
col=6;
print_tri(row,col)

