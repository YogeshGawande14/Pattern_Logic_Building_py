def print_Ntri(row ,col) :
    for i in range(row):
        for j in range(i):
            print(j,end=" ")
        print()
row=5;
col=8;
print_Ntri(row,col);

# Print Tringle Of Numbers ( same of one line other 22....then 3...)
def print_NtriX(row ,col) :
    for i in range(row):
        for j in range(i):
            print(i,end=" ")
        print()
row=5;
col=8;
print_NtriX(row,col);
