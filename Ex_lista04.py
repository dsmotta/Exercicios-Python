num = []

for i in range(0,5):
    n = int(input(f'Digite um valor: '))
    if i == 0 or n > num[-1]:
        num.append(n)
    else:
        pos=0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                break
            pos +=1
    
print(num)