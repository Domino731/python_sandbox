loop = 10
amount = 0;

print('while loop')
while amount < 10:
    print('Amount', amount)
    amount +=1

print('for loop')
for i in range(1,6):
    if i == 4:
        break

    print(i)
