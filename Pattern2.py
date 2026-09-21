def print_alpha(row ,col) :
    for i in range(row):
        for j in range(col):
            print(chr(j+65),end=" ")
        print()
row=5;
col=8;
print_alpha(row,col);

