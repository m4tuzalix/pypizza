test = [7,15,8,3]

for x in range(len(test)-1):
    nx = test[x+1]
    cr = test[x]
    if test[x] > test[x+1]:
        test[x] = nx
        test[x+1] = cr

print(test)