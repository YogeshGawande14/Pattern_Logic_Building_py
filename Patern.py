def print_rect(row,col):
    for i in range(row):
        for j in range(col):
            print("*",end=" ")
        print()

row=7;
col=8;
print_rect(row,col);